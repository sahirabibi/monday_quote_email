import smtplib
import datetime as dt
import random

email = input("Insert your email:\n")
password = input("Insert your password:\n")
recipient  = input("Insert email of recipient\n")

# get the day of week 
now = dt.datetime.now()
current_day = now.weekday()

#send email with quote if its monday
if current_day == 0:
    # get quotes 
    with open("./quotes.txt", "r") as f:
        quotes = f.readlines()
        monday_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=email, password=password)
        conn.sendemail(from_addr=email, to_addrs=recipient,
                    msg=f"Subject:Monday Morning Quote!\n\n{monday_quote}")






   



