"""
Comprehensive Translation Wrapper Script
This script will automatically wrap all visible text in HTML templates with {% trans %} tags
"""
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / 'main' / 'templates' / 'main'

# Text patterns to wrap in {% trans %}
# These are common patterns where text needs translation

def wrap_text_in_trans(content):
    """
    Wrap text content in {% trans %} tags
    This is a comprehensive approach to handle most cases
    """
    
    # Skip if already has trans
    if '{% load i18n %}' not in content:
        # Add i18n load after static load
        content = content.replace(
            '{% load static %}',
            '{% load static %}\n{% load i18n %}'
        )
    
    # Pattern 1: Heading text (<h1>, <h2>, etc.)
    # Example: <h1>Some Text</h1> -> <h1>{% trans "Some Text" %}</h1>
    for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        pattern = rf'<{tag}([^>]*)>([^<{{%]+)</{tag}>'
        def replacer(match):
            attrs = match.group(1)
            text = match.group(2).strip()
            if text and not text.startswith('{%') and not text.startswith('{{'):
                return f'<{tag}{attrs}>{{% trans "{text}" %}}</{tag}>'
            return match.group(0)
        content = re.sub(pattern, replacer, content)
    
    # Pattern 2: Paragraph text
    # Example: <p>Some text</p> -> <p>{% trans "Some text" %}</p>
    pattern = r'<p([^>]*)>([^<{{%][^<]*?)</p>'
    def replacer(match):
        attrs = match.group(1)
        text = match.group(2).strip()
        if text and not text.startswith('{%') and not text.startswith('{{') and len(text) > 2:
            # Escape quotes in text
            text_escaped = text.replace('"', '\\"')
            return f'<p{attrs}>{{% trans "{text_escaped}" %}}</p>'
        return match.group(0)
    content = re.sub(pattern, replacer, content, flags=re.DOTALL)
    
    # Pattern 3: Link text
    # Example: <a href="...">Link Text</a> -> <a href="...">{% trans "Link Text" %}</a>
    pattern = r'(<a[^>]*>)([A-Z][^<{{%]+)(</a>)'
    def replacer(match):
        opening = match.group(1)
        text = match.group(2).strip()
        closing = match.group(3)
        if text and not text.startswith('{%') and not text.startswith('{{'):
            return f'{opening}{{% trans "{text}" %}}{closing}'
        return match.group(0)
    content = re.sub(pattern, replacer, content)
    
    # Pattern 4: Button text
    # Example: <button>Click Me</button> -> <button>{% trans "Click Me" %}</button>
    pattern = r'<button([^>]*)>([^<{{%]+)</button>'
    def replacer(match):
        attrs = match.group(1)
        text = match.group(2).strip()
        if text and not text.startswith('{%') and not text.startswith('{{'):
            return f'<button{attrs}>{{% trans "{text}" %}}</button>'
        return match.group(0)
    content = re.sub(pattern, replacer, content)
    
    # Pattern 5: Placeholder attributes
    # Example: placeholder="Search" -> placeholder="{% trans 'Search' %}"
    pattern = r'placeholder="([^"{{%]+)"'
    def replacer(match):
        text = match.group(1).strip()
        if text and not text.startswith('{%'):
            return f'placeholder="{{% trans \'{text}\' %}}"'
        return match.group(0)
    content = re.sub(pattern, replacer, content)
    
    return content

def process_template(template_path):
    """Process a single template file"""
    print(f"Processing {template_path.name}...")
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply transformations
    new_content = wrap_text_in_trans(content)
    
    # Only write if changed
    if new_content != content:
        with open(template_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  ✓ Updated {template_path.name}")
        return True
    else:
        print(f"  - No changes needed for {template_path.name}")
        return False

def main():
    """Process all templates"""
    templates = list(TEMPLATES_DIR.glob('*.html'))
    updated_count = 0
    
    for template_path in templates:
        if process_template(template_path):
            updated_count += 1
    
    print(f"\nProcessed {len(templates)} templates")
    print(f"Updated {updated_count} templates")
    print("\nNow run: python compile_translations.py")

if __name__ == '__main__':
    main()
