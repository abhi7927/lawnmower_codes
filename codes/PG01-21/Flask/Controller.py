import RPi.GPIO as GPIO
from flask import Flask, render_template, request
from interfaces import *

wheel = Wheel()

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
    4 : {'name' : 'LEFT', 'state' : False},
    2 : {'name' : 'RIGHT', 'state' : False},
    1 : {'name' : 'FORWARD', 'state' : False},
    3 : {'name' : 'BACKWARD', 'state' : False}
   }



@app.route("/")
def main():
    # For each pin, read the pin state and store it in the pins dictionary:
    #for pin in pins:
        #pins[pin]['state'] = GPIO.input(pin)
    # Put the pin dictionary into the template data dictionary:
    templateData = {
      'pins' : pins
      }
    # Pass the template data into the template main.html and return it to the user
    return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Convert the pin from the URL into an integer:
    changePin = int(changePin)
   # Get the device name for the pin being changed:
    deviceName = pins[changePin]['name']
    # If the action part of the URL is "on," execute the code indented below:

    if action == "on":
      # Set the pin high:
        if changePin == 1:
            wheel.exe_motor('r')
            wheel.exe_motor('f')
            pins[1]['state'] = True
            pins[2]['state'] = False
            pins[3]['state'] = False
            pins[4]['state'] = False
        elif changePin == 2:
            wheel.exe_motor('rt')
            pins[2]['state'] = True
            pins[1]['state'] = False
            pins[3]['state'] = False
            pins[4]['state'] = False
        elif changePin == 3:
            wheel.exe_motor('b')
            pins[3]['state'] = True
            pins[2]['state'] = False
            pins[1]['state'] = False
            pins[4]['state'] = False
        elif changePin == 4:
            wheel.exe_motor('lt')
            pins[4]['state'] = True
            pins[2]['state'] = False
            pins[3]['state'] = False
            pins[1]['state'] = False
        # Save the status message to be passed into the template:
        message = "Turned " + deviceName + " on."
    if action == "off":
        pins[changePin]['state'] = False
        wheel.exe_motor('s')
        message = "Turned " + deviceName + " off."

    # For each pin, read the pin state and store it in the pins dictionary:
    #for pin in pins:
        #pins[pin]['state'] = GPIO.input(pin)

    # Along with the pin dictionary, put the message into the template data dictionary:
    templateData = {
      'pins' : pins
    }

    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

