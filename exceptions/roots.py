
import sys



def sqrt(x):

    if x < 0:
        raise ValueError("Cannot compute a square root of "
                         f" negative number {x}")
    guess = x
    i = 0
    while guess * guess !=x and i<20:
        guess = (guess + x / guess) / 2.0
        i+=1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ValueError as e:
        print (e, file=sys.stderr)



if __name__ == '__main__':
    main()

"""
IndexError      : Index out of range
ValueError      : like int('A')
KeyError        : A lookup in a mapping failed


LBYL            : Look before you leap
EAFP            : Easier to ask forgiveness then permission

"""