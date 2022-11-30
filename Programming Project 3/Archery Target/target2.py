#target2.py

#Start

from graphics import *

#User input(s) and equations and calculations
diameter = float(input('Enter diameter of outermost circle: '))
centerradius = (diameter/5)/2
secondringradius = centerradius *2
thirdringradius= centerradius *3
fourthringradius = centerradius *4
fifthringradius = diameter/2

#Cordinates
Cx = (diameter/2)+1
Cy = (diameter/2)+1

#Creating Window for Archery Target
win= GraphWin('Target', diameter + 5, diameter +5)

#Drawing rings of the Archery Target, 5 rings (White, Black, Blue, Red, and Yellow)

#Fifth ring             
fifthring= Circle(Point(Cx,Cy), fifthringradius)
fifthring.setFill('white')
fifthring.setOutline('black')
fifthring.draw(win)
             
#Fourth ring            
fourthring= Circle(Point(Cx,Cy),fourthringradius)
fourthring.setFill('black')
fourthring.setOutline('black')
fourthring.draw(win)             

#Third ring
thirdring= Circle(Point(Cx,Cy),thirdringradius)
thirdring.setFill('blue')
thirdring.setOutline('blue')
thirdring.draw(win)

#Second ring
secondring= Circle(Point(Cx,Cy),secondringradius)
secondring.setFill('red')
secondring.setOutline('red')
secondring.draw(win)

#Center Ring
center= Circle(Point(Cx, Cy),centerradius)
center.setFill('yellow')
center.setOutline('yellow')
center.draw(win)

#End
input("Press <Enter> to quit.")
win.close()

