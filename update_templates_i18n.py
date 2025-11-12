"""
Script to add i18n support to all HTML templates
"""
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'main', 'templates', 'main')

# Files to update (excluding ones we've already done)
templates_to_update = [
    'about.html',
    'careers.html',
    'contact.html',
    'insights.html',
    'markets.html',
    'news.html',
    'projects.html',
    'services.html',
    'search_results.html',
    'architecture_residential.html',
    'architecture_commercial.html',
    'architecture_hospitality.html',
    'architecture_civic.html',
]

def add_i18n_load(content):
    """Add {% load i18n %} if not present"""
    if '{% load i18n %}' in content:
        return content
    
    # Add after {% load static %}
    content = content.replace(
        '{% load static %}',
        '{% load static %}\n{% load i18n %}'
    )
    return content

def update_navigation_links(content):
    """Update navigation menu items with translation tags"""
    replacements = [
        (r'>Markets</a>', r'>{% trans "Markets" %}</a>'),
        (r'>Services</a>', r'>{% trans "Services" %}</a>'),
        (r'>Projects</a>', r'>{% trans "Projects" %}</a>'),
        (r'>Insights</a>', r'>{% trans "Insights" %}</a>'),
        (r'>About</a>', r'>{% trans "About" %}</a>'),
        (r'>Careers</a>', r'>{% trans "Careers" %}</a>'),
        (r'>News</a>', r'>{% trans "News" %}</a>'),
        (r'>Contact</a>', r'>{% trans "Contact" %}</a>'),
    ]
    
    for old, new in replacements:
        # Only replace in navigation context (avoid replacing in other places)
        if old in content and new not in content:
            # Count occurrences
            count = content.count(old)
            # Replace all occurrences
            content = content.replace(old, new)
            print(f"    Replaced {count} occurrences of {old}")
    
    return content

def update_footer(content):
    """Update footer with translation tags"""
    replacements = [
        (r'<h4>Explore</h4>', r'<h4>{% trans "Explore" %}</h4>'),
        (r'<h4>Company</h4>', r'<h4>{% trans "Company" %}</h4>'),
        (
            'Designing sustainable places and systems. We work across markets to\n            make long-term, people-centred change.',
            '{% trans "Designing sustainable places and systems. We work across markets to make long-term, people-centred change." %}'
        ),
        (
            'Designing sustainable places and systems. We work across markets to make long-term, people-centred change.',
            '{% trans "Designing sustainable places and systems. We work across markets to make long-term, people-centred change." %}'
        ),
    ]
    
    for old, new in replacements:
        if old in content and new not in content:
            content = content.replace(old, new)
            print(f"    Updated footer section")
    
    return content

