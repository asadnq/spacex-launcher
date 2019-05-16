arr = ['pro', 'gram', 'merit', 'program', 'it', 'programmer']

"""def matchInput(arg):
    result = []
    for letter in arg:
        check = ''
        for i in arr:
            if(check == i):
                print(i)
        check += letter
    return result"""


def match_input(arg):
    result = []
    current_check = ""
    check = ""
    for letter in arg:
        check += letter
        current_check += letter
        for i in arr:
            if(current_check == i):
                result.append(i)
                current_check = ""
                print(current_check)
        print(current_check)
    return result


print(match_input('programmerit'))