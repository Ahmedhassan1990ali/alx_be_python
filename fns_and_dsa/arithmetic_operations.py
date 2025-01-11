def perform_operation(num1, num2, operation):
    match operation:
        case "add": return num1 + num2
        case "subtract": return num1 - num2
        case "multiply": return num1 * num2
        case "divide":
            try: return num1 / num2
            except ZeroDivisionError : return "cannot divide by zero"
        case _: 
            if operation == "add":
                pass
            elif num2 == 0:
                pass
            else: return "Unknown operartion"