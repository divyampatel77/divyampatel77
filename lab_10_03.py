contact = {
    "Name": input("Enter your name: "),
    "Phone": input("Enter your phone number: "),
    "Email": input("Enter your email: ")
}

with open('contact.vcf', 'w') as f:
    f.write("BEGIN:VCARD\n")
    f.write("VERSION:3.0\n")
    f.write(f"N:{contact['Name']}\n")
    f.write(f"TEL:{contact['Phone']}\n")
    f.write(f"EMAIL:{contact['Email']}\n")
    f.write("END:VCARD\n")

print("vCard created successfully.")