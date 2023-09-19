def MyGen(): 
    n = 1 
    print('This is printed first') # Generator function contains yield statements yield 1

    n += 2
    print('This is printed second')
    yield n

    n += 2
    print('This is printed at third')
    yield n
    
    n += 2
    print('This is printed at fourth')
    yield n
    
    n += 2
    print('This is printed at last')
    yield n
