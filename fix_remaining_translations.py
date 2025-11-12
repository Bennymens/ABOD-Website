import re

# Fix Hospitality Page
hosp_file = r'main\templates\main\architecture_hospitality.html'

with open(hosp_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix all untranslated text
content = re.sub(r'>Hospitality/Leisure Architecture Projects</h1>', r'>{% trans "Hospitality/Leisure Architecture Projects" %}</h1>', content)
content = re.sub(r'At ABOD, we design hospitality and leisure spaces that create memorable experiences\. Our approach focuses on atmosphere, comfort, and service flow, crafting environments where guests feel welcomed, relaxed, and inspired\.', r'{% trans "At ABOD, we design hospitality and leisure spaces that create memorable experiences. Our approach focuses on atmosphere, comfort, and service flow, crafting environments where guests feel welcomed, relaxed, and inspired." %}', content)
content = re.sub(r'From boutique hotels and resorts to restaurants, wellness centers, and entertainment venues, we design with the guest journey in mind\. Every detail is considered to enhance the experience and reflect the unique character of each destination\.', r'{% trans "From boutique hotels and resorts to restaurants, wellness centers, and entertainment venues, we design with the guest journey in mind. Every detail is considered to enhance the experience and reflect the unique character of each destination." %}', content)
content = re.sub(r'Our hospitality projects blend local culture, modern design, and sustainable practices to create spaces that are both beautiful and functional, leaving lasting impressions on all who visit\.', r'{% trans "Our hospitality projects blend local culture, modern design, and sustainable practices to create spaces that are both beautiful and functional, leaving lasting impressions on all who visit." %}', content)
content = re.sub(r'(\s+)>Discover more</h3>', r'\1>{% trans "Discover more" %}</h3>', content)
content = re.sub(r'(\s+)>Discover more\s+<span', r'\1>{% trans "Discover more" %}\n              <span', content)
content = re.sub(r'(\s+)>Get in touch with our team</h3>', r'\1>{% trans "Get in touch with our team" %}</h3>', content)
content = re.sub(r'(\s+)>Contact our experts\s+<span', r'\1>{% trans "Contact our experts" %}\n              <span', content)

with open(hosp_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Hospitality page translations completed!")

# Fix Civic Page
civic_file = r'main\templates\main\architecture_civic.html'

with open(civic_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix all untranslated text
content = re.sub(r'>Civic Architecture Projects</h1>', r'>{% trans "Civic Architecture Projects" %}</h1>', content)
content = re.sub(r'At ABOD, we design civic architecture that serves communities and strengthens public life\. Our approach balances functionality with identity, creating spaces that bring people together and stand as landmarks of shared purpose\.', r'{% trans "At ABOD, we design civic architecture that serves communities and strengthens public life. Our approach balances functionality with identity, creating spaces that bring people together and stand as landmarks of shared purpose." %}', content)
content = re.sub(r'From community centers and cultural facilities to government buildings and public institutions, we design with accessibility, sustainability, and longevity in mind\. Every project is shaped by the needs of the community it serves\.', r'{% trans "From community centers and cultural facilities to government buildings and public institutions, we design with accessibility, sustainability, and longevity in mind. Every project is shaped by the needs of the community it serves." %}', content)
content = re.sub(r'Our civic projects reflect collaboration between stakeholders, designers, and the public, ensuring that every building serves its purpose with dignity, beauty, and resilience\.', r'{% trans "Our civic projects reflect collaboration between stakeholders, designers, and the public, ensuring that every building serves its purpose with dignity, beauty, and resilience." %}', content)
content = re.sub(r'(\s+)>Discover more</h3>', r'\1>{% trans "Discover more" %}</h3>', content)
content = re.sub(r'(\s+)>Discover more\s+<span', r'\1>{% trans "Discover more" %}\n              <span', content)
content = re.sub(r'(\s+)>Get in touch with our team</h3>', r'\1>{% trans "Get in touch with our team" %}</h3>', content)
content = re.sub(r'(\s+)>Contact our experts\s+<span', r'\1>{% trans "Contact our experts" %}\n              <span', content)

with open(civic_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Civic page translations completed!")
print("\nAll 4 architecture pages are now fully translated!")
