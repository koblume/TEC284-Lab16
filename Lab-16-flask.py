from flask import Flask, render_template
from gpiozero import LED

app = Flask(__name__)
led1 = LED(18)
led2 = LED(23)
led3 = LED(24)

@app.route("/")
def index():
    return render_template("HTML Code-flask.html")

@app.route("/led1/<action>")
def LED1Control(action):
    if action == "on":
        led1.on()
        return "LED 1 Turned On"
    elif action == "off":
        led1.off()
        return "LED 1 Turned Off"
    else:
      return "Invalid Action"
      
    
@app.route("/led2/<action>")
def LED2Control(action):
    if action == "on":
        led2.on()
        return "LED 2 Turned On"
    elif action == "off":
        led2.off()
        return "LED 2 Turned Off"
    else:
      return "Invalid Action"
    
@app.route("/led3/<action>")
def LED3Control(action):
    if action == "on":
        led3.on()
        return "LED 3 Turned On"
    elif action == "off":
        led3.off()
        return "LED 3 Turned Off"
    else:
      return "Invalid Action"

if __name__ == "__main__":
    app.run(host="192.168.1.7", port=80)