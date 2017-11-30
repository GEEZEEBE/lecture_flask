import RPi.GPIO as GPIO       # Import GPIO library
import time       # Import 'time' library. Allows us to use 'sleep'
GPIO.setmode(GPIO.BOARD)       # Use board pin numbering
cpin = 13
GPIO.setup(cpin, GPIO.OUT)       # Setup GPIO Pin 11 to OUT
def Blink(numTimes,speed):
        for i in range(0,numTimes):      # Run loop numTimes
                print ("Iteration " , str(i+1))      # Print current loop
                GPIO.output(cpin,True)      # Switch on pin 11
                time.sleep(speed)      # Wait
                GPIO.output(cpin,False)      # Switch off pin 11
                time.sleep(speed)      # Wait
        print ("Done")       # When loop is complete, print "Done"
        GPIO.cleanup()
Blink(3,1)
