from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

from .finders import get_finders


class WagtailEmbedsAppConfig(AppConfig):
    name = "wagtail.embeds"
    label = "wagtailembeds"
    verbose_name = _("Wagtail embeds")
    default_auto_field = "django_mongodb.fields.ObjectIdAutoField"

    def ready(self):
        from . import signal_handlers  # noqa

        # Check configuration on startup
        get_finders()
