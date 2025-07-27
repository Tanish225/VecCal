#utils/vector_calculus.py
#SymPy logic
from sympy.vector import CoordSys3D
from sympy.vector import gradient, divergence, curl
from sympy import sympify

def compute(operation, expression):
    R = CoordSys3D('R')
    try:
        expr = sympify(expression, locals={'R': R})
    except Exception as e:
        return f"Invalid expression: {str(e)}"
    try:
        if operation == 'gradient':
            return str(gradient(expr, R))
        elif operation == 'divergence':
            return str(divergence(expr, R))
        elif operation == 'curl':
            return str(curl(expr, R))
        else:
            return "Invalid operation"
    except Exception as e:
        return f"Computation error : {str(e)}"
