import pandas as pd
import smtplib

port = 587
df = pd.read_excel('F:\Internity\Book1.xlsx')

sender_mail = input("Enter your email address :  ")
sender_password = input("Enter your password :  ")

try:
    server = smtplib.SMTP("smtp.gmail.com",port)
    server.starttls()
    server.login(sender_mail,sender_password)
    for i in range(0,len(df)):
        name = df.iat[i,0]
        receiver_mail = df.iat[i,1]
        message = df.iat[i,2]
               
        server.sendmail(sender_mail,receiver_mail,message)
        
        print("Email sent successfully to ",name)
    server.quit()
except:
    print("Email not sent")
    server.quit()

