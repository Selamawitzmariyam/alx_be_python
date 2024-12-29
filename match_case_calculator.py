num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
operations = input("Choose the operation (+, -, *, /):")
match operations:
    case "+":
        result = num1 + num2
        print("The result is",result)
    case "-":
       result = num1 - num2
       print("The result is",result)
    case "*":
       result = num1  * num2
       print("The result is",result)
    case "/":
       if num2 != 0:
        result = num1 / num2
        print("The result is",result) 
       else :
        print("can't divided by zero")
    case _:
        print("can't divided by zero")
        