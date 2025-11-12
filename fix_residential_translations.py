import re

file_path = r'main\templates\main\architecture_residential.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix heading - wrap the entire text
content = re.sub(
    r'>Residential and Housing Architecture</h1>',
    r'>{% trans "Residential and Housing Architecture" %}</h1>',
    content
)

# Fix first paragraph - combine all parts
content = re.sub(
    r'At ABOD, we see residential design as the art of creating spaces\s+that reflect how people live, feel, and connect\. <br />\s+{% trans "Every home we design is guided by a balance of form, function, and emotion where architecture enhances" %} <br />daily living and\s+celebrates individuality\.',
    r'{% trans "At ABOD, we see residential design as the art of creating spaces that reflect how people live, feel, and connect." %} <br />\n            {% trans "Every home we design is guided by a balance of form, function, and emotion where architecture enhances daily living and celebrates individuality." %}',
    content
)

# Fix "Discover more" heading
content = re.sub(
    r'>Discover more</h3>',
    r'>{% trans "Discover more" %}</h3>',
    content
)

# Fix "Discover more" button
content = re.sub(
    r'>Discover more\s+<span',
    r'>{% trans "Discover more" %}\n              <span',
    content
)

# Fix "Get in touch with our team" heading
content = re.sub(
    r'>Get in touch with our team</h3>',
    r'>{% trans "Get in touch with our team" %}</h3>',
    content
)

# Fix "Contact our experts" button
content = re.sub(
    r'>Contact our experts\s+<span',
    r'>{% trans "Contact our experts" %}\n              <span',
    content
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Residential page translations fixed!")
