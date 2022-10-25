math_ops = {
    "add": lambda a,b: a + b,
    "subtract": lambda a,b: a - b,
    "multiply": lambda a,b: a * b,
    "divide": lambda a,b: a / b,
    "exponent": lambda a,b: a ** b
}

def is_math_op(op_name):
    return op_name in math_ops

