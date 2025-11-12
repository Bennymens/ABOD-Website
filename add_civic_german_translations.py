import polib

# Load the German .po file
po = polib.pofile('locale/de/LC_MESSAGES/django.po')

# German translations for civic architecture page
translations = {
    "Civic Architecture Projects": "Projekte für öffentliche Architektur",
    "At ABOD, we design civic architecture that serves communities and strengthens public life. Our approach balances functionality with identity, creating spaces that bring people together and stand as landmarks of shared purpose.": "Bei ABOD entwerfen wir öffentliche Architektur, die Gemeinden dient und das öffentliche Leben stärkt. Unser Ansatz gleicht Funktionalität mit Identität aus und schafft Räume, die Menschen zusammenbringen und als Wahrzeichen gemeinsamer Ziele dienen.",
    "From community centers and cultural facilities to government buildings and public institutions, we design with accessibility, sustainability, and longevity in mind. Every project is shaped by the needs of the community it serves.": "Von Gemeindezentren und Kultureinrichtungen bis hin zu Regierungsgebäuden und öffentlichen Institutionen entwerfen wir mit Blick auf Zugänglichkeit, Nachhaltigkeit und Langlebigkeit. Jedes Projekt wird durch die Bedürfnisse der Gemeinschaft geprägt, der es dient.",
    "Our civic projects reflect collaboration between stakeholders, designers, and the public, ensuring that every building serves its purpose with dignity, beauty, and resilience.": "Unsere öffentlichen Projekte spiegeln die Zusammenarbeit zwischen Interessengruppen, Designern und der Öffentlichkeit wider und stellen sicher, dass jedes Gebäude seinen Zweck mit Würde, Schönheit und Widerstandsfähigkeit erfüllt.",
    "Discover more": "Mehr entdecken",
    "Our architecture practice has been at the heart of Abods work across the built environment.": "Unsere Architekturpraxis stand im Mittelpunkt der Arbeit von Abod in der gebauten Umwelt.",
    "Get in touch with our team": "Kontaktieren Sie unser Team",
    "Contact our experts": "Kontaktieren Sie unsere Experten",
}

# Add translations
for english, german in translations.items():
    # Check if entry already exists
    entry = po.find(english)
    if entry:
        entry.msgstr = german
        print(f"Updated: {english[:50]}...")
    else:
        entry = polib.POEntry(
            msgid=english,
            msgstr=german,
        )
        po.append(entry)
        print(f"Added: {english[:50]}...")

# Save the file
po.save('locale/de/LC_MESSAGES/django.po')
print("\nGerman translations for civic page added to django.po")
