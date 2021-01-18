import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, adress, name, city, port, date, price):
        with smtplib.SMTP("smtp.gmail.com") as conect:
            conect.starttls()
            conect.login(user="sberrusmoscow@gmail.com", password="00ls0002002123")
            conect.sendmail(from_addr="sberrusmoscow@gmail.com", to_addrs= adress,
                            msg=f"Subject: Dear {name}\n\n We got direct flight for you in {city}\n\nflight would be from airport {port} in {date} it would cost {price}$ for you!")
    def multiway(self, adress, name, city, peresadki=list, port=str, date=str, price=int):
        for i in peresadki:
            target = ""
            if peresadki.index(i) != len(peresadki) - 1:
                way = f"{i} =>"
                target += way
            else:
                way = f"{i}"
                target += way

        with smtplib.SMTP("smtp.gmail.com") as conect:
            conect.starttls()
            conect.login(user="sberrusmoscow@gmail.com", password="00ls0002002123")
            conect.sendmail(from_addr="sberrusmoscow@gmail.com", to_addrs= adress,
                            msg=f"Subject: Dear {name}\n\n We got non-direct flight for you in {city}\n\nflight would be from airport {port} to {target} in {date} it would cost {price}$ for you!")


