x = "awesome"

def myfunc():
  global x
  x = "very good"

myfunc()

print("Python is " + x)