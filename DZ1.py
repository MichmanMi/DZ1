x=input("Введите значение: ")
if x.isnumeric():
  numder=int(x)
  print(type(numder))
elif x in "False":
  false = bool(x)
  print(type(false))
elif x in "True":
  true = bool(x)
  print(type(true))
else:
 print(type(x)) 