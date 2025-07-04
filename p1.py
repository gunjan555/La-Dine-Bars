import smtplib
from email.message import EmailMessage

# ✅ STEP 1: Email details as a dictionary (Python data structure)
email_details = {
    'from': 'gunjanshambwani@gmail.com',
    'to': 'rajpaladitya99@gmail.com',
    'subject': 'Namaskaram from Python 🐍',
    'body': 'Hello! This is La Dine and Bars writing this email to inform you that the festive offer is live at our restaurant kindly ensure your presence for trying amazing delicaies !'
}

# ✅ STEP 2: Create the EmailMessage object using values from dict
msg = EmailMessage()
msg['From'] = email_details['from']
msg['To'] = email_details['to']
msg['Subject'] = email_details['subject']
msg.set_content(email_details['body'])

# ✅ STEP 3: Send the email via Gmail SMTP
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_details['from'], 'kajv kqlp nnxk ctec')  # 👉 Use App Password, not regular one!
        smtp.send_message(msg)
        print("✅ Email sent successfully!!!!")
except Exception as e:
    print("❌ Error while sending email:", e)