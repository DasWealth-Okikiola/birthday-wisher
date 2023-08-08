import pandas
import random
import smtplib
import datetime as time_module
today = time_module.datetime.now()
today_tuple = (today.month, today.day)

host = "your Gmail"
password = "your password"


day_data = pandas.read_csv("birthdays.csv")
new_dic = {(data_row.month, data_row.day): data_row for (index, data_row) in day_data.iterrows()}


if today_tuple in new_dic:
    the_person = new_dic[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as chosen_letter:
        contents = chosen_letter.read()
        contents = contents.replace("[NAME]", the_person["name"])
        contents = contents.replace("Angela", "DasWealth")
        # contents.replace("Angela", "DasWealth")
        # print(contents)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.login(user=host, password=password)
        server.starttls()
        server.sendmail(from_addr=host,
                        to_addrs=the_person["email"],
                        msg=f"Subject:Happy Birthday!!\n\n{contents}")
        print("Email sent successfully!!")
