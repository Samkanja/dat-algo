from unittest import result


def anagramCheck(s1, s2):
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True

s1 = input()
s2 = input()  
result = anagramCheck(s1,s2)
if result:
    print('isValid')
else:
    print('notValid')