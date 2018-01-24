import RPi.GPIO as GPIO
import time             # used so we can use delays
import smtplib
import os
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10,GPIO.IN)  # initial value of input
GPIO.setup(27,GPIO.OUT)	 # PUD_UP is 1 PUD_DOWN is 0
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.output(17, GPIO.HIGH)
GPIO.output(27, GPIO.HIGH)
GPIO.output(22, GPIO.LOW)

def email():
   content = 'Motion detected'
   gmail_sender= 'jdon.rp3@gmail.com'
   gmail_passwd= 'ihaveapiano'
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   server.starttls()
   server.ehlo
   server.login(gmail_sender, gmail_passwd)
   server.sendmail(gmail_sender,gmail_sender,content)
   server.close()




while 1:
   if (GPIO.input(10) == False): 
      GPIO.output(27, GPIO.LOW)
      GPIO.output(22, GPIO.LOW)
      os.system('clear')
   else:
      email() 
      GPIO.output(27, GPIO.HIGH)
      GPIO.output(22, GPIO.HIGH)

