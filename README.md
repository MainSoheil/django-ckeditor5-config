# CKEditor5 Full Configuration for Django
Full-featured CKEditor5 configuration for Django.

This repository provides a full-featured configuration for CKEditor5 in Django, including a custom toolbar, dark mode fix for the Django admin panel.

installation:
```bash
pip install django-ckeditor-5
```

adding to installed apps in django setting:
```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # other apps ...
    "django_ckeditor_5"
]
```

## Features

- **Full Toolbar**: Includes a wide range of options, such as undo/redo, text formatting, alignment, lists, and more.
- **Customizable Placeholder**: You can set a custom placeholder for your editor.
- **Dark Mode Fix**: Includes custom CSS to fix color issues when using the editor in dark mode.

## Configuration

### 1. Add CKEditor5 Config to Your Django Project

In your Django settings file, add the following configuration:
```python
# CKEditor5 Full Configuration
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': {
            'toolbar_panel_id': 'toolbar',
            'toolbar_width': '100%',
            'items': [
                'undo', 'redo', '|',
                'heading', '|',
                'bold', 'italic', 'underline', 'strikethrough', '|',
                'alignment', 'fontFamily', 'fontColor', 'fontBackgroundColor', '|',
                'link', 'imageUpload', 'mediaEmbed', 'fileUpload', '|',
                'bulletedList', 'numberedList', 'todoList', '|',
                'blockQuote', 'insertTable', 'codeBlock', 'code', '|',
                'findAndReplace', 'highlight', 'removeFormat'
            ],
            'shouldNotGroupWhenFull': True
        },
        'language': 'en', # set any language you want
        'image': {
            'toolbar': [
                'imageTextAlternative', 'imageStyle:full', 'imageStyle:side'
            ]
        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells']
        },
        'placeholder': 'Enter Your Text...',
    }
}

# Custom CSS for Dark Mode Fix
CKEDITOR_5_CUSTOM_CSS = 'css/admin_dark_mode_fix.css'
```

### 2. Add This Css Property To admin_dark_mode_fix.css File
1. In your Django project's static folder, create a directory named css.
2. Inside the css folder, create a file called admin_dark_mode_fix.css.
3. Inside the css folder, create a file called admin_dark_mode_fix.css.
```css
.ck.ck-editor {color: black !important;}
```
Adding this CSS property resolves the white text issue in the CKEditor5 editor within the Django admin panel. By default, both the text and background are white, making the text invisible. This fix ensures the text is clearly visible.
