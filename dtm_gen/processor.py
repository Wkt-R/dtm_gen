def validate_input(input_str):
    if not input_str.isdigit() or len(input_str) != 11:
        return False
    return True

def process_input_string(input_str):
    if not validate_input(input_str):
        raise ValueError("Input must be a string of exactly 11 digits")
    
    part1 = input_str[0:2]
    part2 = input_str[2:3]
    part3 = input_str[3:8]
    part4 = input_str[8:11]
    formatted = f"{part1}, {part2}, {part3}, {part4}"
    
    return formatted