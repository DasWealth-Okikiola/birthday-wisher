import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the SMTP server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Create a secure connection to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    try:
        # Log in to your email account
        server.login(sender_email, sender_password)

        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the message to the email
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        server.send_message(msg)

        print('Email sent successfully!')

    except Exception as e:
        print('An error occurred while sending the email:', str(e))

    finally:
        # Disconnect from the server
        server.quit()

# Example usage
sender_email = 'daswealthokikiola@gmail.com'
sender_password = 'wsvrsfitmvmjlqlz'
recipient_email = 'daswealthokikiola@gmail.com'
subject = 'Test Email'
message = 'This is a test email.'

send_email(sender_email, sender_password, recipient_email, subject, message)



##################### Normal Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

# HINT 2: Use pandas to read the birthdays.csv

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



