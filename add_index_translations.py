#!/usr/bin/env python3
"""
Script to add index.html translations to French and German .po files
"""

import polib

def add_translations():
    # Translations mapping: English -> (French, German)
    translations = {
        "search ABOD": ("rechercher ABOD", "ABOD durchsuchen"),
        "Issues": ("Questions", "Themen"),
        "How do you solve tight spaces with smart design and precise engineering": (
            "Comment résoudre les espaces restreints avec une conception intelligente et une ingénierie précise",
            "Wie löst man enge Räume mit intelligentem Design und präziser Technik"
        ),
        "we believe complex challenges can be catalysts for better design": (
            "nous croyons que les défis complexes peuvent être des catalyseurs pour une meilleure conception",
            "wir glauben, dass komplexe Herausforderungen Katalysatoren für besseres Design sein können"
        ),
        "Projects": ("Projets", "Projekte"),
        "The exchange apartments": ("Les appartements exchange", "Die Exchange Apartments"),
        "Modern living spaces designed for contemporary urban lifestyles": (
            "Espaces de vie modernes conçus pour les modes de vie urbains contemporains",
            "Moderne Wohnräume für zeitgenössische urbane Lebensstile"
        ),
        "News": ("Actualités", "Neuigkeiten"),
        "ABOD founder along with others win IFC Edge Design Competition": (
            "Le fondateur d'ABOD et d'autres remportent le concours de design IFC Edge",
            "ABOD-Gründer und andere gewinnen IFC Edge Design-Wettbewerb"
        ),
        "Our Work": ("Notre Travail", "Unsere Arbeit"),
        "See Projects": ("Voir les Projets", "Projekte Ansehen"),
        "Showcasing our latest projects and achievements in engineering and sustainability.": (
            "Présentation de nos derniers projets et réalisations en ingénierie et durabilité.",
            "Präsentation unserer neuesten Projekte und Erfolge in Technik und Nachhaltigkeit."
        ),
        "Urban Development": ("Développement Urbain", "Stadtentwicklung"),
        "Creating sustainable urban spaces that blend innovation with community needs.": (
            "Créer des espaces urbains durables qui allient innovation et besoins de la communauté.",
            "Schaffung nachhaltiger urbaner Räume, die Innovation mit Gemeinschaftsbedürfnissen verbinden."
        ),
        "3d Modeling and Visualisation": ("Modélisation 3D et Visualisation", "3D-Modellierung und Visualisierung"),
        "Advancing engineering solutions for complex challenges in modern construction.": (
            "Faire progresser les solutions d'ingénierie pour les défis complexes de la construction moderne.",
            "Fortschrittliche Ingenieurtechniklösungen für komplexe Herausforderungen im modernen Bauwesen."
        ),
        "Sustainable Architecture": ("Architecture Durable", "Nachhaltige Architektur"),
        "Designing buildings that harmonize with the environment and future generations.": (
            "Concevoir des bâtiments en harmonie avec l'environnement et les générations futures.",
            "Gebäude entwerfen, die mit der Umwelt und zukünftigen Generationen harmonieren."
        ),
        "Modern Construction": ("Construction Moderne", "Modernes Bauen"),
        "Implementing cutting-edge techniques for efficient and resilient structures.": (
            "Mise en œuvre de techniques de pointe pour des structures efficaces et résilientes.",
            "Umsetzung modernster Techniken für effiziente und widerstandsfähige Strukturen."
        ),
        "We explore some of the biggest questions facing the built and natural environments.": (
            "Nous explorons certaines des plus grandes questions auxquelles sont confrontés les environnements bâtis et naturels.",
            "Wir untersuchen einige der größten Fragen, mit denen die gebaute und natürliche Umwelt konfrontiert ist."
        ),
        "View more issues": ("Voir plus de questions", "Mehr Themen anzeigen"),
        "Issue": ("Question", "Thema"),
        "How do we create climate-resilient, energy-efficient buildings?": (
            "Comment créer des bâtiments résilients au climat et économes en énergie ?",
            "Wie schaffen wir klimaresistente, energieeffiziente Gebäude?"
        ),
        "How do we tackle high-end, technically challenging developments?": (
            "Comment relever les défis des développements haut de gamme et techniquement exigeants ?",
            "Wie gehen wir mit hochwertigen, technisch anspruchsvollen Entwicklungen um?"
        ),
        "How do we Prioritize inclusive, user-focused solutions?": (
            "Comment prioriser des solutions inclusives et centrées sur l'utilisateur ?",
            "Wie priorisieren wir inklusive, benutzerzentrierte Lösungen?"
        ),
    }
    
    # Update French translations
    print("Updating French translations...")
    po_fr = polib.pofile(r'locale/fr/LC_MESSAGES/django.po')
    
    for english, (french, german) in translations.items():
        entry = po_fr.find(english)
        if entry:
            entry.msgstr = french
            print(f"  Updated: {english[:50]}...")
        else:
            entry = polib.POEntry(
                msgid=english,
                msgstr=french,
                occurrences=[('main/templates/main/index.html', '')]
            )
            po_fr.append(entry)
            print(f"  Added: {english[:50]}...")
    
    po_fr.save()
    print("✓ French translations updated")
    
    # Update German translations
    print("\nUpdating German translations...")
    po_de = polib.pofile(r'locale/de/LC_MESSAGES/django.po')
    
    for english, (french, german) in translations.items():
        entry = po_de.find(english)
        if entry:
            entry.msgstr = german
            print(f"  Updated: {english[:50]}...")
        else:
            entry = polib.POEntry(
                msgid=english,
                msgstr=german,
                occurrences=[('main/templates/main/index.html', '')]
            )
            po_de.append(entry)
            print(f"  Added: {english[:50]}...")
    
    po_de.save()
    print("✓ German translations updated")

if __name__ == '__main__':
    add_translations()
    print("\n✓ All translations added successfully!")
