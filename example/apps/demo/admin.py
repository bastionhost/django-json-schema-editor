from django.contrib import admin

from django_json_schema_editor.widgets import JSONSchemaEditorWidget

from .models import SchemaModel


@admin.register(SchemaModel)
class SchemaModelAdmin(admin.ModelAdmin):
    search_fields = ('data',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(SchemaModelAdmin, self).get_form(request, obj, widgets={'data': JSONSchemaEditorWidget}, **kwargs)
        return form
