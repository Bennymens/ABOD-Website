#!/usr/bin/env python3
"""
Script to add project translations to .po files
"""

# French translations
fr_translations = """
# Projects Data
msgid "Aseda Garden Estate"
msgstr "Aseda Garden Estate"

msgid "Luxury home featuring innovative architecture. A bespoke residence with modern amenities and green spaces."
msgstr "Maison de luxe dotée d'une architecture innovante. Une résidence sur mesure avec des équipements modernes et des espaces verts."

msgid "Tema, Ghana"
msgstr "Tema, Ghana"

msgid "Beach House"
msgstr "Maison de Plage"

msgid "Seaside retreat with panoramic ocean views. A coastal property designed for relaxation and harmony with nature."
msgstr "Refuge en bord de mer avec vue panoramique sur l'océan. Une propriété côtière conçue pour la détente et l'harmonie avec la nature."

msgid "First love center"
msgstr "Centre First Love"

msgid "Developing multiple components, from Internal to the new tower block."
msgstr "Développement de multiples composants, de l'intérieur à la nouvelle tour."

msgid "Gardenia"
msgstr "Gardenia"

msgid "Commercial complex with modern retail spaces. A vibrant hub for shopping and entertainment in the city center."
msgstr "Complexe commercial avec des espaces commerciaux modernes. Un hub dynamique pour le shopping et le divertissement au centre-ville."

msgid "Rustic retreat nestled in the hills. An eco-lodge offering tranquility and adventure experiences."
msgstr "Retraite rustique nichée dans les collines. Un éco-lodge offrant tranquillité et expériences d'aventure."

msgid "private residence tema"
msgstr "résidence privée tema"

msgid "High-rise residential towers with city views. Luxury apartments featuring smart home technology and amenities."
msgstr "Tours résidentielles avec vue sur la ville. Appartements de luxe dotés de technologie domotique et d'équipements."

msgid "The Exchange apartments"
msgstr "Appartements The Exchange"

msgid "Exclusive villas along the riverbank. Private estates with lush gardens and waterfront access."
msgstr "Villas exclusives le long de la berge. Domaines privés avec jardins luxuriants et accès au bord de l'eau."

msgid "Theatre"
msgstr "Théâtre"

msgid "Sustainable community living spaces. A green development promoting environmental consciousness."
msgstr "Espaces de vie communautaire durables. Un développement vert promouvant la conscience environnementale."

msgid "Kumasi, Ghana"
msgstr "Kumasi, Ghana"

msgid "TSC Commercial, Tema"
msgstr "TSC Commercial, Tema"

msgid "Luxury accommodation with cultural significance. A boutique hotel preserving local heritage and traditions."
msgstr "Hébergement de luxe avec importance culturelle. Un hôtel-boutique préservant le patrimoine et les traditions locales."

msgid "Cape Coast, Ghana"
msgstr "Cape Coast, Ghana"

msgid "roof top"
msgstr "toit-terrasse"

msgid "Tech and startup incubation center. A modern facility fostering entrepreneurship and innovation."
msgstr "Centre d'incubation technologique et de startups. Une installation moderne favorisant l'entrepreneuriat et l'innovation."

msgid "Private Residence Ashongman"
msgstr "Résidence Privée Ashongman"

msgid "Spa and wellness retreat destination. A serene oasis for relaxation and rejuvenation."
msgstr "Destination de retraite spa et bien-être. Une oasis sereine pour la détente et le rajeunissement."

msgid "Takoradi, Ghana"
msgstr "Takoradi, Ghana"
"""

