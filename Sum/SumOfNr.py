try:
    num1 = int(input("Vendos nr 1 : "))
    num2 = int(input("Vendos nr 2 : "))
    num3 = int(input("Vendos nr 3 : "))
except ValueError:
    raise Exception('The variable is not a number')

sum1 =  num1 + num2 + num3



print(sum1)