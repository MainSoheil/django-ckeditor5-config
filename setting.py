# Add this code in your django setting file

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
        'language': 'en',
        'image': {
            'toolbar': [
                'imageTextAlternative', 'imageStyle:full', 'imageStyle:side'
            ]
        },
        'table': {
            'contentToolbar': ['tableColumn', 'tableRow', 'mergeTableCells']
        },
        'heading': {
            'options': [
                {'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph'},
                {'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1'},
                {'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2'},
                {'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3'},
                {'model': 'heading4', 'view': 'h4', 'title': 'Heading 4', 'class': 'ck-heading_heading4'},
                {'model': 'heading5', 'view': 'h5', 'title': 'Heading 5', 'class': 'ck-heading_heading5'},
                {'model': 'heading6', 'view': 'h6', 'title': 'Heading 6', 'class': 'ck-heading_heading6'}
            ]
        },
        'placeholder': 'متن خود را وارد کنید...',
    }
}

CKEDITOR_5_CUSTOM_CSS = 'css/admin_dark_mode_fix.css'
