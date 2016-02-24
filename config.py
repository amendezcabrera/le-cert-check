#!/usr/bin/env python

## CONFIG Modify these values

# Certs
# · Path
root = "/etc/letsencrypt/live/"
# · Name
cert_name = "cert.pem"

# Email
mail_from = 'YOUR NAME'
mail_rcpt = ['RCPT_EMAIL_1', 'RCPT_EMAIL_2']
mail_subject = "EMAIL SUBJECT"
email = "Subject: %s\n\n"%mail_subject

# Days (to check) until expiration date to throw the warning
days = 15