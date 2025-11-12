import re

# Architecture Residential
residential_file = r'main\templates\main\architecture_residential.html'

with open(residential_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace "Back to Architecture and Design"
content = re.sub(
    r'← Back to Architecture and Design',
    r'{% trans "← Back to Architecture and Design" %}',
    content
)

# Replace heading
content = re.sub(
    r'>Residential and Housing Architecture</h1>',
    r'>{% trans "Residential and Housing Architecture" %}</h1>',
    content
)

# Replace first paragraph
content = re.sub(
    r'At ABOD, we see residential design as the art of creating spaces that\s+reflect how people live, feel, and connect\.',
    r'{% trans "At ABOD, we see residential design as the art of creating spaces that reflect how people live, feel, and connect." %}',
    content
)

content = re.sub(
    r'Every home we design is guided by a balance of form, function, and\s+emotion where architecture enhances',
    r'{% trans "Every home we design is guided by a balance of form, function, and emotion where architecture enhances" %}',
    content
)

content = re.sub(
    r'daily living and celebrates\s+individuality\.',
    r'{% trans "daily living and celebrates individuality." %}',
    content
)

# Replace second paragraph
content = re.sub(
    r'From private residences and beach houses to modern estates and\s+housing developments, our work combines',
    r'{% trans "From private residences and beach houses to modern estates and housing developments, our work combines" %}',
    content
)

content = re.sub(
    r'inovation with a deep respect for context and comfort\. We design\s+with purpose considering light, space,',
    r'{% trans "innovation with a deep respect for context and comfort. We design with purpose considering light, space," %}',
    content
)

content = re.sub(
    r'and material to create\s+homes that feel natural, inspiring, and enduring\.',
    r'{% trans "and material to create homes that feel natural, inspiring, and enduring." %}',
    content
)

# Replace third paragraph
content = re.sub(
    r'Each project begins with understanding our clients\' vision and\s+lifestyle\. Through collaboration and creativity,',
    r'{% trans "Each project begins with understanding our clients\' vision and lifestyle. Through collaboration and creativity," %}',
    content
)

content = re.sub(
    r'we craft personalized spaces that are beautiful, practical, and\s+built to stand the test of time\.',
    r'{% trans "we craft personalized spaces that are beautiful, practical, and built to stand the test of time." %}',
    content
)

# Replace "Discover more"
content = re.sub(
    r'>Discover more</h3>',
    r'>{% trans "Discover more" %}</h3>',
    content
)

content = re.sub(
    r'Our architecture practice has been at the heart of Abods work\s+across the built environment\.',
    r'{% trans "Our architecture practice has been at the heart of Abods work across the built environment." %}',
    content
)

content = re.sub(
    r'>Discover more\s+<span',
    r'>{% trans "Discover more" %}\n              <span',
    content
)

# Replace "Get in touch with our team"
content = re.sub(
    r'>Get in touch with our team</h3>',
    r'>{% trans "Get in touch with our team" %}</h3>',
    content
)

content = re.sub(
    r'>Contact our experts\s+<span',
    r'>{% trans "Contact our experts" %}\n              <span',
    content
)

with open(residential_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Residential page translations added!")

# Architecture Commercial
commercial_file = r'main\templates\main\architecture_commercial.html'

with open(commercial_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace "Back to Architecture and Design"
content = re.sub(
    r'← Back to Architecture and Design',
    r'{% trans "← Back to Architecture and Design" %}',
    content
)

# Replace heading
content = re.sub(
    r'>Commercial Architecture Projects</h1>',
    r'>{% trans "Commercial Architecture Projects" %}</h1>',
    content
)

# Replace paragraphs
content = re.sub(
    r'At ABOD, we design commercial spaces that drive business success and enhance user experience\. Our buildings are tailored to reflect brand identity, support operational efficiency, and create environments that inspire and engage\.',
    r'{% trans "At ABOD, we design commercial spaces that drive business success and enhance user experience. Our buildings are tailored to reflect brand identity, support operational efficiency, and create environments that inspire and engage." %}',
    content
)

content = re.sub(
    r'From office buildings and retail centers to mixed-use developments and corporate headquarters, we balance aesthetics with functionality\. Every project is designed with sustainability, flexibility, and long-term value in mind\.',
    r'{% trans "From office buildings and retail centers to mixed-use developments and corporate headquarters, we balance aesthetics with functionality. Every project is designed with sustainability, flexibility, and long-term value in mind." %}',
    content
)

content = re.sub(
    r'We work closely with clients to understand their vision and goals, delivering commercial architecture that is innovative, practical, and built to adapt to the future of work and commerce\.',
    r'{% trans "We work closely with clients to understand their vision and goals, delivering commercial architecture that is innovative, practical, and built to adapt to the future of work and commerce." %}',
    content
)

# Replace "Discover more"
content = re.sub(
    r'>Discover more</h3>',
    r'>{% trans "Discover more" %}</h3>',
    content
)

content = re.sub(
    r'Our architecture practice has been at the heart of Abods work\s+across the built environment\.',
    r'{% trans "Our architecture practice has been at the heart of Abods work across the built environment." %}',
    content
)

content = re.sub(
    r'>Discover more\s+<span',
    r'>{% trans "Discover more" %}\n              <span',
    content
)

# Replace "Get in touch with our team"
content = re.sub(
    r'>Get in touch with our team</h3>',
    r'>{% trans "Get in touch with our team" %}</h3>',
    content
)

content = re.sub(
    r'>Contact our experts\s+<span',
    r'>{% trans "Contact our experts" %}\n              <span',
    content
)

with open(commercial_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Commercial page translations added!")

# Architecture Hospitality
hospitality_file = r'main\templates\main\architecture_hospitality.html'

with open(hospitality_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace "Back to Architecture and Design"
content = re.sub(
    r'← Back to Architecture and Design',
    r'{% trans "← Back to Architecture and Design" %}',
    content
)

# Replace heading
content = re.sub(
    r'>Hospitality/Leisure Architecture Projects</h1>',
    r'>{% trans "Hospitality/Leisure Architecture Projects" %}</h1>',
    content
)

# Replace paragraphs
content = re.sub(
    r'At ABOD, we design hospitality and leisure spaces that create memorable experiences\. Our approach focuses on atmosphere, comfort, and service flow, crafting environments where guests feel welcomed, relaxed, and inspired\.',
    r'{% trans "At ABOD, we design hospitality and leisure spaces that create memorable experiences. Our approach focuses on atmosphere, comfort, and service flow, crafting environments where guests feel welcomed, relaxed, and inspired." %}',
    content
)

content = re.sub(
    r'From boutique hotels and resorts to restaurants, wellness centers, and entertainment venues, we design with the guest journey in mind\. Every detail is considered to enhance the experience and reflect the unique character of each destination\.',
    r'{% trans "From boutique hotels and resorts to restaurants, wellness centers, and entertainment venues, we design with the guest journey in mind. Every detail is considered to enhance the experience and reflect the unique character of each destination." %}',
    content
)

content = re.sub(
    r'Our hospitality projects blend local culture, modern design, and sustainable practices to create spaces that are both beautiful and functional, leaving lasting impressions on all who visit\.',
    r'{% trans "Our hospitality projects blend local culture, modern design, and sustainable practices to create spaces that are both beautiful and functional, leaving lasting impressions on all who visit." %}',
    content
)

# Replace "Discover more"
content = re.sub(
    r'>Discover more</h3>',
    r'>{% trans "Discover more" %}</h3>',
    content
)

content = re.sub(
    r'Our architecture practice has been at the heart of Abods work\s+across the built environment\.',
    r'{% trans "Our architecture practice has been at the heart of Abods work across the built environment." %}',
    content
)

content = re.sub(
    r'>Discover more\s+<span',
    r'>{% trans "Discover more" %}\n              <span',
    content
)

# Replace "Get in touch with our team"
content = re.sub(
    r'>Get in touch with our team</h3>',
    r'>{% trans "Get in touch with our team" %}</h3>',
    content
)

content = re.sub(
    r'>Contact our experts\s+<span',
    r'>{% trans "Contact our experts" %}\n              <span',
    content
)

with open(hospitality_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Hospitality page translations added!")

# Architecture Civic
civic_file = r'main\templates\main\architecture_civic.html'

with open(civic_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace "Back to Architecture and Design"
content = re.sub(
    r'← Back to Architecture and Design',
    r'{% trans "← Back to Architecture and Design" %}',
    content
)

# Replace heading
content = re.sub(
    r'>Civic Architecture Projects</h1>',
    r'>{% trans "Civic Architecture Projects" %}</h1>',
    content
)

# Replace paragraphs
content = re.sub(
    r'At ABOD, we design civic architecture that serves communities and strengthens public life\. Our approach balances functionality with identity, creating spaces that bring people together and stand as landmarks of shared purpose\.',
    r'{% trans "At ABOD, we design civic architecture that serves communities and strengthens public life. Our approach balances functionality with identity, creating spaces that bring people together and stand as landmarks of shared purpose." %}',
    content
)

content = re.sub(
    r'From community centers and cultural facilities to government buildings and public institutions, we design with accessibility, sustainability, and longevity in mind\. Every project is shaped by the needs of the community it serves\.',
    r'{% trans "From community centers and cultural facilities to government buildings and public institutions, we design with accessibility, sustainability, and longevity in mind. Every project is shaped by the needs of the community it serves." %}',
    content
)

content = re.sub(
    r'Our civic projects reflect collaboration between stakeholders, designers, and the public, ensuring that every building serves its purpose with dignity, beauty, and resilience\.',
    r'{% trans "Our civic projects reflect collaboration between stakeholders, designers, and the public, ensuring that every building serves its purpose with dignity, beauty, and resilience." %}',
    content
)

# Replace "Discover more"
content = re.sub(
    r'>Discover more</h3>',
    r'>{% trans "Discover more" %}</h3>',
    content
)

content = re.sub(
    r'Our architecture practice has been at the heart of Abods work\s+across the built environment\.',
    r'{% trans "Our architecture practice has been at the heart of Abods work across the built environment." %}',
    content
)

content = re.sub(
    r'>Discover more\s+<span',
    r'>{% trans "Discover more" %}\n              <span',
    content
)

# Replace "Get in touch with our team"
content = re.sub(
    r'>Get in touch with our team</h3>',
    r'>{% trans "Get in touch with our team" %}</h3>',
    content
)

content = re.sub(
    r'>Contact our experts\s+<span',
    r'>{% trans "Contact our experts" %}\n              <span',
    content
)

with open(civic_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Civic page translations added!")
print("\nAll architecture pages have been translated!")
