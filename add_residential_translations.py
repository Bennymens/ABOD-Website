import polib

# Translations for residential architecture page
translations = {
    "Residential and Housing Architecture": {
        "fr": "Architecture Résidentielle et de Logement",
        "de": "Wohn- und Wohnungsarchitektur"
    },
    "At ABOD, we see residential design as the art of creating spaces that reflect how people live, feel, and connect. Every home we design is guided by a balance of form, function, and emotion where architecture enhances daily living and celebrates individuality.": {
        "fr": "Chez ABOD, nous considérons le design résidentiel comme l'art de créer des espaces qui reflètent la façon dont les gens vivent, ressentent et se connectent. Chaque maison que nous concevons est guidée par un équilibre entre forme, fonction et émotion où l'architecture améliore la vie quotidienne et célèbre l'individualité.",
        "de": "Bei ABOD sehen wir Wohndesign als die Kunst, Räume zu schaffen, die widerspiegeln, wie Menschen leben, fühlen und sich verbinden. Jedes Haus, das wir entwerfen, wird von einem Gleichgewicht aus Form, Funktion und Emotion geleitet, bei dem Architektur das tägliche Leben verbessert und Individualität feiert."
    },
    "From private residences and beach houses to modern estates and housing developments, our work combines innovation with a deep respect for context and comfort. We design with purpose considering light, space, and material to create homes that feel natural, inspiring, and enduring.": {
        "fr": "Des résidences privées et maisons de plage aux domaines modernes et développements immobiliers, notre travail combine l'innovation avec un profond respect pour le contexte et le confort. Nous concevons avec intention en tenant compte de la lumière, de l'espace et des matériaux pour créer des maisons qui se sentent naturelles, inspirantes et durables.",
        "de": "Von Privatresidenzen und Strandhäusern bis hin zu modernen Anwesen und Wohnsiedlungen verbindet unsere Arbeit Innovation mit tiefem Respekt für Kontext und Komfort. Wir entwerfen mit Absicht und berücksichtigen Licht, Raum und Material, um Häuser zu schaffen, die sich natürlich, inspirierend und beständig anfühlen."
    },
    "Each project begins with understanding our clients' vision and lifestyle. Through collaboration and creativity, we craft personalized spaces that are beautiful, practical, and built to stand the test of time.": {
        "fr": "Chaque projet commence par la compréhension de la vision et du style de vie de nos clients. Grâce à la collaboration et à la créativité, nous créons des espaces personnalisés qui sont beaux, pratiques et conçus pour résister à l'épreuve du temps.",
        "de": "Jedes Projekt beginnt mit dem Verständnis der Vision und des Lebensstils unserer Kunden. Durch Zusammenarbeit und Kreativität schaffen wir personalisierte Räume, die schön, praktisch und gebaut sind, um die Zeit zu überdauern."
    }
}

# Process French translations
print("Adding French translations...")
po_fr = polib.pofile('locale/fr/LC_MESSAGES/django.po')
for english, trans in translations.items():
    entry = po_fr.find(english)
    if entry:
        entry.msgstr = trans["fr"]
        print(f"Updated FR: {english[:50]}...")
    else:
        entry = polib.POEntry(msgid=english, msgstr=trans["fr"])
        po_fr.append(entry)
        print(f"Added FR: {english[:50]}...")
po_fr.save('locale/fr/LC_MESSAGES/django.po')

# Process German translations
print("\nAdding German translations...")
po_de = polib.pofile('locale/de/LC_MESSAGES/django.po')
for english, trans in translations.items():
    entry = po_de.find(english)
    if entry:
        entry.msgstr = trans["de"]
        print(f"Updated DE: {english[:50]}...")
    else:
        entry = polib.POEntry(msgid=english, msgstr=trans["de"])
        po_de.append(entry)
        print(f"Added DE: {english[:50]}...")
po_de.save('locale/de/LC_MESSAGES/django.po')

print("\nResidential page translations added for both French and German!")

