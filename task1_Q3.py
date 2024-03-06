op = input("choose your math operaton (between sum, difference, multiple, divide) :")
num1 = float(input("enter first number :"))
num2 = float(input("enter secend number :"))

if op == "sum" :
    result = num1 + num2 

elif op == "difference" :
    result = num1 - num2

elif op == "multiple" :
    result = num1 * num2

elif op == "divide" :
    result = num1 / num2
    if num2 == 0 :
        result = "Undefined"

print("The result is",result)