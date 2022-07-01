import sys

DIGIT_MAP ={
    'zero' : '0',
    'one'  : '1',
    'two'  : '2',
    'three': '3',
    'four' : '4',
    'five' : '5',
    'six'  : '6',
    'seven': '7',
    'eight': '8',
    'nine' : '9', 
}

def convert(s):
    x = -1
    try:
        number = ''
        for token in s:
            number+=DIGIT_MAP[token]
        
        x = int(number)
        print(f"Conversion succeede! x={x}")
    
    except (KeyError, TypeError) as e:
        print(f"Conversion failed : {e!r}",file=sys.stderr)
    
    return x



if __name__ == '__main__':
    convert("one two three ii".split())
    