import csv

# Read the CSV file
contacts = []
with open('Vcf/contacthenna.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        contacts.append(row)

# Create vCard content
vcf_content = ""
for contact in contacts:
    vcf_content += "BEGIN:VCARD\n"
    vcf_content += "VERSION:3.0\n"
    vcf_content += f"N:{contact.get('last_name', '')};{contact.get('first_name', '')};;;\n"
    vcf_content += f"FN:{contact.get('first_name', '')} {contact.get('last_name', '')}\n"
    vcf_content += f"TEL;TYPE=CELL:{contact.get('phone', '')}\n"
    vcf_content += "END:VCARD\n"

# Save to .vcf file
with open('Vcf/Henna.vcf', mode='w', encoding='utf-8') as file:
    file.write(vcf_content)

print("vCard file created successfully.")
