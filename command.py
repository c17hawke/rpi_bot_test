# import curses, GPIO and time
import curses
import RPi.GPIO as GPIO
import time

#set GPIO numbering mode and define output pins
LEFT_POS = 6
LEFT_NEG = 13
RIGHT_POS = 19
RIGHT_NEG = 26


GPIO.setmode(GPIO.BOARD)
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
            elif char == ord('d'):
                GPIO.output(LEFT_NEG,True)
                GPIO.output(RIGHT_NEG,True)
                time.sleep(.5)
                GPIO.output(LEFT_POS,True)
                GPIO.output(LEFT_NEG,False)
                GPIO.output(RIGHT_POS,True)
                GPIO.output(RIGHT_NEG,False)
                time.sleep(.5)
                GPIO.output(LEFT_POS,True)
                GPIO.output(LEFT_NEG,False)
                GPIO.output(RIGHT_POS,False)
                GPIO.output(RIGHT_NEG,True)
                time.sleep(.5)
                GPIO.output(LEFT_POS,False)
                GPIO.output(LEFT_NEG,True)
                GPIO.output(RIGHT_POS,True)
                GPIO.output(RIGHT_NEG,False)
                time.sleep(.5)
                GPIO.output(LEFT_NEG,False)
                GPIO.output(RIGHT_POS,False)
            elif char == 10:
                GPIO.output(LEFT_POS,False)
                GPIO.output(LEFT_NEG,False)
                GPIO.output(RIGHT_POS,False)
                GPIO.output(RIGHT_NEG,False)
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    GPIO.cleanup()
    