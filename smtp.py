import smtplib

fromaddr = 'explanation123@gmail.com'
toaddrs  = 'pashaphb@gmail.com'
msg = 'Hello Pasha!'
password = 'qwerty123'
s = smtplib.SMTP('smtp.gmail.com:587')
s.ehlo()
s.starttls()
s.login(fromaddr,password)
s.set_debuglevel(1)
s.sendmail('explanation123@gmail.com','pashaphb@gmail.com',msg)
s.quit()