from .models import User
from django.contrib.auth.hashers import check_password

class UserAuthBackend:

    def authenticate(self, request, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """
        Overrides the get_user method to allow users to log in using their email address.
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None