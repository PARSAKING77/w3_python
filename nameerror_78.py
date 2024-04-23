try:
  print(p)
except NameError:
  print("Variable p is not defined")
except:
  print("Something else went wrong")
