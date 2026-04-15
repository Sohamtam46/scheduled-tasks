# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.

import os
import smtplib
import random
import datetime as dt
import pandas as pd
birthday_today = False

NAME_PLACEHOLDER = "[NAME]"
AGE_PLACEHOLDER = "[AGE]"

# getting current day details
now = dt.datetime.now()
present_year = now.year
present_day = now.day
present_month = now.month
# getting the birthday details
birthdays = pd.read_csv("birthdays.csv")

birthdays_dict = birthdays.to_dict(orient="records")
for people_details in birthdays_dict:
    if people_details["month"] == present_month and people_details["day"] == present_day:
        birthday_person_details = people_details
        birthday_today = True
        print("got a hit")

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

if birthday_today:
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as data:
        letter = data.read()
        output_letter_rough =letter.replace(NAME_PLACEHOLDER,birthday_person_details["name"])
        age = present_year - birthday_person_details["year"]
        output_letter = output_letter_rough.replace(AGE_PLACEHOLDER,str(age))
    with smtplib.SMTP("smtp.gmail.com") as connection:
        print("sending email....")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
                            from_addr=MY_EMAIL,
                            to_addrs=birthday_person_details["email"],
                            msg=f"Subject:Birthday Wishes!\n\n{output_letter}"
                            )
