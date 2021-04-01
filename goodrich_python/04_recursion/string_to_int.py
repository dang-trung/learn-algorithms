def string_to_int(str):
    if len(str) == 1:
        return ord(str) - ord('0')
    else:
        return string_to_int(str[-1]) + string_to_int(str[:-1]) * 10
    
if __name__=='__main__':
    print(string_to_int('1231'))