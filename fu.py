def div (number, by):
        return number/by

def X (number, by):
        return number*by

def minus (number, by):
        return number - by

def plus (number, by):
        return number+ by

    

numbers=["1:Addition","2:Subtraction","3:Multiplication","4:Division"]

for x in numbers:
          print(x)

fuck =input("print the number of what the fuck do you want please: ")

a=int(input("enter first number :"))
b=int(input("enter second number :"))

result=None
if fuck == "1":
    result= plus(a,b)
        
elif fuck == "2":
    result= minus(a,b)
        

elif fuck == "3":
    result= X(a,b)
       
    
elif fuck == "4":
    result= div(a,b)
else:
    result="كل خرا"
                
         
print(result)
print("thanks for trying وخرا بشرفك")
