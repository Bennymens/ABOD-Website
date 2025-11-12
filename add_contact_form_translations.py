#!/usr/bin/env python3
"""
Script to add missing Careers and Other form translations to .po files
"""

import polib

def add_translations():
    # Translations mapping: English -> (French, German)
    translations = {
        # Careers section subtitle
        "Speak to Arup's recruitment teams about job opportunities and careers. Before sending a general enquiry, kindly review our application process to see if your question has already been addressed.": (
            "Parlez aux équipes de recrutement d'Arup des opportunités d'emploi et de carrière. Avant d'envoyer une demande générale, veuillez consulter notre processus de candidature pour voir si votre question a déjà été traitée.",
            "Sprechen Sie mit den Rekrutierungsteams von Arup über Jobmöglichkeiten und Karrieren. Bevor Sie eine allgemeine Anfrage senden, überprüfen Sie bitte unseren Bewerbungsprozess, um zu sehen, ob Ihre Frage bereits beantwortet wurde."
        ),
        
        # Form labels
        "First name": ("Prénom", "Vorname"),
        "Last name": ("Nom", "Nachname"),
        "Email address": ("Adresse e-mail", "E-Mail-Adresse"),
        "Phone number": ("Numéro de téléphone", "Telefonnummer"),
        "Company name": ("Nom de l'entreprise", "Firmenname"),
        "Job title": ("Titre du poste", "Berufsbezeichnung"),
        "Country/Location": ("Pays/Lieu", "Land/Standort"),
        "City/Town": ("Ville", "Stadt"),
        "How did you hear about us?": ("Comment avez-vous entendu parler de nous ?", "Wie haben Sie von uns erfahren?"),
        "What would you like to discuss?": ("De quoi aimeriez-vous discuter ?", "Worüber möchten Sie sprechen?"),
        "Area of business": ("Domaine d'activité", "Geschäftsbereich"),
        "Select your service of interest (if known)": ("Sélectionnez votre service d'intérêt (si connu)", "Wählen Sie Ihren interessierenden Service (falls bekannt)"),
        
        # Select options
        "Select": ("Sélectionner", "Auswählen"),
        "Select...": ("Sélectionner...", "Auswählen..."),
        "Submit": ("Soumettre", "Einreichen"),
        
        # How did you hear about us options
        "Social Media": ("Réseaux sociaux", "Soziale Medien"),
        "Website": ("Site web", "Webseite"),
        "Referral": ("Référence", "Empfehlung"),
        "Advertisement": ("Publicité", "Werbung"),
        "Job Board": ("Site d'emploi", "Jobportal"),
        "LinkedIn": ("LinkedIn", "LinkedIn"),
        "Indeed": ("Indeed", "Indeed"),
        "Glassdoor": ("Glassdoor", "Glassdoor"),
        "University/Career Fair": ("Université/Salon de l'emploi", "Universität/Karrieremesse"),
        "Networking Event": ("Événement de réseautage", "Networking-Event"),
        
        # Area of business options
        "Buildings": ("Bâtiments", "Gebäude"),
        "Infrastructure": ("Infrastructure", "Infrastruktur"),
        "Transport": ("Transport", "Transport"),
        "Energy": ("Énergie", "Energie"),
        "Water": ("Eau", "Wasser"),
        "Environment": ("Environnement", "Umwelt"),
        "Cities & Urban Design": ("Villes et design urbain", "Städte & Stadtgestaltung"),
        "Digital & Technology": ("Digital et technologie", "Digital & Technologie"),
        "Advisory": ("Conseil", "Beratung"),
        "Health": ("Santé", "Gesundheit"),
        "Education": ("Éducation", "Bildung"),
        "Defence": ("Défense", "Verteidigung"),
        "Mining": ("Mines", "Bergbau"),
        "Maritime": ("Maritime", "Maritime"),
        "Property & Real Estate": ("Immobilier", "Immobilien & Grundbesitz"),
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
                occurrences=[('main/templates/main/contact.html', '')]
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
                occurrences=[('main/templates/main/contact.html', '')]
            )
            po_de.append(entry)
            print(f"  Added: {english[:50]}...")
    
    po_de.save()
    print("✓ German translations updated")

if __name__ == '__main__':
    add_translations()
    print("\n✓ All contact form translations added successfully!")
