from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string


class JSONSchemaEditorWidget(forms.Widget):
    template_name = 'django_json_schema_editor/editor.html'

    def render(self, name, value, attrs=None, renderer=None):
        context = {
            'name': name,
            'data': value,
        }
        return mark_safe(render_to_string(self.template_name, context))

    @property
    def media(self):
        css = {
            'all': [
                'django_json_schema_editor/css/vendors~main.css',
            ]
        }
        js = [
            'django_json_schema_editor/js/main.js',
            'django_json_schema_editor/js/vendors~main.js',
        ]
        return forms.Media(css=css, js=js)
