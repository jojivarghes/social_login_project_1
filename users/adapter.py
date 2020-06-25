from django.contrib.auth import get_user_model
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

User = get_user_model()


class PreSocialLoginAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        try:
            if sociallogin.is_existing:
                print(f'PreSocialLoginAdapter: sociallogin.is_existing')
                return
            user = User.objects.get(email=sociallogin.user.email)
            sociallogin.connect(request, user)
        except User.DoesNotExist:
            print(f'PreSocialLoginAdapter: sociallogin.not_existing')
