#!/user/bin/python
# python code for my halloween project.  This code will receive a triger from a motion
# sensor and then turn on the fog, then make scary sounds, move some things and make
# some lights turn on and off and or blink.
# Also make sure that you run as SUDO

import time
import RPi.GPIO as GPIO
import os

#Here I set the board as the numbering scheme

GPIO.setwarnings(False)
print ('holloween script now loading....')

GPIO.setmode(GPIO.BOARD)
print ('mode set to board')


# Now I need to define the pins and how I plan to use them

GPIO.PIR = 7
GPIO.FOG = 11
GPIO.MOVEMENT = 13
GPIO.LIGHTS = 15

# Here I'm setting two vaiables for the while loop

Current_State = 0
Previous_State = 0

print ('GPIO pins 7, 11, , &  have now been set')

# Here I set the PIR as input
# Note here I set the pin as 0v pulled down.  Need to check if that's how it should be

GPIO.setup(GPIO.PIR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

print ('Motion detection ready to read')

# Now to set the fog, lights, movement as output

GPIO.setup(GPIO.FOG, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(GPIO.MOVEMENT, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(GPIO.LIGHTS, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN)

# Read PIR

GPIO.input(GPIO.PIR)

# Read PIR

try:
           print ('Waiting for motion')
           while GPIO.input(GPIO.PIR)==0:
               Current_State = 0
           print ('ready')
           while True:
               Current_State = GPIO.input(GPIO.PIR)
               if Current_State ==1 and Previous_State==0:
                   print ('Motion detected')
                   print ('Starting scary halloween stuff that Kelsey thought of')
                   print ('to scare everyone')
                   GPIO.output(GPIO.FOG, True)
                   print ('fog set to on....')
                   time.sleep(2)
                   print ('scary sounds started')
                   os.system('mpg321 1.mp3 &')
                   GPIO.output(GPIO.MOVEMENT, True)
                   time.sleep(2)
                   print ('movement on ......')
                   GPIO.output(GPIO.LIGHTS, True)
                   time.sleep(2)
                   print ('lights set to on...')
                   print ('now delay 6 min to reset everything')
                   time.sleep(600)
                   GPIO.output(GPIO.FOG, GPIO.LOW)
                   GPIO.output(GPIO.MOVEMENT, GPIO.LOW)
                   GPIO.output(GPIO.LIGHTS, GPIO.LOW) 
                   Previous_State = 1
               elif Current_State==0 and Previous_State==1:
                   print ('back to ready')
                   Previous_State=0
               time.sleep(0.01)
except KeyboardInterrupt:
           print ('Quit')
           GPIO.cleanup()
           
           
