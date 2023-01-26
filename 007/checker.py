def check_menu(num, lst):

    if len(num) == 1 and num.isdigit() is True and num in lst:
        return True
        
    return False
