#!/usr/bin/env python3
"""
Script to add {% trans %} tags to index.html for i18n support
"""

import re

def wrap_text_with_trans(content):
    """Wrap hardcoded text with {% trans %} tags"""
    
    replacements = [
        # Search placeholder
        (r'placeholder="search ABOD"', r'placeholder="{% trans \'search ABOD\' %}"'),
        
        # Issues section - Second card (Issues title already has trans tag)
        (r'<a href="#" class="card-link">Issues</a>',
         r'<a href="{% url \'insights\' %}" class="card-link">{% trans "Issues" %}</a>'),
        
        # Card text for Issues card
        (r'<p class="card-link-main">How do you solve tight spaces with smart design and precise engineering</p>',
         r'<p class="card-link-main">{% trans "How do you solve tight spaces with smart design and precise engineering" %}</p>'),
        (r'<p class="card-link-sub">we believe complex challenges can be catalysts for better design</p>',
         r'<p class="card-link-sub">{% trans "we believe complex challenges can be catalysts for better design" %}</p>'),
        
        # Projects card
        (r'<a href="{% url \'projects\' %}" class="card-link">Projects</a>',
         r'<a href="{% url \'projects\' %}" class="card-link">{% trans "Projects" %}</a>'),
        (r'<p class="card-link-main">The exchange apartments</p>',
         r'<p class="card-link-main">{% trans "The exchange apartments" %}</p>'),
        (r'<p class="card-link-sub">Modern living spaces designed for contemporary urban lifestyles</p>',
         r'<p class="card-link-sub">{% trans "Modern living spaces designed for contemporary urban lifestyles" %}</p>'),
        
        # News card
        (r'<a href="{% url \'news\' %}" class="card-link">News</a>',
         r'<a href="{% url \'news\' %}" class="card-link">{% trans "News" %}</a>'),
        (r'<p class="card-link-main">ABOD founder along with others win IFC Edge Design Competition</p>',
         r'<p class="card-link-main">{% trans "ABOD founder along with others win IFC Edge Design Competition" %}</p>'),
        
        # Our Work section
        (r'<h2 class="our-work-header">Our Work</h2>',
         r'<h2 class="our-work-header">{% trans "Our Work" %}</h2>'),
        (r'<a href="/projects/" class="see-projects-button">See Projects →</a>',
         r'<a href="/projects/" class="see-projects-button">{% trans "See Projects" %} →</a>'),
        (r'Showcasing our latest projects and achievements in engineering and\s+sustainability\.',
         r'{% trans "Showcasing our latest projects and achievements in engineering and sustainability." %}'),
        
        # Work showcase texts
        (r'<h3>Urban Development</h3>',
         r'<h3>{% trans "Urban Development" %}</h3>'),
        (r'Creating sustainable urban spaces that blend innovation with\s+community needs\.',
         r'{% trans "Creating sustainable urban spaces that blend innovation with community needs." %}'),
        
        (r'<h3>3d Modeling and Visualisation</h3>',
         r'<h3>{% trans "3d Modeling and Visualisation" %}</h3>'),
        (r'Advancing engineering solutions for complex challenges in modern\s+construction\.',
         r'{% trans "Advancing engineering solutions for complex challenges in modern construction." %}'),
        
        (r'<h3>Sustainable Architecture</h3>',
         r'<h3>{% trans "Sustainable Architecture" %}</h3>'),
        (r'Designing buildings that harmonize with the environment and future\s+generations\.',
         r'{% trans "Designing buildings that harmonize with the environment and future generations." %}'),
        
        (r'<h3>Modern Construction</h3>',
         r'<h3>{% trans "Modern Construction" %}</h3>'),
        (r'Implementing cutting-edge techniques for efficient and resilient\s+structures\.',
         r'{% trans "Implementing cutting-edge techniques for efficient and resilient structures." %}'),
        
        # Issues section header
        (r'<h1 class="issues-title">Issues</h1>',
         r'<h1 class="issues-title">{% trans "Issues" %}</h1>'),
        (r'We explore some of the biggest questions facing the built and\s+natural environments\.',
         r'{% trans "We explore some of the biggest questions facing the built and natural environments." %}'),
        (r'View more issues',
         r'{% trans "View more issues" %}'),
        
        # Issue cards
        (r'<span class="card-label">Issue</span>',
         r'<span class="card-label">{% trans "Issue" %}</span>'),
        (r'How do we create climate-resilient, energy-efficient buildings\?',
         r'{% trans "How do we create climate-resilient, energy-efficient buildings?" %}'),
        (r'How do we tackle high-end, technically challenging developments\?',
         r'{% trans "How do we tackle high-end, technically challenging developments?" %}'),
        (r'How do we Prioritize inclusive, user-focused solutions\?',
         r'{% trans "How do we Prioritize inclusive, user-focused solutions?" %}'),
    ]
    
    for old, new in replacements:
        content = re.sub(old, new, content, flags=re.MULTILINE | re.DOTALL)
    
    return content

def main():
    file_path = r'c:\Users\PC\OneDrive\Desktop\ABOD\main\templates\main\index.html'
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply translations
    content = wrap_text_with_trans(content)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated {file_path}")

if __name__ == '__main__':
    main()
