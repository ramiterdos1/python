from graphics import *

def Checkerboard() :
  win=GraphWin('Checkers', 100,100)
  off_x=10
  off_y=10
  size=10
  for i in range(8) :
     ipt=Point(off_x,off_y)
     for j in range(8) :
         if (i+j) %2 == 0 :
             color = 'white'
         else :
             color = 'black'
         pt1=Point(ipt.x+j*size,ipt.y)
         pt2=Point(ipt.x+(j+1)*size,ipt.y+size)
         rct=Rectangle(pt1,pt2)
         rct.draw(win)
         rct.setFill(color)
     off_y+=size

def CheckerboardRandMat(r,size) :
  length=len(r)
  win=GraphWin('Checkers', size*(length+2),size*(length+2))
  off_x=size
  off_y=size
  for i in range(length) :
     ipt=Point(off_x,off_y)
     for j in range(length) :
         if r[i][j] == 1 :
             color = 'white'
         else :
             color = 'black'
         pt1=Point(ipt.x+j*size,ipt.y)
         pt2=Point(ipt.x+(j+1)*size,ipt.y+size)
         rct=Rectangle(pt1,pt2)
         rct.draw(win)
         rct.setFill(color)
     off_y+=size

    
