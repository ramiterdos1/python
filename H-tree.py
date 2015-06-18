import turtle;
def draw_htree(b, n,i, len) :
    if n == i :
      b.forward(len/2)
      b.right(90)
      b.forward(len/2)
      #
      b.right(180)
      b.forward(len)
      #
      b.right(180)
      b.forward(len/2)
      b.right(90)
      b.forward(len)
      b.right(90)
      b.forward(len/2)
      #
      b.right(180)
      b.forward(len)
      #
      b.left(180)
      b.forward(len/2)
      b.right(90)
      b.forward(len/2)            
    else :
      b.forward(len/2)
      b.right(90)
      b.forward(len/2)
      b.right(90)
      draw_htree(b,n,i+1,len/2)
      
      b.right(90)
      b.forward(len)
      b.left(90)
      draw_htree(b,n,(i+1),len/2)
      b.left(90)
      b.forward(len/2)
      b.right(90)
      b.forward(len)
      b.right(90)
      b.forward(len/2)
      b.right(90)
      draw_htree(b,n,(i+1),len/2)
      b.right(90)
      b.forward(len)
      b.left(90)
      draw_htree(b,n,(i+1),len/2)
      b.left(90)
      b.forward(len/2)
      b.right(90)
      b.forward(len/2)
            
n = raw_input('Enter no of iterations :')
n= int(n)
spd= int ( raw_input(' Speed enter '))
window=turtle.Screen();
window.bgcolor("blue");
b= turtle.Turtle()
b.shape("turtle");
b.color("yellow")
b.speed(spd)
i = 1
draw_htree(b,n,i,200)
window.exitonclick()