# German translations
de_translations = """
# Projects Data
msgid "Aseda Garden Estate"
msgstr "Aseda Garden Estate"

msgid "Luxury home featuring innovative architecture. A bespoke residence with modern amenities and green spaces."
msgstr "Luxushaus mit innovativer Architektur. Eine maßgeschneiderte Residenz mit modernen Annehmlichkeiten und Grünflächen."

msgid "Tema, Ghana"
msgstr "Tema, Ghana"

msgid "Beach House"
msgstr "Strandhaus"

msgid "Seaside retreat with panoramic ocean views. A coastal property designed for relaxation and harmony with nature."
msgstr "Küstenrückzugsort mit Panoramablick auf den Ozean. Eine Küstenimmobilie für Entspannung und Harmonie mit der Natur."

msgid "First love center"
msgstr "First Love Zentrum"

msgid "Developing multiple components, from Internal to the new tower block."
msgstr "Entwicklung mehrerer Komponenten, vom Innenbereich bis zum neuen Turmgebäude."

msgid "Gardenia"
msgstr "Gardenia"

msgid "Commercial complex with modern retail spaces. A vibrant hub for shopping and entertainment in the city center."
msgstr "Gewerblicher Komplex mit modernen Einzelhandelsflächen. Ein lebendiger Knotenpunkt für Shopping und Unterhaltung im Stadtzentrum."

msgid "Rustic retreat nestled in the hills. An eco-lodge offering tranquility and adventure experiences."
msgstr "Rustikaler Rückzugsort in den Hügeln. Eine Öko-Lodge, die Ruhe und Abenteuererlebnisse bietet."

msgid "private residence tema"
msgstr "Privatresidenz Tema"

msgid "High-rise residential towers with city views. Luxury apartments featuring smart home technology and amenities."
msgstr "Hochhaus-Wohntürme mit Stadtblick. Luxusapartments mit Smart-Home-Technologie und Annehmlichkeiten."

msgid "The Exchange apartments"
msgstr "Die Exchange Apartments"

msgid "Exclusive villas along the riverbank. Private estates with lush gardens and waterfront access."
msgstr "Exklusive Villen am Flussufer. Private Anwesen mit üppigen Gärten und Zugang zum Wasser."

msgid "Theatre"
msgstr "Theater"

msgid "Sustainable community living spaces. A green development promoting environmental consciousness."
msgstr "Nachhaltige gemeinschaftliche Wohnräume. Eine grüne Entwicklung zur Förderung des Umweltbewusstseins."

msgid "Kumasi, Ghana"
msgstr "Kumasi, Ghana"

msgid "TSC Commercial, Tema"
msgstr "TSC Commercial, Tema"

msgid "Luxury accommodation with cultural significance. A boutique hotel preserving local heritage and traditions."
msgstr "Luxusunterkunft mit kultureller Bedeutung. Ein Boutique-Hotel, das lokales Erbe und Traditionen bewahrt."

msgid "Cape Coast, Ghana"
msgstr "Cape Coast, Ghana"

msgid "roof top"
msgstr "Dachterrasse"

msgid "Tech and startup incubation center. A modern facility fostering entrepreneurship and innovation."
msgstr "Technologie- und Startup-Inkubationszentrum. Eine moderne Einrichtung zur Förderung von Unternehmertum und Innovation."

msgid "Private Residence Ashongman"
msgstr "Privatresidenz Ashongman"

msgid "Spa and wellness retreat destination. A serene oasis for relaxation and rejuvenation."
msgstr "Spa- und Wellness-Rückzugsziel. Eine ruhige Oase für Entspannung und Erholung."

msgid "Takoradi, Ghana"
msgstr "Takoradi, Ghana"
"""

# Read and append to French .po file
with open('locale/fr/LC_MESSAGES/django.po', 'r', encoding='utf-8') as f:
    fr_content = f.read()

if 'msgid "Aseda Garden Estate"' not in fr_content:
    with open('locale/fr/LC_MESSAGES/django.po', 'a', encoding='utf-8') as f:
        f.write(fr_translations)
    print("✓ Added French project translations")
else:
    print("French project translations already exist")

# Read and append to German .po file
with open('locale/de/LC_MESSAGES/django.po', 'r', encoding='utf-8') as f:
    de_content = f.read()

if 'msgid "Aseda Garden Estate"' not in de_content:
    with open('locale/de/LC_MESSAGES/django.po', 'a', encoding='utf-8') as f:
        f.write(de_translations)
    print("✓ Added German project translations")
else:
    print("German project translations already exist")

print("\nDone! Run compile_translations.py to compile the translations.")
