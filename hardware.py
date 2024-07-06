import RPi.GPIO as GPIO
import time
import tm1637

tm = tm1637.TM1637(clk=23, dio=24)
# Set GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Define GPIO pins for LEDs
RED_LED_1 = 2
YELLOW_LED_1 = 3
GREEN_LED_1 = 4

RED_LED_2 = 22
YELLOW_LED_2 = 17
GREEN_LED_2 = 27

# Set up GPIO pins
GPIO.setup([RED_LED_1, YELLOW_LED_1, GREEN_LED_1,
            RED_LED_2, YELLOW_LED_2, GREEN_LED_2], GPIO.OUT)

# Function to control traffic light


def light(pin=1,val=1):
    if pin==1:
        GPIO.output(RED_LED_1, GPIO.LOW)
        GPIO.output(YELLOW_LED_1, GPIO.LOW)
        GPIO.output(GREEN_LED_1, GPIO.LOW)
        if val==1:
            GPIO.output(RED_LED_1, GPIO.HIGH)
        elif val==2:
            GPIO.output(YELLOW_LED_1, GPIO.HIGH)
        else:
            GPIO.output(GREEN_LED_1, GPIO.HIGH)
    else:
        GPIO.output(RED_LED_2, GPIO.LOW)
        GPIO.output(YELLOW_LED_2, GPIO.LOW)
        GPIO.output(GREEN_LED_2, GPIO.LOW)
        if val==1:
            GPIO.output(RED_LED_2, GPIO.HIGH)
        elif val==2:
            GPIO.output(YELLOW_LED_2, GPIO.HIGH)
        else:
            GPIO.output(GREEN_LED_2, GPIO.HIGH)
def counter(count):
    tm.show("0000")
    while count>=0:
        
        tm.show(str(count))
        count-=1;
        time.sleep(1)
        
def traffic_lights():
    count1=5;
    count3=5;
    count2=2
    while True:
        # go-stop
        light(1,3)
        light(2,1)
        
        counter(count1)
        # stop-stop
        light(1,2)
        light(2,2)
        
        counter(count2)
        #stop-go
        light(1,1)
        light(2,3)
        counter(count3)
        



try:
    # Start the traffic light control
    traffic_lights()

except KeyboardInterrupt:
    # Clean up GPIO
    GPIO.cleanup()