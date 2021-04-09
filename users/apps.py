from django.apps import AppConfig

# Using signals
class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals