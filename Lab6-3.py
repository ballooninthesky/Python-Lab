import RPi.GPIO as GPIO
SW = 22
LED = 18
count=0
st=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SW,GPIO.IN,pull_up_down = GPIO.PUD_UP)
try:
    while True:
        if GPIO.wait_for_edge(SW, GPIO.FALLING) :
            st=st+1
            st=st%2
            count=count+1
            if(st==1):
                GPIO.output (LED, True)
                print("LED => ON")
            else:   
                GPIO.output (LED, False)                  
                print("LED => OFF")
            print(f"{count}")
except KeyboardInterrupt:
    GPIO.cleanup()
print("\nBye")
