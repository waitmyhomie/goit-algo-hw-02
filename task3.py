def check_brackets(expression):
    stack = [] 
    pairs = {'(': ')', '[': ']', '{': '}'}  

    for char in expression:
        if char in pairs:  
            stack.append(char)
        elif char in pairs.values(): 
            if not stack or pairs[stack.pop()] != char:
                return False

    return not stack  

examples = [
    "(a + b) * (c + d)",
    "{[()]}",
    "(a + b] * c)",
    "([)]",
    "(a + b * (c - d))"
]

for expr in examples:
    print(f"'{expr}': {'коректно' if check_brackets(expr) else 'некоректно'}")
