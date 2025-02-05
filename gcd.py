
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
#get input numbers from the math trying to crack gcd.
num1 = int(input("enter an integer value:"))
num2 = int(input("enter another integer value:"))
result = gcd(num1, num2)
#Calaculate the gcd and print your result.
print("The greatest common divisor of",num1 ,"and",num2 ,"is", result)