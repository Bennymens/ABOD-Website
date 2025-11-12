import polib

# Load the French .po file
po = polib.pofile('locale/fr/LC_MESSAGES/django.po')

# Translations to add for architecture_civic.html
translations = {
    "Civic Architecture Projects": "Projets d'Architecture Civique",
    "At ABOD, we design civic architecture that serves communities and strengthens public life. Our approach balances functionality with identity, creating spaces that bring people together and stand as landmarks of shared purpose.": "Chez ABOD, nous concevons une architecture civique qui sert les communautés et renforce la vie publique. Notre approche équilibre fonctionnalité et identité, créant des espaces qui rassemblent les gens et se dressent comme des repères d'un objectif commun.",
    "From community centers and cultural facilities to government buildings and public institutions, we design with accessibility, sustainability, and longevity in mind. Every project is shaped by the needs of the community it serves.": "Des centres communautaires et installations culturelles aux bâtiments gouvernementaux et institutions publiques, nous concevons en pensant à l'accessibilité, à la durabilité et à la longévité. Chaque projet est façonné par les besoins de la communauté qu'il sert.",
    "Our civic projects reflect collaboration between stakeholders, designers, and the public, ensuring that every building serves its purpose with dignity, beauty, and resilience.": "Nos projets civiques reflètent la collaboration entre les parties prenantes, les concepteurs et le public, garantissant que chaque bâtiment remplit son objectif avec dignité, beauté et résilience.",
}

# Add translations
for english, french in translations.items():
    # Check if entry already exists
    entry = po.find(english)
    if entry:
        entry.msgstr = french
        print(f"Updated: {english[:50]}...")
    else:
        entry = polib.POEntry(
            msgid=english,
            msgstr=french,
        )
        po.append(entry)
        print(f"Added: {english[:50]}...")

# Save the file
po.save('locale/fr/LC_MESSAGES/django.po')
print("\nCivic page translations added to django.po")
