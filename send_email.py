from email.mime.text import MIMEText
import smtplib

def send_email(fname,lname,ename,cname,county,sleeping,depression,appetite,aches):
    from_email="ENTEREMAILADDRESS"
    from_password="ENTERPASSWORD"
    to_email=ename

    subject="Thanks For Registering"
    message="Hey there, <strong>%s</strong>. <br><br> Thank you for signing up from <strong>%s</strong> county. We'll reach out to you via <strong>%s</strong> <br><br> Based on the below info: <br><br> Do you have trouble sleeping? <strong>%s</strong>. <br> Do you suffer from depression? <strong>%s</strong>. <br> Do you lack appetite? <strong>%s</strong>. <br> Do you have aches and pains in your body? <strong>%s</strong>. <br><br> We'll be sending a email soon. <br><br> Have a great day. <br><br> Hook Alert OUT!!! " %(fname, county, ename, sleeping, depression, appetite, aches)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    email_=smtplib.SMTP('SMTPSERVER','PORT#')
    email_.ehlo()
    email_.starttls()
    email_.login(from_email, from_password)
    email_.send_message(msg)
