import os
import django
import polib

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ABOD.settings')
django.setup()

# Dictionary of English to French and German translations for commercial page
translations = {
    "Commercial Architecture Projects": {
        "fr": "Projets d'architecture commerciale",
        "de": "Gewerbearchitektur-Projekte"
    },
    "At ABOD, we design commercial spaces that drive business success and enhance user experience. Our buildings are tailored to reflect brand identity, support operational efficiency, and create environments that inspire and engage.": {
        "fr": "Chez ABOD, nous concevons des espaces commerciaux qui favorisent le succès commercial et améliorent l'expérience utilisateur. Nos bâtiments sont conçus pour refléter l'identité de marque, soutenir l'efficacité opérationnelle et créer des environnements qui inspirent et engagent.",
        "de": "Bei ABOD entwerfen wir Gewerberäume, die den Geschäftserfolg fördern und das Benutzererlebnis verbessern. Unsere Gebäude sind darauf zugeschnitten, die Markenidentität widerzuspiegeln, die betriebliche Effizienz zu unterstützen und Umgebungen zu schaffen, die inspirieren und begeistern."
    },
    "From office buildings and retail centers to mixed-use developments and corporate headquarters, we balance aesthetics with functionality. Every project is designed with sustainability, flexibility, and long-term value in mind.": {
        "fr": "Des immeubles de bureaux et centres commerciaux aux développements à usage mixte et sièges sociaux, nous équilibrons esthétique et fonctionnalité. Chaque projet est conçu en tenant compte de la durabilité, de la flexibilité et de la valeur à long terme.",
        "de": "Von Bürogebäuden und Einzelhandelszentren bis hin zu gemischt genutzten Entwicklungen und Unternehmenszentralen balancieren wir Ästhetik mit Funktionalität. Jedes Projekt wird mit Blick auf Nachhaltigkeit, Flexibilität und langfristigen Wert entworfen."
    },
    "We work closely with clients to understand their vision and goals, delivering commercial architecture that is innovative, practical, and built to adapt to the future of work and commerce.": {
        "fr": "Nous travaillons en étroite collaboration avec les clients pour comprendre leur vision et leurs objectifs, en livrant une architecture commerciale innovante, pratique et conçue pour s'adapter à l'avenir du travail et du commerce.",
        "de": "Wir arbeiten eng mit Kunden zusammen, um ihre Vision und Ziele zu verstehen, und liefern Gewerbearchitektur, die innovativ, praktisch und darauf ausgelegt ist, sich an die Zukunft von Arbeit und Handel anzupassen."
    },
    "Our architecture practice has been at the heart of Abods work across the built environment.": {
        "fr": "Notre pratique d'architecture a été au cœur du travail d'Abod dans tout l'environnement bâti.",
        "de": "Unsere Architekturpraxis stand im Mittelpunkt der Arbeit von Abod in der gebauten Umwelt."
    }
}

# Function to add translations to a .po file
def add_translations_to_po(po_file_path, lang_code):
    print(f"\nProcessing {lang_code.upper()} translations...")
    
    # Load or create the .po file
    if os.path.exists(po_file_path):
        po = polib.pofile(po_file_path)
        print(f"Loaded existing file: {po_file_path}")
    else:
        po = polib.POFile()
        print(f"Created new file: {po_file_path}")
    
    # Add each translation
    for english_text, translations_dict in translations.items():
        translation_text = translations_dict[lang_code]
        
        # Check if entry already exists
        existing_entry = po.find(english_text)
        
        if existing_entry:
            # Update existing entry
            if existing_entry.msgstr != translation_text:
                existing_entry.msgstr = translation_text
                print(f"Updated: {english_text[:50]}...")
            else:
                print(f"Skipped (already correct): {english_text[:50]}...")
        else:
            # Add new entry
            entry = polib.POEntry(
                msgid=english_text,
                msgstr=translation_text
            )
            po.append(entry)
            print(f"Added: {english_text[:50]}...")
    
    # Save the .po file
    po.save(po_file_path)
    print(f"Saved {po_file_path}")

# Add French translations
fr_po_path = os.path.join('locale', 'fr', 'LC_MESSAGES', 'django.po')
add_translations_to_po(fr_po_path, 'fr')

# Add German translations
de_po_path = os.path.join('locale', 'de', 'LC_MESSAGES', 'django.po')
add_translations_to_po(de_po_path, 'de')

print("\n✅ All commercial translations have been added successfully!")
print("Next step: Run 'python compile_translations.py' to compile the translations.")
