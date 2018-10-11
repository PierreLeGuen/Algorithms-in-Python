from tkinter import *
#function  d e f i n i t i o n
def draw_point ( canvas ,  x ,  y ,  color="black" ):
    canvas.create_rectangle (x , y , x , y ,fill =color , width=0)


#window  creation
window = Tk()
#canvas  creation
w = Canvas (window ,  width=200,  height =100)
w. pack ()
#drawing  functions
w. create_line (0,0 ,200 ,100)
w. create_line (0,100 ,200 ,0 ,  fill ="red" )
w. create_rectangle (50 ,  25 ,  150 ,  75 ,  fill ="blue" )
#main loop  to  allow  i nt er ac ti on
draw_point (w,10 ,10)
mainloop ()
