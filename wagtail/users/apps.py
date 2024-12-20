from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WagtailUsersAppConfig(AppConfig):
    name = "wagtail.users"
    label = "wagtailusers"
    verbose_name = _("Wagtail users")
    default_auto_field = "django_mongodb.fields.ObjectIdAutoField"
    group_viewset = "wagtail.users.views.groups.GroupViewSet"
    user_viewset = "wagtail.users.views.users.UserViewSet"
