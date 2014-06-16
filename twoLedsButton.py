import RPi.GPIO as GPIO
pinButton = 4 # pin 7
pinLedGreen = 25 # pin 6
pinLedRed = 24 # pin 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinButton, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(pinLedRed, GPIO.OUT)
GPIO.setup(pinLedGreen, GPIO.OUT)
while True:
  GPIO.wait_for_edge(pinButton, GPIO.FALLING)
  print("Button Pressed")
  GPIO.output(pinLedRed, 1)
  GPIO.output(pinLedGreen, 0)
  GPIO.wait_for_edge(pinButton, GPIO.RISING)
  print("Button Released")
  GPIO.output(pinLedRed, 0)
  GPIO.output(pinLedGreen, 1)
GPIO.cleanup()
