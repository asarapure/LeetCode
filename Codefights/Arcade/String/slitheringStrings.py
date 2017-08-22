__author__ = 'asarapure'

def catWalk(code):
    return " ".join(code.split()) #When split is used without parameters, it splits on whitespace.

#Remove multiple whitespaces with a single one.
line = "def      m   e  gaDifficu     ltFun        ction(x):"
print(catWalk(line))

#For the purpose of mapping a letter to another, use maketrans. Then input word in translate method.
def permutationCipher(password, key):
    table = str.maketrans('abcdefghijklmnopqrstuvwxyz',key)
    return password.translate(table)

