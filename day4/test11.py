pin = input("PIN: ")
if pin == "":
    print("Invalid PIN.")
else:
    is_valid_length = False
    is_all_digits = True
    digit_count = 0
    for char in pin:
        if '0' <= char <= '9':
            digit_count += 1
        else:
            is_all_digits = False
            break
    if " " not in pin: 
        if is_all_digits:
            if digit_count == 4 or digit_count == 6:
                is_valid_length = True
    if is_valid_length:
        print("Valid PIN.")
    else:
        print("Invalid PIN.")