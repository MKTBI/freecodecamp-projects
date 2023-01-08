def arithmetic_arranger(problems, show_solution):
    if len(problems) > 5:
        return "Error: Too many problems."
  
    top_row = ""
    bottom_row = ""
    divider = ""
    solution = ""
  
    for problem in problems:
        # Check for correct operator
        if problem[3] != '+' and problem[3] != '-':
            return "Error: Operator must be '+' or '-'."
    
        # Check for non-digit characters in operands
        if not problem[0:3].isdigit() or not problem[4:].isdigit():
            return "Error: Numbers must only contain digits."
    
        # Check for operands with more than 4 digits
        if len(problem[0:3]) > 4 or len(problem[4:]) > 4:
            return "Error: Numbers cannot be more than four digits."
  
        if show_solution:
            for problem in problems:
        # Get operands and operator
                operand1 = int(problem[0:3])
                operator = problem[3]
                operand2 = int(problem[4:])
    
        # Calculate solution
            if operator == '+':
                solution += f"{operand1 + operand2:>4}    "
            elif operator == '-':
                solution += f"{operand1 - operand2:>4}    "
            else:
                solution = ""
    return f"{top_row}\n{bottom_row}\n{divider}\n{solution}"


print(arithmetic_arranger([32 + 8, 1 - 3801, 9999 + 9999, 523 - 49], True))