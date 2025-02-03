first = input("enput first number : ")
operator = input("enter operater (+,-,*,/,%) : ")
second = input("enter secomd number : ")

first = int(first)
second = int(second)

if operator == "+" :
   print(first + second)
elif operator == "-" :
   print(first - second)
elif operator == "*" :
   print(first * second)
elif operator == "/" :
   print(first / second)  
elif operator == "%" :
  print(first % second)    
else:
   print("Invalid operation")