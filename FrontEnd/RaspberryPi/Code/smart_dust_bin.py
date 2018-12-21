import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def getDistance(): #To measure the distance using the distance sensor
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

def getPresence(): #To judge the presence of a person as per the distance measured by the distance sensor
    dist=getDistance()
    maxDist = 75
    if(dist <= maxDist):
        return(True)
    else:
        return(False)

def servo(pin, angle): #Rotates the servo motor at a given pin to the desired angle
	GPIO.setup(pin, GPIO.OUT)
	pwm=GPIO.PWM(pin, 50)
	p=angle*0.055555
	p=p+2.5
	pwm.start(p)
	time.sleep(3)
	pwm.stop()

def binOpen():
    servo(17, 130)

def binClose():
    servo(17, 0)


#The main program
binClose()
while(True):
    flag=0
    presence=getPresence()
    time.sleep(0.5)
    while(presence == True):
        binOpen()
        flag=1
        time.sleep(7)
        presence=False
        presence=getPresence()
        time.sleep(0.5)
    time.sleep(0.5)
    if(flag==1):
        binClose()
        flag=0
    time.sleep(0.5)

GPIO.cleanup()
