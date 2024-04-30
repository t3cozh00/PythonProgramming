##8.4 Exercise: Your own module with several parameters

# inspector.py

def testme(input_string):
    if len(input_string) < 6:
        return False
    
    has_letter = False
    has_digit = False
    
    for char in input_string:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True
            
    if has_letter and has_digit:
        return True
    else:
        return False
