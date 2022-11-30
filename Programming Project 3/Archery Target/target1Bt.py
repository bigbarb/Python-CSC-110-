#Brian Tran
#Programing Progect 3
#11/20/20
#target1.py

#Start

from graphics import *

#Creating Window
win=GraphWin('Target', 400,400)

#Drawing rings of the Archery Target, 5 rings (White, Black, Blue, Red, and Yellow)

#Fifth ring             
fifthring= Circle(Point(200,200), 50)
fifthring.setFill('white')
fifthring.setOutline('black')
fifthring.draw(win)
             
#Fourth ring            
fourthring= Circle(Point(200,200),40)
fourthring.setFill('black')
fourthring.setOutline('black')
fourthring.draw(win)             

#Third ring
thirdring= Circle(Point(200,200), 30)
thirdring.setFill('blue')
thirdring.setOutline('blue')
thirdring.draw(win)

#Second ring
secondring= Circle(Point(200,200), 20)
secondring.setFill('red')
secondring.setOutline('red')
secondring.draw(win)

#Center Ring
center= Circle(Point(200,200),10)
center.setFill('yellow')
center.setOutline('yellow')
center.draw(win)

#End
input("Press <Enter> to quit.")
win.close()

