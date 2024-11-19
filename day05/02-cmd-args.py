import sys

def add(num1,num2):
    a = num1 + num2
    return a

def sub(num1,num2):
    s = num1 - num2
    return s

def mul(num1,num2):
    m = num1 * num2
    return m

def div(num1,num2):
    d = num1 / num2
    return d

num1 = int(sys.argv[1])
operator = sys.argv[2]
num2 = int(sys.argv[3])

if operator == "add":
    output = add(num1,num2)

elif operator == "sub":
    output = sub(num1,num2)

elif operator == "mul":
    output = mul(num1,num2)

elif operator == "div":
    output = div(num1,num2)

else:
    output = "Invalid Operator"

print(output)