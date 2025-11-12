"""
Script to compile .po files to .mo files for Django translations
"""
import polib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOCALE_DIR = os.path.join(BASE_DIR, 'locale')

def compile_messages():
    """Compile all .po files to .mo files"""
    languages = ['fr', 'de']
    
    for lang in languages:
        po_file = os.path.join(LOCALE_DIR, lang, 'LC_MESSAGES', 'django.po')
        mo_file = os.path.join(LOCALE_DIR, lang, 'LC_MESSAGES', 'django.mo')
        
        if os.path.exists(po_file):
            print(f"Compiling {lang} translations...")
            po = polib.pofile(po_file)
            po.save_as_mofile(mo_file)
            print(f"✓ Created {mo_file}")
        else:
            print(f"✗ {po_file} not found")

if __name__ == '__main__':
    compile_messages()
    print("\nTranslation files compiled successfully!")
