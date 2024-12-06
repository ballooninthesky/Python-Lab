from flask import Flask, render_template, request
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

@app.route('/', methods=['GET', 'POST'])
def index():
    led1_state = 'ON' if GPIO.input(LED1_GPIO) == GPIO.HIGH else 'OFF'
    led2_state = 'ON' if GPIO.input(LED2_GPIO) == GPIO.HIGH else 'OFF'

    if request.method == 'POST':
        led = request.form['led']
        if led == 'led1_on':
            turn_on('led1')
        elif led == 'led1_off':
            turn_off('led1')
        elif led == 'led2_on':
            turn_on('led2')
        elif led == 'led2_off':
            turn_off('led2')

    return render_template('index.html', led1_state=led1_state, led2_state=led2_state)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
