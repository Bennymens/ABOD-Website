#!/usr/bin/env python3
"""
Script to add tagline translations to French and German .po files
"""

import polib

def add_translations():
    # Translations mapping: English -> (French, German)
    translations = {
        "We are designing structures for life": (
            "Nous concevons des structures pour la vie",
            "Wir entwerfen Strukturen fürs Leben"
        ),
        "We are engineering the change we want to see": (
            "Nous créons le changement que nous voulons voir",
            "Wir gestalten den Wandel, den wir sehen wollen"
        ),
    }
    
    # Update French translations
    print("Updating French translations...")
    po_fr = polib.pofile(r'locale/fr/LC_MESSAGES/django.po')
    
    for english, (french, german) in translations.items():
        entry = po_fr.find(english)
        if entry:
            entry.msgstr = french
            print(f"  Updated: {english}")
        else:
            entry = polib.POEntry(
                msgid=english,
                msgstr=french,
                occurrences=[('main/templates/main/index.html', '')]
            )
            po_fr.append(entry)
            print(f"  Added: {english}")
    
    po_fr.save()
    print("✓ French translations updated")
    
    # Update German translations
    print("\nUpdating German translations...")
    po_de = polib.pofile(r'locale/de/LC_MESSAGES/django.po')
    
    for english, (french, german) in translations.items():
        entry = po_de.find(english)
        if entry:
            entry.msgstr = german
            print(f"  Updated: {english}")
        else:
            entry = polib.POEntry(
                msgid=english,
                msgstr=german,
                occurrences=[('main/templates/main/index.html', '')]
            )
            po_de.append(entry)
            print(f"  Added: {english}")
    
    po_de.save()
    print("✓ German translations updated")

if __name__ == '__main__':
    add_translations()
    print("\n✓ All tagline translations added successfully!")
