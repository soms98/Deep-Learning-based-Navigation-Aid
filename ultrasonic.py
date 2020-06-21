#importing the Libraries
import RPi.GPIO as GPIO
import time


#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def glowLed(LED_PIN):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LED_PIN,GPIO.OUT)
    # print "LED on"
    GPIO.output(LED_PIN,GPIO.HIGH)
    time.sleep(1)
    # print "LED off"
    GPIO.output(LED_PIN,GPIO.LOW)
    

def distance(GPIO_TRIGGER, GPIO_ECHO):
    # set GPIO Direction (IN/ OUT)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)

    # Set Trigger to high
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = TimeElapsed * 34300 / 2

    return distance



#Main Program
def ultrasonicCall():
    try:
        while True:
            # calculating front distance
            dist = distance(2, 3) # GPIO pin2 - trig, pin3 - echo
            print ("Measured Distance from front = %.1f cm" % dist)
            time.sleep(1)
            '''
            if(dist<40):
                glowLed(16) # GPIO pin
            '''

            # calculating left distance
            dist_left = distance(17, 18) # GPIO pin - trig, pin - echo
            print("Measured Distance from left = %.1f cm" % dist_left)
            time.sleep(1)
            '''
            if(dist_left<40):
                glowLed(20) # GPIO pin
            '''

            # calculating right distance
            dist_right = distance(26, 19) # GPIO pin2 - trig, pin3 - echo
            print("Measured Distance from right = %.1f cm" % dist_right)
            time.sleep(1)
            '''
            if(dist_right<40):
                glowLed(21) # GPIO pin
            '''

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

