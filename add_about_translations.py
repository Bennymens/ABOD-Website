#!/usr/bin/env python3
"""
Script to add about.html translations to French and German .po files
"""

import polib

def add_translations():
    # Translations mapping: English -> (French, German)
    translations = {
        "About Us": ("À Propos", "Über Uns"),
        "WHO ARE WE?": ("QUI SOMMES-NOUS ?", "WER SIND WIR?"),
        "Abod Group is a premier built environment consultancy headquartered in Accra, Ghana. We are dedicated to transforming Africa's urban landscape through innovative, sustainable, and high-tech design solutions. Our team of visionary architects, engineers, and sustainability experts leverages cutting-edge technologies like AI, BIM, and digital twinning to deliver iconic, complex projects that redefine excellence.": (
            "Abod Group est un cabinet de conseil de premier plan dans l'environnement bâti, basé à Accra, au Ghana. Nous nous consacrons à transformer le paysage urbain africain grâce à des solutions de conception innovantes, durables et high-tech. Notre équipe d'architectes visionnaires, d'ingénieurs et d'experts en durabilité exploite des technologies de pointe comme l'IA, le BIM et le jumeau numérique pour réaliser des projets emblématiques et complexes qui redéfinissent l'excellence.",
            "Abod Group ist ein führendes Beratungsunternehmen für die gebaute Umwelt mit Hauptsitz in Accra, Ghana. Wir widmen uns der Transformation der afrikanischen Stadtlandschaft durch innovative, nachhaltige und hochtechnologische Designlösungen. Unser Team aus visionären Architekten, Ingenieuren und Nachhaltigkeitsexperten nutzt modernste Technologien wie KI, BIM und Digital Twinning, um ikonische, komplexe Projekte zu realisieren, die Exzellenz neu definieren."
        ),
        "CORE VALUES": ("VALEURS FONDAMENTALES", "KERNWERTE"),
        "Innovation (pushing design boundaries)": (
            "Innovation (repousser les limites de la conception)",
            "Innovation (Designgrenzen verschieben)"
        ),
        "Sustainability (prioritizing environmental responsibility)": (
            "Durabilité (prioriser la responsabilité environnementale)",
            "Nachhaltigkeit (Umweltverantwortung priorisieren)"
        ),
        "Excellence (delivering superior quality)": (
            "Excellence (offrir une qualité supérieure)",
            "Exzellenz (überlegene Qualität liefern)"
        ),
        "Integrity (maintaining ethical standards)": (
            "Intégrité (maintenir des normes éthiques)",
            "Integrität (ethische Standards wahren)"
        ),
        "Collaboration (working closely with clients, communities, and partners)": (
            "Collaboration (travailler étroitement avec les clients, les communautés et les partenaires)",
            "Zusammenarbeit (eng mit Kunden, Gemeinden und Partnern arbeiten)"
        ),
        "WHY ABOD?": ("POURQUOI ABOD ?", "WARUM ABOD?"),
        "Complex, Iconic Projects: Delivering landmark developments with a wow factor.": (
            "Projets complexes et emblématiques : réaliser des développements phares avec un effet wow.",
            "Komplexe, ikonische Projekte: Wegweisende Entwicklungen mit Wow-Faktor liefern."
        ),
        "Sustainability and Climate Resilience: Committing to net-zero goals and green certifications.": (
            "Durabilité et résilience climatique : s'engager pour des objectifs zéro émission nette et des certifications vertes.",
            "Nachhaltigkeit und Klimaresilienz: Engagement für Netto-Null-Ziele und grüne Zertifizierungen."
        ),
        "Advanced Technology: Harnessing AI, BIM, parametric design, and digital twinning for precision and innovation.": (
            "Technologie avancée : exploiter l'IA, le BIM, la conception paramétrique et le jumeau numérique pour la précision et l'innovation.",
            "Fortschrittliche Technologie: KI, BIM, parametrisches Design und Digital Twinning für Präzision und Innovation nutzen."
        ),
        "Africa-Centric Solutions: Combining global expertise with local knowledge to address regional challenges.": (
            "Solutions centrées sur l'Afrique : combiner l'expertise mondiale avec les connaissances locales pour relever les défis régionaux.",
            "Afrika-zentrierte Lösungen: Globale Expertise mit lokalem Wissen kombinieren, um regionale Herausforderungen anzugehen."
        ),
        "Human-Centered Design: Creating inclusive, narrative-driven spaces that inspire.": (
            "Conception centrée sur l'humain : créer des espaces inclusifs et narratifs qui inspirent.",
            "Menschenzentriertes Design: Inklusive, narrative Räume schaffen, die inspirieren."
        ),
        "OUR DESIGN PHILOSOPHY": ("NOTRE PHILOSOPHIE DE CONCEPTION", "UNSERE DESIGNPHILOSOPHIE"),
        "Collaborative Engagement: Prioritizing collaboration, client feedback, and constant communication to co-create innovative, meaningful designs that resonate with stakeholders.": (
            "Engagement collaboratif : prioriser la collaboration, les retours clients et la communication constante pour co-créer des conceptions innovantes et significatives qui résonnent avec les parties prenantes.",
            "Kollaboratives Engagement: Zusammenarbeit, Kundenfeedback und ständige Kommunikation priorisieren, um innovative, bedeutungsvolle Designs zu schaffen, die bei Stakeholdern Anklang finden."
        ),
        "Narrative-Driven Design: Crafting spaces that tell a story and engage communities, enriched through collaborative input and ongoing client dialogue.": (
            "Conception narrative : créer des espaces qui racontent une histoire et engagent les communautés, enrichis par une contribution collaborative et un dialogue client continu.",
            "Narratives Design: Räume schaffen, die eine Geschichte erzählen und Gemeinschaften einbeziehen, bereichert durch kollaborativen Input und fortlaufenden Kundendialog."
        ),
        "Sustainable High-Tech Solutions: Integrating green materials, smart systems, and innovative forms, developed with client collaboration and feedback to ensure sustainable outcomes.": (
            "Solutions high-tech durables : intégrer des matériaux verts, des systèmes intelligents et des formes innovantes, développés avec la collaboration et les retours clients pour garantir des résultats durables.",
            "Nachhaltige High-Tech-Lösungen: Grüne Materialien, intelligente Systeme und innovative Formen integrieren, entwickelt mit Kundenzusammenarbeit und Feedback für nachhaltige Ergebnisse."
        ),
        "Challenging the Status Quo: Embracing a what can't be done mindset to push boundaries, shaped by constant communication and client insights to drive bold innovation.": (
            "Défier le statu quo : adopter un état d'esprit 'ce qui ne peut pas être fait' pour repousser les limites, façonné par une communication constante et les insights clients pour stimuler l'innovation audacieuse.",
            "Status Quo herausfordern: Eine 'Was nicht getan werden kann'-Mentalität annehmen, um Grenzen zu verschieben, geprägt durch ständige Kommunikation und Kundeneinblicke für kühne Innovation."
        ),
        "User-Centric and Inclusive: Prioritizing functionality, accessibility, and excellence, co-designed with clients through continuous feedback and collaborative processes.": (
            "Centré sur l'utilisateur et inclusif : prioriser la fonctionnalité, l'accessibilité et l'excellence, co-conçu avec les clients par des retours continus et des processus collaboratifs.",
            "Benutzerzentriert und inklusiv: Funktionalität, Zugänglichkeit und Exzellenz priorisieren, gemeinsam mit Kunden durch kontinuierliches Feedback und kollaborative Prozesse entwickelt."
        ),
        "Research-Based and AI-Backed: Grounded in deep research and cutting-edge technology, enhanced by iterative client collaboration and constant communication for impactful solutions.": (
            "Basé sur la recherche et soutenu par l'IA : ancré dans une recherche approfondie et une technologie de pointe, amélioré par une collaboration client itérative et une communication constante pour des solutions impactantes.",
            "Forschungsbasiert und KI-gestützt: Verwurzelt in tiefgehender Forschung und modernster Technologie, verbessert durch iterative Kundenzusammenarbeit und ständige Kommunikation für wirkungsvolle Lösungen."
        ),
        "OUR CLIENTS": ("NOS CLIENTS", "UNSERE KUNDEN"),
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
                occurrences=[('main/templates/main/about.html', '')]
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
                occurrences=[('main/templates/main/about.html', '')]
            )
            po_de.append(entry)
            print(f"  Added: {english[:50]}...")
    
    po_de.save()
    print("✓ German translations updated")

if __name__ == '__main__':
    add_translations()
    print("\n✓ All about.html translations added successfully!")
