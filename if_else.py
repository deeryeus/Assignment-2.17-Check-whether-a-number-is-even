x = 2

if (x > 3):
    print('BIG')
else: 
    print('SMALL')

# doesn't check for exactly 0
def sign(x):
    if (x > 0):
        print('POSITIVE')
    else: 
        print('NEGATIVE')
    
sign(-2)

def sign2(x):
    if x == 0:
        print('ZERO')
    elif x > 0:
        print('POSITIVE')
    else:
        print('NEGATIVE')

sign2(0)


