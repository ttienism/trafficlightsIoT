from gpiozero import LED, Button
from time import sleep
from signal import pause

ledred = LED(25)
ledyellow = LED(24)
ledgreen = LED(14)
button = Button(2)
ledgreen.on()
while True:
    button.wait_for_press()
    ledgreen.off()
    ledyellow.on()
    sleep(3)
    ledyellow.off()
    ledred.on()
    sleep(10)
    ledred.off()
    ledgreen.on()
