from time import sleep

print("Hello, welcome to Rohit's calculator\n")
sleep(2.0)
print('Before we start please make sure, if you select subtraction or division your 1st number')
print('should be greater than your 2nd number\n')
print('No errors will occur if you enter incorrectly, just your answer would be incorrect\n')
sleep(10)

first = input('Enter 1st number: ')

second =input('Enter 2nd number: ')

error = True

def calculate():
    print("\nEnter '+' to add first and second number")
    print("Enter '-' to subtract first and second number")
    print("Enter '*' to multiply first and second number")
    print("Enter '/' to divide first and second number")

    sign = input('\nOperator: ')

    if(sign == '+'):
        result = float(first) + float(second)
        print("\nThe sum of",first,"and",second,"is:",result)
        return False
    elif(sign == '-'):
        result = float(first) - float(second)
        print("\nThe difference of",first,"and",second,"is:")
        return False
    elif(sign == '*'):
        result = float(first) * float(second)
        print("\nThe product of",first,"and",second,"is:",result)
        return False
    elif(sign == '/'):
        result = float(first) / float(second)
        print("\nThe fraction of",first,"and",second,"is:",result)
        return False
    else:
        print("Invalid selection!!")
        sleep(2.0)
        print("Please check the characters and type correctly\n")
        sleep(2.0)
        return True
    
    return error
        
while error:
   error = calculate()

sleep(1.5)
print("\nHope you got your answer!!")
print("Thanks for using calculator")
