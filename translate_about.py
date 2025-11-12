#!/usr/bin/env python3
"""
Script to add {% trans %} tags to about.html for i18n support
"""

import re

def wrap_text_with_trans(content):
    """Wrap hardcoded text with {% trans %} tags"""
    
    replacements = [
        # Page title and tagline
        (r'<div class="tagline-below-navbar tagline-left slide-up">About Us</div>',
         r'<div class="tagline-below-navbar tagline-left slide-up">{% trans "About Us" %}</div>'),
        
        # WHO ARE WE section
        (r'<h2 class="who-heading tagline-left slide-up">WHO ARE WE\?</h2>',
         r'<h2 class="who-heading tagline-left slide-up">{% trans "WHO ARE WE?" %}</h2>'),
        
        # Who text paragraph - need to handle the multi-line text
        (r'Abod Group is a premier built environment consultancy headquartered in Accra,\s+Ghana\. <br>We are dedicated to transforming Africa\'s urban landscape through innovative,\s+sustainable, <br>and high-tech design solutions\. Our team of visionary architects,\s+engineers, and sustainability <br>experts leverages cutting-edge technologies like AI,\s+BIM,and digital twinning to deliver iconic, <br>complex projects that redefine excellence\.',
         r'{% trans "Abod Group is a premier built environment consultancy headquartered in Accra, Ghana. We are dedicated to transforming Africa\'s urban landscape through innovative, sustainable, and high-tech design solutions. Our team of visionary architects, engineers, and sustainability experts leverages cutting-edge technologies like AI, BIM, and digital twinning to deliver iconic, complex projects that redefine excellence." %}'),
        
        # CORE VALUES section
        (r'<h2 class="core-heading tagline-left slide-up">CORE VALUES</h2>',
         r'<h2 class="core-heading tagline-left slide-up">{% trans "CORE VALUES" %}</h2>'),
        
        (r'<li>Innovation \(pushing design boundaries\)</li>',
         r'<li>{% trans "Innovation (pushing design boundaries)" %}</li>'),
        (r'<li>Sustainability \(prioritizing environmental responsibility\)</li>',
         r'<li>{% trans "Sustainability (prioritizing environmental responsibility)" %}</li>'),
        (r'<li>Excellence \(delivering superior quality\)</li>',
         r'<li>{% trans "Excellence (delivering superior quality)" %}</li>'),
        (r'<li>Integrity \(maintaining ethical standards\)</li>',
         r'<li>{% trans "Integrity (maintaining ethical standards)" %}</li>'),
        (r'<li>Collaboration \(working closely with clients, communities, and partners\)</li>',
         r'<li>{% trans "Collaboration (working closely with clients, communities, and partners)" %}</li>'),
        
        # WHY ABOD section
        (r'<h2 class="why-heading tagline-left slide-up">WHY ABOD\?</h2>',
         r'<h2 class="why-heading tagline-left slide-up">{% trans "WHY ABOD?" %}</h2>'),
        
        (r'<li>Complex, Iconic Projects: Delivering landmark developments with a "wow factor\."</li>',
         r'<li>{% trans "Complex, Iconic Projects: Delivering landmark developments with a wow factor." %}</li>'),
        (r'<li>Sustainability and Climate Resilience: Committing to net-zero goals and green certifications\.</li>',
         r'<li>{% trans "Sustainability and Climate Resilience: Committing to net-zero goals and green certifications." %}</li>'),
        (r'<li>Advanced Technology: Harnessing AI, BIM, parametric design, and digital twinning for precision and innovation\.</li>',
         r'<li>{% trans "Advanced Technology: Harnessing AI, BIM, parametric design, and digital twinning for precision and innovation." %}</li>'),
        (r'<li>Africa-Centric Solutions: Combining global expertise with local knowledge to address regional challenges\.</li>',
         r'<li>{% trans "Africa-Centric Solutions: Combining global expertise with local knowledge to address regional challenges." %}</li>'),
        (r'<li>Human-Centered Design: Creating inclusive, narrative-driven spaces that inspire\.</li>',
         r'<li>{% trans "Human-Centered Design: Creating inclusive, narrative-driven spaces that inspire." %}</li>'),
        
        # DESIGN PHILOSOPHY section
        (r'<h2 class="design-heading tagline-left slide-up">OUR DESIGN PHILOSPHY</h2>',
         r'<h2 class="design-heading tagline-left slide-up">{% trans "OUR DESIGN PHILOSOPHY" %}</h2>'),
        
        # Design philosophy captions
        (r'Collaborative Engagement: Prioritizing collaboration, client feedback, and constant communication to co-create innovative, meaningful designs that resonate with stakeholders\.',
         r'{% trans "Collaborative Engagement: Prioritizing collaboration, client feedback, and constant communication to co-create innovative, meaningful designs that resonate with stakeholders." %}'),
        
        (r'Narrative-Driven Design: Crafting spaces that tell a story and engage communities, enriched through collaborative input and ongoing client dialogue\.',
         r'{% trans "Narrative-Driven Design: Crafting spaces that tell a story and engage communities, enriched through collaborative input and ongoing client dialogue." %}'),
        
        (r'Sustainable High-Tech Solutions: Integrating green materials, smart systems, and innovative forms, developed with client collaboration and feedback to ensure sustainable outcomes\.',
         r'{% trans "Sustainable High-Tech Solutions: Integrating green materials, smart systems, and innovative forms, developed with client collaboration and feedback to ensure sustainable outcomes." %}'),
        
        (r'Challenging the Status Quo: Embracing a "what can\'t be done" mindset to push boundaries, shaped by constant communication and client insights to drive bold innovation\.',
         r'{% trans "Challenging the Status Quo: Embracing a what can\'t be done mindset to push boundaries, shaped by constant communication and client insights to drive bold innovation." %}'),
        
        (r'User-Centric and Inclusive: Prioritizing functionality, accessibility, and excellence, co-designed with clients through continuous feedback and collaborative processes\.',
         r'{% trans "User-Centric and Inclusive: Prioritizing functionality, accessibility, and excellence, co-designed with clients through continuous feedback and collaborative processes." %}'),
        
        (r'Research-Based and AI-Backed: Grounded in deep research and cutting-edge technology, enhanced by iterative client collaboration and constant communication for impactful solutions\.',
         r'{% trans "Research-Based and AI-Backed: Grounded in deep research and cutting-edge technology, enhanced by iterative client collaboration and constant communication for impactful solutions." %}'),
        
        # OUR CLIENTS section
        (r'<h2 class="clients-heading tagline-left slide-up">OUR CLIENTS</h2>',
         r'<h2 class="clients-heading tagline-left slide-up">{% trans "OUR CLIENTS" %}</h2>'),
        
        # Issues section (already translated in index, but check)
        (r'<h1 class="issues-title">Issues</h1>',
         r'<h1 class="issues-title">{% trans "Issues" %}</h1>'),
        (r'We explore some of the biggest questions facing the built and\s+natural environments\.',
         r'{% trans "We explore some of the biggest questions facing the built and natural environments." %}'),
        (r'View more issues',
         r'{% trans "View more issues" %}'),
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
    file_path = r'c:\Users\PC\OneDrive\Desktop\ABOD\main\templates\main\about.html'
    
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
