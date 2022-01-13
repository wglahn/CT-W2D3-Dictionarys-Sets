'''
1) Has a function to calculate the square footage of a house
Reminder of Formula: Length X Width == Area
2) Has a function to calculate the circumference of a circle 
'''

def area(l,w):
    '''
    User submits arguments for length & width.
    Function returns the calculated area.
    '''
    return l*w

def circum(r):
    from math import pi
    '''
    User submits argument for radius.
    Function returns the circumference of a circle for the given radius.
    '''

    return (2 * pi * r) 