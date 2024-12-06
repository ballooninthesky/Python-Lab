from flask import Flask
import RPi.GPIO as GPIO
app = Flask(__name__)

# กำหนดโหมดของ GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# กำหนดขา GPIO ของ LED
LED1_GPIO = 17
LED2_GPIO = 27

# กำหนด GPIO เป็นโหมด Output
GPIO.setup(LED1_GPIO, GPIO.OUT)
GPIO.setup(LED2_GPIO, GPIO.OUT)

def turn_on(led):
    if led == 'led1':
        GPIO.output(LED1_GPIO, GPIO.HIGH)  # เปิด LED1
    elif led == 'led2':
        GPIO.output(LED2_GPIO, GPIO.HIGH)  # เปิด LED2
    else:
        pass  # ถ้า LED ไม่ถูกต้อง ไม่ต้องทำอะไร

def turn_off(led):
    if led == 'led1':
        GPIO.output(LED1_GPIO, GPIO.LOW)  # ปิด LED1
    elif led == 'led2':
        GPIO.output(LED2_GPIO, GPIO.LOW)  # ปิด LED2
    else:
        pass  # ถ้า LED ไม่ถูกต้อง ไม่ต้องทำอะไร

@app.route('/<led>/<action>')
def control_led(led, action):
    if led == 'led1':
        if action == 'on':
            turn_on('led1')
        elif action == 'off':
            turn_off('led1')
    elif led == 'led2':
        if action == 'on':
            turn_on('led2')
        elif action == 'off':
            turn_off('led2')

    return f"LED {led[-1]} - {action.upper()}"

@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
