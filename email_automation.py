import smtplib

port = 587
sender_mail = input("Enter your email address :  ")
sender_password = input("Enter your password :  ")
receiver_mail = input("Enter receiver's mail address :  ")
message = input("Enter the message you want to send ")

try:
    server = smtplib.SMTP("smtp.gmail.com",port)
    server.starttls()
    server.login(sender_mail,sender_password)
    server.sendmail(sender_mail,receiver_mail,message)
    print("Email sent successfully")
    server.quit()
except:
    print("Email not sent")
    server.quit()
