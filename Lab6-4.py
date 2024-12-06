import RPi.GPIO as GPIO
SW = 22
LEDr = 14
LEDg = 15
LEDb = 18
count=0
st=0
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDr, 0)
GPIO.setup(LEDg, 0)
GPIO.setup(LEDb, 0)
GPIO.setup(SW,GPIO.IN,pull_up_down = GPIO.PUD_UP)
GPIO.output (LEDr, False)
GPIO.output (LEDg, False)
GPIO.output (LEDb, False)
try:
    while True:
        if GPIO.wait_for_edge(SW, GPIO.FALLING) :
            st=st+1
            st=st%8
            count=count+1
            if(st==0):
                GPIO.output (LEDr, False)
                GPIO.output (LEDg, False)
                GPIO.output (LEDb, False)
                print("LED => OFF")
            elif(st==1):
                GPIO.output (LEDr, False)
                GPIO.output (LEDg, False)
                GPIO.output (LEDb, True)
                print("LED => BLUE")
            elif(st==2):   
                GPIO.output (LEDr, False)
                GPIO.output (LEDg, True)
                GPIO.output (LEDb, False)
                print("LED => GREEN")
            elif(st==3):   
                GPIO.output (LEDr, False)
                GPIO.output (LEDg, True)
                GPIO.output (LEDb, True)
                print("LED => CYAN")
            elif(st==4):   
                GPIO.output (LEDr, True)
                GPIO.output (LEDg, False)
                GPIO.output (LEDb, False)
                print("LED => RED")
            elif(st==5):   
                GPIO.output (LEDr, True)
                GPIO.output (LEDg, False)
                GPIO.output (LEDb, True)
                print("LED => Magenta")
            elif(st==6):   
                GPIO.output (LEDr, True)
                GPIO.output (LEDg, True)
                GPIO.output (LEDb, False)
                print("LED => YELLOW")
            elif(st==7):   
                GPIO.output (LEDr, True)
                GPIO.output (LEDg, True)
                GPIO.output (LEDb, True)
                print("LED => WHITE")
            print(f"{count}")
except KeyboardInterrupt:
    GPIO.cleanup()
print("\nBye")
