import os
import django
import polib

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ABOD.settings')
django.setup()

# Dictionary of English to French and German translations for hospitality page
translations = {
    "Hospitality/Leisure Architecture Projects": {
        "fr": "Projets d'architecture hôtelière et de loisirs",
        "de": "Architekturprojekte für Gastgewerbe und Freizeit"
    },
    "At ABOD, we design hospitality and leisure spaces that create memorable experiences. Our approach focuses on atmosphere, comfort, and service flow, crafting environments where guests feel welcomed, relaxed, and inspired.": {
        "fr": "Chez ABOD, nous concevons des espaces d'accueil et de loisirs qui créent des expériences mémorables. Notre approche se concentre sur l'atmosphère, le confort et le flux de service, créant des environnements où les clients se sentent accueillis, détendus et inspirés.",
        "de": "Bei ABOD entwerfen wir Gastgewerbe- und Freizeiträume, die unvergessliche Erlebnisse schaffen. Unser Ansatz konzentriert sich auf Atmosphäre, Komfort und Serviceablauf und schafft Umgebungen, in denen sich Gäste willkommen, entspannt und inspiriert fühlen."
    },
    "From boutique hotels and resorts to restaurants, wellness centers, and entertainment venues, we design with the guest journey in mind. Every detail is considered to enhance the experience and reflect the unique character of each destination.": {
        "fr": "Des hôtels boutique et complexes hôteliers aux restaurants, centres de bien-être et lieux de divertissement, nous concevons en gardant à l'esprit le parcours client. Chaque détail est considéré pour améliorer l'expérience et refléter le caractère unique de chaque destination.",
        "de": "Von Boutique-Hotels und Resorts bis hin zu Restaurants, Wellnesszentren und Unterhaltungsstätten entwerfen wir mit Blick auf die Gästereise. Jedes Detail wird berücksichtigt, um das Erlebnis zu verbessern und den einzigartigen Charakter jedes Reiseziels widerzuspiegeln."
    },
    "Our hospitality projects blend local culture, modern design, and sustainable practices to create spaces that are both beautiful and functional, leaving lasting impressions on all who visit.": {
        "fr": "Nos projets hôteliers mélangent culture locale, design moderne et pratiques durables pour créer des espaces à la fois beaux et fonctionnels, laissant des impressions durables à tous ceux qui les visitent.",
        "de": "Unsere Hospitality-Projekte verbinden lokale Kultur, modernes Design und nachhaltige Praktiken, um Räume zu schaffen, die sowohl schön als auch funktional sind und bei allen Besuchern bleibende Eindrücke hinterlassen."
    },
    "Discover more": {
        "fr": "Découvrir plus",
        "de": "Mehr erfahren"
    },
    "Our architecture practice combines innovation with sustainability to create spaces that inspire and endure.": {
        "fr": "Notre pratique d'architecture combine innovation et durabilité pour créer des espaces qui inspirent et durent.",
        "de": "Unsere Architekturpraxis verbindet Innovation mit Nachhaltigkeit, um Räume zu schaffen, die inspirieren und Bestand haben."
    },
    "Get in touch with our team": {
        "fr": "Contactez notre équipe",
        "de": "Kontaktieren Sie unser Team"
    },
    "Contact our experts": {
        "fr": "Contactez nos experts",
        "de": "Kontaktieren Sie unsere Experten"
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

print("\n✅ All hospitality translations have been added successfully!")
print("Next step: Run 'python compile_translations.py' to compile the translations.")
