import RPi.GPIO as GPIO
import time             # used so we can use delays
import smtplib           # to use the email function
import os                 # used to clear the terminal 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10,GPIO.IN)  # initiate inputs and outputs
GPIO.setup(27,GPIO.OUT)	 # PUD_UP is 1 PUD_DOWN is 0
GPIO.setup(17,GPIO.OUT)   # attatch a photoresistor to gpio 10 
GPIO.setup(22,GPIO.OUT)    # attatch a laser sensor to gpio 17
GPIO.output(17, GPIO.HIGH)  # attatch an LED to gpio 27
GPIO.output(27, GPIO.HIGH)   # attatch a photoresistor to gpio 
GPIO.output(22, GPIO.LOW)     # attatch buzzer to gpio 22

def email():                     # function to send an email
   content = 'Motion detected'
   gmail_sender= 'your gmail'  # configure this to your own gmail account
   gmail_passwd= 'your password' # fill this part with your password too
   server = smtplib.SMTP('smtp.gmail.com',587)
   server.ehlo()
   server.starttls()
   server.ehlo
   server.login(gmail_sender, gmail_passwd)
   server.sendmail(gmail_sender,gmail_sender,content)
   server.close()




while 1:
   if (GPIO.input(10) == False):    # while the laser is not blocked from pointing to the photo resistor
      GPIO.output(27, GPIO.LOW)      # the buzzer will not make a sound and the led will be off
      GPIO.output(22, GPIO.LOW)
      os.system('clear')
   else:
      email()                       # when the laser is blocked the buzzer will beep and the led will illuminate
      GPIO.output(27, GPIO.HIGH)    # might want to add a delay so that your email doesnt get spammed lol  ex time.sleep(5)
      GPIO.output(22, GPIO.HIGH)    # which will send the email every 5 seconds if the laser is tripped

