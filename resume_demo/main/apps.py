from django.apps import AppConfig

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

# overwrite the ready method
# when this will fire up the app
    def ready(self):
        import main.signals