from .models import User

## Custom user email login backend to replace
## the standard django one
##
class User_Backend(object):

    # Required method 1
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)
        except User.MultipleObjectsReturned:
            user = User.objects.filter(email=username).order_by('id').first()
        except User.DoesNotExist:
            return None

        if getattr(user, 'is_active') and user.check_password(password):
            return user
        return None

    # Required method 2
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesnotExist:
            return None
