#!/usr/bin/env python3
"""
Script to add {% trans %} tags to remaining untranslated text in contact.html
"""

import re

# Read the file
with open('main/templates/main/contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define replacements for the Careers section
replacements = [
    ('<h3>Careers</h3>', '<h3>{% trans "Careers" %}</h3>'),
    ('<p class="accordion-subtext">Speak to Arup\'s recruitment teams about job opportunities and careers. Before sending a general enquiry, kindly review our application process to see if your question has already been addressed.</p>',
     '<p class="accordion-subtext">{% trans "Speak to Arup\'s recruitment teams about job opportunities and careers. Before sending a general enquiry, kindly review our application process to see if your question has already been addressed." %}</p>'),
    ('<label>Experience level</label>', '<label>{% trans "Experience level" %}</label>'),
    ('<option value="internship">Internship</option>', '<option value="internship">{% trans "Internship" %}</option>'),
    ('<option value="entry">Entry Level</option>', '<option value="entry">{% trans "Entry Level" %}</option>'),
    ('<option value="mid">Mid Level</option>', '<option value="mid">{% trans "Mid Level" %}</option>'),
    ('<option value="senior">Senior Level</option>', '<option value="senior">{% trans "Senior Level" %}</option>'),
    ('<option value="executive">Executive</option>', '<option value="executive">{% trans "Executive" %}</option>'),
    ('<option value="graduate">Graduate</option>', '<option value="graduate">{% trans "Graduate" %}</option>'),
    ('<p class="privacy-note">Arup will only process your data in accordance with its <a href="#">privacy policy</a>.</p>',
     '<p class="privacy-note">{% trans "Arup will only process your data in accordance with its" %} <a href="#">{% trans "privacy policy" %}</a>.</p>'),
]

# Replacements for Other section
replacements.extend([
    ('<h3>Other</h3>', '<h3>{% trans "Other" %}</h3>'),
    ('<p class="accordion-subtext">Speak to us about anything else.</p>',
     '<p class="accordion-subtext">{% trans "Speak to us about anything else." %}</p>'),
])

# Nearest office section
replacements.extend([
    ('<div class="nearest-office-heading">Your nearest office</div>',
     '<div class="nearest-office-heading">{% trans "Your nearest office" %}</div>'),
    ('Contact office', '{% trans "Contact office" %}'),
])

# Cookie consent banner
replacements.extend([
    ('<p>We use cookies to enhance your browsing experience, serve personalized content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies.</p>',
     '<p>{% trans "We use cookies to enhance your browsing experience, serve personalized content, and analyze our traffic. By clicking \\"Accept All\\", you consent to our use of cookies." %}</p>'),
    ('>Accept All</', '>{% trans "Accept All" %}</'),
    ('>Reject All</', '>{% trans "Reject All" %}</'),
    ('>Customize</', '>{% trans "Customize" %}</'),
    ('<h3>Cookie Preferences</h3>', '<h3>{% trans "Cookie Preferences" %}</h3>'),
    ('<h4>Essential Cookies</h4>', '<h4>{% trans "Essential Cookies" %}</h4>'),
    ('<p>These cookies are necessary for the website to function and cannot be switched off in our systems.</p>',
     '<p>{% trans "These cookies are necessary for the website to function and cannot be switched off in our systems." %}</p>'),
    ('<h4>Analytics Cookies</h4>', '<h4>{% trans "Analytics Cookies" %}</h4>'),
    ('<p>These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site.</p>',
     '<p>{% trans "These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site." %}</p>'),
    ('<h4>Marketing Cookies</h4>', '<h4>{% trans "Marketing Cookies" %}</h4>'),
    ('<p>These cookies may be set through our site by our advertising partners to build a profile of your interests.</p>',
     '<p>{% trans "These cookies may be set through our site by our advertising partners to build a profile of your interests." %}</p>'),
    ('>Save Preferences</', '>{% trans "Save Preferences" %}</'),
])

# Apply all replacements
for old, new in replacements:
    content = content.replace(old, new)

# Write back
with open('main/templates/main/contact.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Successfully added {% trans %} tags to contact.html")
