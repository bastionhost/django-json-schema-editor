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
                'django_json_schema_editor/1.8c99a08b.chunk.css',
            ]
        }
        js = [
            'django_json_schema_editor/1.4b4cfb7b.chunk.js',
            'django_json_schema_editor/main.2c7dbe2d.chunk.js',
        ]
        return forms.Media(css=css, js=js)
