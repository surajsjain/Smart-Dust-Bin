import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def getDistance():
    trig=4
    echo=18

    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    GPIO.output(trig, True)
    time.sleep(0.0001)
    GPIO.output(trig, False)

    while GPIO.input(echo) == False:
        start=time.time()

    while GPIO.input(echo) == True:
        end=time.time()

    sig_time= end-start

    distance= sig_time/0.000058

    return(distance)

def getPresence():
    dist=getDistance()

    if(dist <= 100):
        return(True)
    else:
        return(False)

print str(getPresence())
