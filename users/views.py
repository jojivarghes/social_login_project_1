import copy

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.generic import ListView, DetailView
from django.dispatch import receiver
from django.shortcuts import redirect
from allauth.account.signals import user_signed_up
from allauth.socialaccount.signals import pre_social_login

User = get_user_model()


class UserListView(ListView):
    model = User


user_list_view = login_required(UserListView.as_view())


class UserDetailView(DetailView):
    model = User


user_detail_view = login_required(UserDetailView.as_view())


@login_required
def user_set_password(request):
    return render(request, 'users/user_set_password.html')
    # return redirect('/accounts/password/set/')


def update_user_info(user):
    github_name = linkedin_name = twitter_name = ''
    github_extra_data = linkedin_extra_data = twitter_extra_data = {}
    github_data = user.socialaccount_set.filter(provider='github')
    if github_data:
        github_extra_data = github_data[0].extra_data
        github_name = github_extra_data['name']

    linkedin_data = user.socialaccount_set.filter(provider='linkedin_oauth2')
    if linkedin_data:
        linkedin_extra_data = linkedin_data[0].extra_data
        linkedin_name = f'{linkedin_extra_data["firstName"]["localized"]["en_US"]} ' \
                        f'{linkedin_extra_data["lastName"]["localized"]["en_US"]}'

    twitter_data = user.socialaccount_set.filter(provider='twitter')
    if twitter_data:
        twitter_extra_data = twitter_data[0].extra_data
        twitter_name = twitter_extra_data['name']

    user_meta = {
        'github': github_extra_data,
        'linkedin': linkedin_extra_data,
        'twitter': twitter_extra_data,
    }
    name_list = [github_name, linkedin_name, twitter_name]
    name = next(s for s in name_list if s)
    if name:
        user.name = name
    user.meta = user_meta
    user.save()
    print(f'update_user_info: Updated user info')


@receiver(pre_social_login)
def update_user_info_on_login(sociallogin, **kwargs):
    print(f'update_user_info_on_login: called')
    if sociallogin.is_existing:
        print(f'update_user_info_on_login: sociallogin.is_existing')
        user = User.objects.get(email=sociallogin.user.email)
        update_user_info(user)
    else:
        print(f'update_user_info_on_login: sociallogin.not_existing')


@receiver(user_signed_up)
def update_user_info_on_signup(user, **kwargs):
    print(f'update_user_info_on_signup: called')
    update_user_info(user)


def login(request):
    return redirect('/accounts/login')


def logout(request):
    return redirect('/accounts/logout')