def update_language_switcher(content):
    """Update language dropdown to use POST forms"""
    # Desktop language menu
    old_desktop = '''          <ul class="lang-menu" id="lang-menu">
            <li><a href="?lang=en">English</a></li>
            <li><a href="?lang=fr">French</a></li>
            <li><a href="?lang=de">German</a></li>
          </ul>'''
    
    new_desktop = '''          <ul class="lang-menu" id="lang-menu">
            <li>
              <form action="{% url 'set_language' %}" method="post" style="margin: 0;">
                {% csrf_token %}
                <input name="next" type="hidden" value="{{ request.get_full_path }}" />
                <input name="language" type="hidden" value="en" />
                <button type="submit" style="background: none; border: none; cursor: pointer; padding: 8px 16px; width: 100%; text-align: left; font-family: inherit; font-size: inherit; color: inherit;">English</button>
              </form>
            </li>
            <li>
              <form action="{% url 'set_language' %}" method="post" style="margin: 0;">
                {% csrf_token %}
                <input name="next" type="hidden" value="{{ request.get_full_path }}" />
                <input name="language" type="hidden" value="fr" />
                <button type="submit" style="background: none; border: none; cursor: pointer; padding: 8px 16px; width: 100%; text-align: left; font-family: inherit; font-size: inherit; color: inherit;">Français</button>
              </form>
            </li>
            <li>
              <form action="{% url 'set_language' %}" method="post" style="margin: 0;">
                {% csrf_token %}
                <input name="next" type="hidden" value="{{ request.get_full_path }}" />
                <input name="language" type="hidden" value="de" />
                <button type="submit" style="background: none; border: none; cursor: pointer; padding: 8px 16px; width: 100%; text-align: left; font-family: inherit; font-size: inherit; color: inherit;">Deutsch</button>
              </form>
            </li>
          </ul>'''
    
    if old_desktop in content:
        content = content.replace(old_desktop, new_desktop)
        print("    Updated desktop language switcher")
    
    # Mobile language menu pattern 1
    old_mobile1 = '''            <li><a href="{% url 'set_language' %}?language=en&next={{ request.get_full_path }}">English</a></li>
            <li><a href="{% url 'set_language' %}?language=fr&next={{ request.get_full_path }}">French</a></li>
            <li><a href="{% url 'set_language' %}?language=de&next={{ request.get_full_path }}">German</a></li>'''
    
    new_mobile1 = '''            <li>
              <form action="{% url 'set_language' %}" method="post" style="margin: 0;">
                {% csrf_token %}
                <input name="next" type="hidden" value="{{ request.get_full_path }}" />
                <input name="language" type="hidden" value="en" />
                <button type="submit" style="background: none; border: none; cursor: pointer; padding: 8px 16px; width: 100%; text-align: left; font-family: inherit; font-size: inherit; color: inherit;">English</button>
              </form>
            </li>
            <li>
              <form action="{% url 'set_language' %}" method="post" style="margin: 0;">
                {% csrf_token %}
                <input name="next" type="hidden" value="{{ request.get_full_path }}" />
                <input name="language" type="hidden" value="fr" />
                <button type="submit" style="background: none; border: none; cursor: pointer; padding: 8px 16px; width: 100%; text-align: left; font-family: inherit; font-size: inherit; color: inherit;">Français</button>
              </form>
            </li>
            <li>
              <form action="{% url 'set_language' %}" method="post" style="margin: 0;">
                {% csrf_token %}
                <input name="next" type="hidden" value="{{ request.get_full_path }}" />
                <input name="language" type="hidden" value="de" />
                <button type="submit" style="background: none; border: none; cursor: pointer; padding: 8px 16px; width: 100%; text-align: left; font-family: inherit; font-size: inherit; color: inherit;">Deutsch</button>
              </form>
            </li>'''
    
    if old_mobile1 in content:
        content = content.replace(old_mobile1, new_mobile1)
        print("    Updated mobile language switcher")
    
    return content

def update_search_placeholder(content):
    """Update search placeholder with translation"""
    old = 'placeholder="Search..."'
    new = 'placeholder="{% trans \'Search\' %}..."'
    if old in content and new not in content:
        content = content.replace(old, new)
        print("    Updated search placeholder")
    
    old_button = '>Search</button>'
    new_button = '>{% trans "Search" %}</button>'
    if old_button in content and new_button not in content:
        content = content.replace(old_button, new_button)
        print("    Updated search button")
    
    return content

def update_template(filepath):
    """Update a single template file"""
    print(f"\nUpdating {os.path.basename(filepath)}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Apply updates
    content = add_i18n_load(content)
    content = update_navigation_links(content)
    content = update_footer(content)
    content = update_language_switcher(content)
    content = update_search_placeholder(content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Updated {os.path.basename(filepath)}")
    else:
        print(f"  - No changes needed for {os.path.basename(filepath)}")

def main():
    print("=" * 60)
    print("Adding i18n support to all HTML templates")
    print("=" * 60)
    
    for template_name in templates_to_update:
        filepath = os.path.join(TEMPLATES_DIR, template_name)
        if os.path.exists(filepath):
            update_template(filepath)
        else:
            print(f"\n✗ File not found: {template_name}")
    
    print("\n" + "=" * 60)
    print("All templates updated!")
    print("=" * 60)

if __name__ == '__main__':
    main()
