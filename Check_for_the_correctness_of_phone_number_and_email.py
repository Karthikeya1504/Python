'''
Write a python program to read a phone number and email id from the user and check for the correctness
'''


def validate_phone_number(phone):
    if phone.isdigit() and len(phone)==10:
        return True
    else:
        return False

def validate_email(email):
    if "@" in email and "." in email.split("@")[-1]:
        return True
    else:
        return False

#Input from the user
phone_number = input("Enter your phone number (10 digits): ")
email_id = input("Enter your email address: ")

#Validate phone number
if validate_phone_number(phone_number):
    print("Phone number is valid.")
else:
    print("Invalid phone number. Please enter exactly 10 digits.")

#Validate Email
if validate_email(email_id):
    print("Email address is valid.")
else:
    print("Invalid email address. Please check the format.")
