'''
Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''

def add_up(lista, k):
    while lista:
        if max(lista) + min(lista) == k:
            return True
        elif max(lista) + min(lista) > k:
            lista.remove(max(lista))
        else:
            lista.remove(min(lista))
    return False

print(add_up([10, 15, 3, 25, 2, 9, 57,0],2))