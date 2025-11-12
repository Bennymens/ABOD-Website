#!/usr/bin/env python3
"""
Script to add missing {% trans %} tags to Careers and Other forms in contact.html
"""

import re

def wrap_text_with_trans(content):
    """Wrap hardcoded text with {% trans %} tags"""
    
    # Careers section - subtitle
    content = re.sub(
        r'<p class="accordion-subtext">Speak to Arup\'s recruitment teams about job opportunities and careers\. Before sending a general enquiry, kindly review our application process to see if your question has already been addressed\.</p>',
        r'<p class="accordion-subtext">{% trans "Speak to Arup\'s recruitment teams about job opportunities and careers. Before sending a general enquiry, kindly review our application process to see if your question has already been addressed." %}</p>',
        content
    )
    
    # Careers form labels
    labels_careers = [
        (r'<label>First name</label>', r'<label>{% trans "First name" %}</label>'),
        (r'<label>Last name</label>', r'<label>{% trans "Last name" %}</label>'),
        (r'<label>Email address</label>', r'<label>{% trans "Email address" %}</label>'),
        (r'<label>Phone number</label>', r'<label>{% trans "Phone number" %}</label>'),
        (r'<label>Company name</label>', r'<label>{% trans "Company name" %}</label>'),
        (r'<label>Job title</label>', r'<label>{% trans "Job title" %}</label>'),
        (r'<label>Country/Location</label>', r'<label>{% trans "Country/Location" %}</label>'),
        (r'<label>City/Town</label>', r'<label>{% trans "City/Town" %}</label>'),
        (r'<label>How did you hear about us\?</label>', r'<label>{% trans "How did you hear about us?" %}</label>'),
        (r'<label>What would you like to discuss\?</label>', r'<label>{% trans "What would you like to discuss?" %}</label>'),
        (r'<label>Area of business</label>', r'<label>{% trans "Area of business" %}</label>'),
        (r'<label>Select your service of interest \(if known\)</label>', r'<label>{% trans "Select your service of interest (if known)" %}</label>'),
    ]
    
    for old, new in labels_careers:
        content = re.sub(old, new, content)
    
    # Career/Other form options - "Select", "Select..."
    content = re.sub(r'<option value="">Select</option>', r'<option value="">{% trans "Select" %}</option>', content)
    content = re.sub(r'<option value="">Select\.\.\.</option>', r'<option value="">{% trans "Select..." %}</option>', content)
    
    # Countries (need to translate in Careers section)
    countries = [
        'United Kingdom', 'United States', 'Canada', 'Australia', 'Ireland',
        'France', 'Germany', 'Netherlands', 'Spain', 'Italy', 'Sweden', 
        'Norway', 'Denmark', 'Finland', 'Belgium', 'Switzerland', 'Austria', 
        'Poland', 'Portugal', 'Greece', 'Turkey', 'Russia', 'China', 'India',
        'Japan', 'South Korea', 'Singapore', 'Hong Kong SAR', 
        'United Arab Emirates', 'Saudi Arabia', 'South Africa', 'Kenya', 
        'Nigeria', 'Egypt', 'Brazil', 'Mexico', 'Argentina', 'Chile', 
        'Colombia', 'New Zealand'
    ]
    
    for country in countries:
        escaped_country = country.replace(' ', r'\s*')
        content = re.sub(
            f'<option value="[^"]*">{country}</option>',
            f'<option value="{{{{ match.group(0).split(\'"\')[1] }}}}">{{% trans "{country}" %}}</option>',
            content
        )
        # Simpler approach
        content = re.sub(
            f'>{country}</option>',
            f'>{{% trans "{country}" %}}</option>',
            content
        )
    
    # "Other" option
    content = re.sub(r'<option value="other">Other</option>', r'<option value="other">{% trans "Other" %}</option>', content)
    
    # "How did you hear about us" options
    hear_options = [
        'Social Media', 'Website', 'Referral', 'Advertisement', 'Job Board',
        'LinkedIn', 'Indeed', 'Glassdoor', 'University/Career Fair', 'Networking Event'
    ]
    
    for option in hear_options:
        content = re.sub(
            f'>{option}</option>',
            f'>{{% trans "{option}" %}}</option>',
            content
        )
    
    # Area of business options
    business_areas = [
        'Buildings', 'Infrastructure', 'Transport', 'Energy', 'Water',
        'Environment', 'Cities &amp; Urban Design', 'Digital &amp; Technology',
        'Advisory', 'Health', 'Education', 'Defence', 'Mining', 'Maritime',
        'Property &amp; Real Estate'
    ]
    
    for area in business_areas:
        # Handle &amp; properly
        display_area = area.replace('&amp;', '&')
        content = re.sub(
            f'>{area}</option>',
            f'>{{% trans "{display_area}" %}}</option>',
            content
        )
    
    # Service of interest options (already have trans tags from previous script, but check)
    
    # Submit button in Careers section
    content = re.sub(
        r'<button type="submit" class="btn-submit">Submit</button>',
        r'<button type="submit" class="btn-submit">{% trans "Submit" %}</button>',
        content
    )
    
    return content

def main():
    file_path = r'c:\Users\PC\OneDrive\Desktop\ABOD\main\templates\main\contact.html'
    
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
