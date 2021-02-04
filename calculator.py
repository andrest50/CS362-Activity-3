def addition(a, b):
    try:
        return round(a + b, 2)
    except:
        return -1

def subtraction(a, b):
    try:
        return round(a - b, 2)
    except:
        return -1

def multiplication(a, b):
    try:
        return round(a * b, 2)
    except:
        return -1

def division(a, b):
    try:
        return round(a / b, 2)
    except:
        return -1