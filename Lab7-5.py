import RPi.GPIO as GPIO
import time
import drivers

display = drivers.Lcd()
display.lcd_clear()

SW1  = 17  
SW2  = 27

lcd_position = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.add_event_detect(SW1, GPIO.FALLING)
GPIO.add_event_detect(SW2, GPIO.FALLING)
display.lcd_display_string("LAB 7", 1)
count = 0
try:
    while True:
        if GPIO.event_detected(SW1):
            count += 1      
            if(count==0):
                display.lcd_display_string("LAB 7", 1)
            if(count==1):
                display.lcd_display_string(" LAB 7", 1)
            if(count==2):
                display.lcd_display_string("  LAB 7", 1)
            if(count==3):
                display.lcd_display_string("   LAB 7", 1)
            if(count==4):
                display.lcd_display_string("    LAB 7", 1)
            if(count==5):
                display.lcd_display_string("     LAB 7", 1)
            if(count==6):
                display.lcd_display_string("      LAB 7", 1)
            if(count==7):
                display.lcd_display_string("       LAB 7", 1)
            if(count==8):
                display.lcd_display_string("        LAB 7", 1)
            if(count==9):
                display.lcd_display_string("         LAB 7", 1)
            if(count==10):
                display.lcd_display_string("          LAB 7", 1)
            if(count==11):
                display.lcd_display_string("           LAB 7                  ", 1)                                                 
        elif GPIO.event_detected(SW2):
            count -= 1
            if(count==0):
                display.lcd_display_string("LAB 7  ", 1)
            if(count==1):
                display.lcd_display_string(" LAB 7  ", 1)
            if(count==2):
                display.lcd_display_string("  LAB 7  ", 1)
            if(count==3):
                display.lcd_display_string("   LAB 7 ", 1)
            if(count==4):
                display.lcd_display_string("    LAB 7 ", 1)
            if(count==5):
                display.lcd_display_string("     LAB 7 ", 1)
            if(count==6):
                display.lcd_display_string("      LAB 7 ", 1)
            if(count==7):
                display.lcd_display_string("       LAB 7 ", 1)
            if(count==8):
                display.lcd_display_string("        LAB 7 ", 1)
            if(count==9):
                display.lcd_display_string("         LAB 7 ", 1)
            if(count==10):
                display.lcd_display_string("          LAB 7 ", 1)
            if(count==11):
                display.lcd_display_string("           LAB 7 ", 1)
                
        time.sleep(0.5)

except KeyboardInterrupt:

    GPIO.remove_event_detect(SW1)
    GPIO.remove_event_detect(SW2)
    GPIO.cleanup()

    print("\nBye...")
