#print("Hello World")
y=5
print(y)
t=5
a="Elizabeth"
print(y*t)
print("hi\ngoodbye")
#\n skips a line
x=3
print(x+t)
print(x*t+x-y)
print(str(x)+"Elizabeth")
print(str(x-y*t)+"John")
v1,v2,v3="red","blue","white"
print(v1)
print(str(x)+v1)
print(v1,v2,v3)
colors=["red","blue","white"]
print(colors)
b, c, d = colors
print(d)
print(d+" "+c)
color=["purple",1]
p, i =color
print(p)
print(i)
n=2
print(x+n/y)
print(n,x)
someFloat=14.5
print(type(someFloat))
m=7.2
l=50
print(int(m+l))
v=4j
print(m+v)
f=5j
print(v+f)
import random
print(random.randrange(1,10))
print(random.randrange(1,100)/1.4)
print(random.randrange(1,10)/random.randrange(1,10))
#here we set the range from 1 to 10
r=random.randrange 
print(r(1,10))
print("Pizza is the best food")
print("Halloween is in a couple of day")
greeting="hello world"
print(greeting[2])
Txt="October"
print(Txt[0:4])
print(Txt[1: ])
print(10>9)
print(10==10)
someTxt="Red is my favorite color"
print("blue"in someTxt)
print("blue"not in someTxt)
a=20
b=30
if b < a:
 print("b is greater than a")
else:
 print("b is not greater than a")
print(bool("green"))
print(bool(["Hi",3,"dogs"]))
print(bool({"Hi"}))
def func():
  return True
if not func():
  print('Yes')
else:
  print('No')
