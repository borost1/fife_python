
start = int(input("Add meg a kezdoerteket!"))
stop = int(input("Add meg a zaroerteket!"))

res = start

for i, j in enumerate(range(start, stop+1)):
    '''
    i = 0 + 1 = 1. -> j = 4
    i = 1 + 1 = 2. -> j = 5
    ...
    '''

    if (i+1) % 2 == 1:
        print(f"{i+1}. {res} * {j}")
        res *= j
        # res = res * j
    else:
        print(f"{i + 1}. {res} / {j}")
        res /= j
    print(f"{res}")


'''
ke: 4
ze: 8
er = ke = 4
[4,5,6,7,8]
1. 4 * 4 = 16 
2. 16 / 5 = 3.2
3. 3.2 * 6 = 19.2
4. 19.2 / 7
...  
'''

# AZ ELSO N SZAM OSSZEGE
