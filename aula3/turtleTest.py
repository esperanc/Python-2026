import piplite
await piplite.install('jupyturtle', deps=False)
await piplite.install('ipycanvas') 

from jupyturtle import *

make_turtle(height=300)
for i in range(4):
   forward(100)
   left(90)


make_turtle(height=300)
for i in range(20):
    forward (50+i*10)
    left (90)



