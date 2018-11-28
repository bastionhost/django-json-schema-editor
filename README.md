# django-json-schema-editor

A simple django field widget for editing json schema.

## Installation and usage
1. Install with pip
```
pip install django-json-schema-editor
```
2. Add "django_json_schema_editor" to your INSTALLED_APPS setting like this:
```
    INSTALLED_APPS = [
        ...
        'django_json_schema_editor',
        ...
    ]
```
3. In the form, set the field's widget to be "JSONSchemaEditorWidget", such as:
```
    self.fields['essay_response'].widget = JSONSchemaEditorWidget
```

To run the example project, run the server using the settings file in the example module.
```
python manage.py runserver --settings=example_project.settings.dev
```
