#!/usr/bin/env python
"""
Script to add issue detail page translations to French and German .po files
"""

def add_translations():
    # Translations dictionary
    translations = {
        "Issues": {
            "fr": "Problématiques",
            "de": "Themen"
        },
        "How do you solve tight spaces with smart design and precise engineering": {
            "fr": "Comment résoudre les espaces restreints avec un design intelligent et une ingénierie précise",
            "de": "Wie löst man enge Räume mit intelligentem Design und präziser Technik"
        },
        "In our Issues section, we discuss the big questions facing the built and natural environments.": {
            "fr": "Dans notre section Problématiques, nous discutons des grandes questions concernant l'environnement bâti et naturel.",
            "de": "In unserem Themenbereich diskutieren wir die großen Fragen der gebauten und natürlichen Umwelt."
        },
        "Share": {
            "fr": "Partager",
            "de": "Teilen"
        },
        "LinkedIn": {
            "fr": "LinkedIn",
            "de": "LinkedIn"
        },
        "Facebook": {
            "fr": "Facebook",
            "de": "Facebook"
        },
        "Instagram": {
            "fr": "Instagram",
            "de": "Instagram"
        },
        "WhatsApp": {
            "fr": "WhatsApp",
            "de": "WhatsApp"
        },
        "Twitter": {
            "fr": "Twitter",
            "de": "Twitter"
        },
        "Copy Link": {
            "fr": "Copier le lien",
            "de": "Link kopieren"
        },
        "For a private residence, our industrial designers were presented with the challenge of creating a staircase within a tightly confined space. The spatial limitations required precise planning and a deep understanding of form, proportion, and functionality to ensure the staircase complemented the home's interior layout. Every inch of the available area had to be optimized without compromising comfort or safety.": {
            "fr": "Pour une résidence privée, nos designers industriels ont été confrontés au défi de créer un escalier dans un espace très restreint. Les limitations spatiales ont nécessité une planification précise et une compréhension approfondie de la forme, de la proportion et de la fonctionnalité pour garantir que l'escalier complète l'aménagement intérieur de la maison. Chaque centimètre de la surface disponible devait être optimisé sans compromettre le confort ou la sécurité.",
            "de": "Für ein privates Wohnhaus standen unsere Industriedesigner vor der Herausforderung, eine Treppe in einem sehr beengten Raum zu schaffen. Die räumlichen Einschränkungen erforderten präzise Planung und ein tiefes Verständnis von Form, Proportion und Funktionalität, um sicherzustellen, dass die Treppe das Innenraumlayout des Hauses ergänzt. Jeder Zentimeter des verfügbaren Bereichs musste optimiert werden, ohne Komfort oder Sicherheit zu beeinträchtigen."
        },
        "Midway through the project, the client introduced a new requirement the inclusion of a landing before the stairwell. This addition had not been anticipated in the original architectural design, meaning our team had to revisit and rethink the entire staircase configuration. The challenge demanded a balance between meeting the client's functional needs and preserving the intended flow of the interior space.": {
            "fr": "À mi-chemin du projet, le client a introduit une nouvelle exigence : l'inclusion d'un palier avant la cage d'escalier. Cet ajout n'avait pas été anticipé dans la conception architecturale originale, ce qui signifie que notre équipe a dû revoir et repenser toute la configuration de l'escalier. Le défi exigeait un équilibre entre la satisfaction des besoins fonctionnels du client et la préservation du flux prévu de l'espace intérieur.",
            "de": "In der Mitte des Projekts führte der Kunde eine neue Anforderung ein: die Einbeziehung eines Podests vor dem Treppenhaus. Diese Ergänzung war im ursprünglichen architektonischen Entwurf nicht vorgesehen, was bedeutete, dass unser Team die gesamte Treppenkonfiguration überdenken musste. Die Herausforderung erforderte ein Gleichgewicht zwischen der Erfüllung der funktionalen Bedürfnisse des Kunden und der Beibehaltung des beabsichtigten Flusses des Innenraums."
        },
        "Through innovative problem-solving and collaboration between designers, architects, and builders, we developed a creative solution that seamlessly integrated the landing without disrupting the home's design language. The final result was a refined staircase that combined practicality with aesthetic sophistication, turning a spatial constraint into a defining architectural feature.": {
            "fr": "Grâce à une résolution de problèmes innovante et à la collaboration entre designers, architectes et constructeurs, nous avons développé une solution créative qui a intégré de manière transparente le palier sans perturber le langage de conception de la maison. Le résultat final était un escalier raffiné qui combinait praticité et sophistication esthétique, transformant une contrainte spatiale en une caractéristique architecturale déterminante.",
            "de": "Durch innovative Problemlösung und Zusammenarbeit zwischen Designern, Architekten und Bauherren entwickelten wir eine kreative Lösung, die das Podest nahtlos integrierte, ohne die Designsprache des Hauses zu stören. Das Endergebnis war eine raffinierte Treppe, die Praktikabilität mit ästhetischer Raffinesse verband und eine räumliche Einschränkung in ein prägendes architektonisches Merkmal verwandelte."
        },
        "How we tackle this issue:": {
            "fr": "Comment nous abordons ce problème :",
            "de": "Wie wir dieses Problem angehen:"
        },
        "Collaborating closely, we engineered a winder staircase with a dog-leg configuration, breaking it into three parts: a starting section, a folded winder segment to maximize space, and a long landing for safe passage of two users, followed by a final dog-leg. Designed for steel fabricators, we detailed the structure in three modular parts for seamless assembly and installation.": {
            "fr": "En collaborant étroitement, nous avons conçu un escalier à quart tournant avec une configuration en équerre, le divisant en trois parties : une section de départ, un segment à quart tournant plié pour maximiser l'espace, et un long palier pour le passage sûr de deux utilisateurs, suivi d'un dernier quart tournant. Conçu pour les fabricants d'acier, nous avons détaillé la structure en trois parties modulaires pour un assemblage et une installation sans couture.",
            "de": "In enger Zusammenarbeit entwickelten wir eine Wendeltreppe mit einer Hundebein-Konfiguration, die in drei Teile unterteilt wurde: einen Startabschnitt, ein gefaltetes Wendelsegment zur Maximierung des Raums und ein langes Podest für den sicheren Durchgang von zwei Benutzern, gefolgt von einem letzten Hundebein. Für Stahlhersteller entwickelt, detaillierten wir die Struktur in drei modularen Teilen für eine nahtlose Montage und Installation."
        },
        "Our solution prioritized functionality, safety, and fabrication efficiency, delivering a bespoke staircase that transformed a constrained space into a practical and elegant feature.": {
            "fr": "Notre solution a donné la priorité à la fonctionnalité, à la sécurité et à l'efficacité de fabrication, offrant un escalier sur mesure qui a transformé un espace restreint en une caractéristique pratique et élégante.",
            "de": "Unsere Lösung priorisierte Funktionalität, Sicherheit und Fertigungseffizienz und lieferte eine maßgeschneiderte Treppe, die einen eingeschränkten Raum in ein praktisches und elegantes Merkmal verwandelte."
        },
        "Explore more services": {
            "fr": "Explorer plus de services",
            "de": "Weitere Dienstleistungen erkunden"
        },
        "Discover our comprehensive range of architectural solutions and design services.": {
            "fr": "Découvrez notre gamme complète de solutions architecturales et de services de conception.",
            "de": "Entdecken Sie unser umfassendes Angebot an architektonischen Lösungen und Designdienstleistungen."
        },
        "Explore more": {
            "fr": "Explorer plus",
            "de": "Mehr erkunden"
        }
    }

    # French translations
    print("Adding French translations...")
    fr_po_path = "locale/fr/LC_MESSAGES/django.po"
    
    with open(fr_po_path, 'r', encoding='utf-8') as f:
        fr_content = f.read()
    
    for english, trans in translations.items():
        entry = f'\nmsgid "{english}"\nmsgstr "{trans["fr"]}"\n'
        if f'msgid "{english}"' not in fr_content:
            fr_content += entry
            print(f"Added FR: {english[:50]}...")
    
    with open(fr_po_path, 'w', encoding='utf-8') as f:
        f.write(fr_content)
    
    # German translations
    print("\nAdding German translations...")
    de_po_path = "locale/de/LC_MESSAGES/django.po"
    
    with open(de_po_path, 'r', encoding='utf-8') as f:
        de_content = f.read()
    
    for english, trans in translations.items():
        entry = f'\nmsgid "{english}"\nmsgstr "{trans["de"]}"\n'
        if f'msgid "{english}"' not in de_content:
            de_content += entry
            print(f"Added DE: {english[:50]}...")
    
    with open(de_po_path, 'w', encoding='utf-8') as f:
        f.write(de_content)
    
    print("\n✓ Translations added successfully!")
    print("\nNext steps:")
    print("1. Run: python manage.py compilemessages")
    print("2. Test the translations on the issue detail page")

if __name__ == "__main__":
    add_translations()
