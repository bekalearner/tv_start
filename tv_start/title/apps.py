from django.apps import AppConfig


class TitleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'title'

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_app'

    def ready(self):
        import my_app.signals