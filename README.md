# CKEditor5 Full Configuration for Django
Full-featured CKEditor5 configuration for Django.

This repository provides a full-featured configuration for CKEditor5 in Django, including a custom toolbar, dark mode fix for the Django admin panel.

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
        'language': 'fa',
        'image': {
            'toolbar': [
                'imageTextAlternative', 'imageStyle:full', 'imageStyle:side'
            ]
        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells']
        },
        'placeholder': 'متن خود را وارد کنید...',
    }
}

# Custom CSS for Dark Mode Fix
CKEDITOR_5_CUSTOM_CSS = 'css/admin_dark_mode_fix.css'
