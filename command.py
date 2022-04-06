# import curses, GPIO and time
import curses
import RPi.GPIO as GPIO
import time

#set GPIO numbering mode and define output pins
LEFT_POS = 6
LEFT_NEG = 13
RIGHT_POS = 19
RIGHT_NEG = 26


GPIO.setmode(GPIO.BCM)
GPIO.setup(LEFT_POS,GPIO.OUT)
GPIO.setup(LEFT_NEG,GPIO.OUT)
GPIO.setup(RIGHT_POS,GPIO.OUT)
GPIO.setup(RIGHT_NEG,GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
                GPIO.output(LEFT_POS,False)
                GPIO.output(LEFT_NEG,True)
                GPIO.output(RIGHT_POS,False)
                GPIO.output(RIGHT_NEG,True)
            elif char == curses.KEY_DOWN:
                GPIO.output(LEFT_POS,True)
                GPIO.output(LEFT_NEG,False)
                GPIO.output(RIGHT_POS,True)
                GPIO.output(RIGHT_NEG,False)
            elif char == curses.KEY_RIGHT:
                GPIO.output(LEFT_POS,True)
                GPIO.output(LEFT_NEG,False)
                GPIO.output(RIGHT_POS,False)
                GPIO.output(RIGHT_NEG,True)
            elif char == curses.KEY_LEFT:
                GPIO.output(LEFT_POS,False)
                GPIO.output(LEFT_NEG,True)
                GPIO.output(RIGHT_POS,True)
                GPIO.output(RIGHT_NEG,False)
            elif char == ord('s'):
                GPIO.output(LEFT_POS,False)
                GPIO.output(LEFT_NEG,False)
                GPIO.output(RIGHT_POS,False)
                GPIO.output(RIGHT_NEG,False)
             
finally:
    #Close down curses properly, inc turn echo back on!
    GPIO.output(LEFT_POS,False)
    GPIO.output(LEFT_NEG,False)
    GPIO.output(RIGHT_POS,False)
    GPIO.output(RIGHT_NEG,False)
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    