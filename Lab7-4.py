import RPi.GPIO as GPIO
import drivers
import time
from time import sleep

SW1 = 27
SW2 = 17
lcd_position = 0
count = 0
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)

display = drivers.Lcd()
display.lcd_clear()

try:
 while True:
    if GPIO.event_detected(SW1):
            count = count + 1
            count = count % 2
            if(count==0) :
                display.lcd_display_string("Surattana", 1)
                display.lcd_display_string("1165104000484", 2)
                          
                
            elif(count==1) :
                display.lcd_display_string("Teeraphat", 1)
                display.lcd_display_string("1165104000518", 2)
                         
                    

    elif GPIO.event_detected(SW2):
        time.sleep(0.5)
        display.lcd_clear()   
        display.lcd_display_string("Bye", 1)
        time.sleep(0.5)
        display.lcd_clear()


except KeyboardInterrupt:
    GPIO.remove_event_detect(SW1)
    GPIO.remove_event_detect(SW2)
    GPIO.cleanup()

display.lcd_clear()
print("\nBye...")
