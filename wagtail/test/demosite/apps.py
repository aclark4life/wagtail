from django.apps import AppConfig


class DemositeAppConfig(AppConfig):
    default_auto_field = "django_mongodb.fields.ObjectIdAutoField"
    name = "wagtail.test.demosite"
