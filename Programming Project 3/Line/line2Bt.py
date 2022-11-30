#Brian Tran
#Programing Progect 3
#11/20/20
#line2.py


#Start
from graphics import *
import math
def main():
    win = GraphWin('Line Segment')
    
#Mouse Click 1   
    p1 = win.getMouse()
    p1.getX()
    p1.getY()
    p1.draw(win)
    mouseclick1x = p1.getX()               
    mouseclick1y = p1.getY()
#Mouse Click 2                       
    p2 = win.getMouse()
    p2.getX()
    p2.getY()
    p2.draw(win)               
    mouseclick2x = p2.getX()
    mouseclick2y = p2.getY()
#Calculate Slope with formulas on Page 127 chapter 4               
    slopex = mouseclick2x - mouseclick1x
    slopey = mouseclick2y - mouseclick1y
    
    slope = slopey/slopex
    print("Slope is", slope)
#Calculate Length with formula on page 127 chapter 4   
    length= math.sqrt(math.pow(slopex, 2) + math.pow(slopey,2))
    print("length is", length)
    
#Midpoint formula 
    midpointx= (mouseclick1x + mouseclick2x)/ 2
    midpointy= (mouseclick1y + mouseclick2y)/ 2

    center = Point(midpointx, midpointy)
    center.setFill('Cyan')
    center.setOutline('Cyan')
    Line(Point(mouseclick1x,mouseclick1y), Point(mouseclick2x,mouseclick2y)).draw(win)
    center.draw (win)
#Labeling Midpoint
    offset= 100,000
    labelmidpointx = (midpointx)
    labelmidpointy = (midpointy-10)
    labelmidpointtext = ('midpoint of line is:' ,midpointx,',',midpointy)

    labelmidpoint = Text(Point(labelmidpointx, labelmidpointy),labelmidpointtext)
    labelmidpoint.draw(win)                     

main()
    

   

      

