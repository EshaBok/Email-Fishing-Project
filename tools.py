fraud_words = ["urgent", "action required", "free", "congradulations"]


def scan_email_for_fraud(email):
   email = email.lower()
   score = 0
   for word in fraud_words:
      if word in email:
         score += 10
   return score

email = input("Copy and enter the email content: ")
emailscore = scan_email_for_fraud(email)
if emailscore >= 15:
   print("This email is likely to be fraudulent.")
else:   print("This email is likely to be safe.")
