import polib

# Load the French .po file
po = polib.pofile('locale/fr/LC_MESSAGES/django.po')

# Translation to add
english = "Speak to ABOD's recruitment teams about job opportunities and careers. Before sending a general enquiry, kindly review our application process to see if your question has already been addressed."
french = "Parlez aux équipes de recrutement d'ABOD concernant les opportunités d'emploi et les carrières. Avant d'envoyer une demande générale, veuillez consulter notre processus de candidature pour voir si votre question a déjà été traitée."

# Check if entry already exists
entry = po.find(english)
if entry:
    entry.msgstr = french
    print(f"Updated translation")
else:
    entry = polib.POEntry(
        msgid=english,
        msgstr=french,
    )
    po.append(entry)
    print(f"Added translation")

# Save the file
po.save('locale/fr/LC_MESSAGES/django.po')
print("Contact subtext translation added to django.po")
