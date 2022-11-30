
#Programming Project 4


#Start
from graphics import *
import time

# Frame is a rectangle offset by 20 pixels from the edges of the window and has a black outline of 10 pixels width 
def create_frame(window):
    frame = Rectangle(Point(20, 20), Point(window.getWidth() - 20, window.getHeight() - 20))
    frame.config['outline'] = "black"  
    frame.config['width'] = 10 
    return frame


# create display text to display time
def create_display_text(window):
    displaytext = Text(Point(window.getWidth() / 2, window.getHeight() / 2), text="")
    #font, size, style and color
    displaytext.setFace('times roman')
    displaytext.setSize(25)
    displaytext.setStyle('bold')
    displaytext.setFill('red')
    displaytext.setOutline('red')
    return displaytext

# method to return current time in seconds
def getTimeSeconds():
    # fetching hours, minutes and seconds using time module
    h = int(time.strftime("%H"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    # returning total time in seconds
    return (h * 60 * 60) + (m * 60) + s


# Time Conversions
# 60 Seconds = 1 minute
# 3600 seconds = 1 hour
# 60 minutes = 1 hour
# 86400 seconds = 1 day
# 24 hours =  1 day
# 12 hours = 1/2 day
# Day (AM) is midnight to noon , 12 hours
# Night (PM) is noon to midnight, 12 hours
#Time
def getTime(seconds):
# converting seconds to minutes and hours
    m = seconds // 60
    h = m // 60
# wrapping the values so that each value is under proper range
    m = m % 60  
    s = seconds % 60  
    h = h % 24
    am_pm = "AM"
# converting time to 12 hr format
    if h == 0:
        h = 12
# if h is already 12, setting am_pm to "PM"
    elif h == 12:
        am_pm = "PM"
# if h>12, subtracting 12 and setting am_pm to "PM"
    elif h > 12:
        am_pm = "PM"
        h = h - 12
# returning time string properly formatted
    return '{:d}:{:02d}:{:02d} {:s}'.format(h, m, s, am_pm)


# main method
def main():
# creating a window
    win = GraphWin("CSC 110 Digital Clock", 300, 200)
# setting background
    win.setBackground('lightgreen')
# creating frame
    frame = create_frame(win)
# creating time text label
    time_text = create_display_text(win)
# draw
    frame.draw(win)
    time_text.draw(win)
# fetching current time in seconds
    seconds = getTimeSeconds()
    while win.isOpen():
# converting seconds to formatted time
        formatted = getTime(seconds)
# display text
        time_text.setText(formatted)
# updating seconds
        seconds += 1
# pausing for 1 second
        time.sleep(1)


#End
main()

