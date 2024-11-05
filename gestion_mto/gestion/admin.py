from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from gestion import models

admin.site.register(models.Parada)
admin.site.register(models.Week)


admin.site.site_header = _("Administrar datos de parada y gestión")
admin.site.site_title = _("Administración de datos")
admin.site.index_title = _("Página principal")