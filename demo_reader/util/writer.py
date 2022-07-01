import sys

def main(opener):
    f = open(sys.argv[1], mode ='wt')
    f.write(' '.join(sys.argv[2:]))
    f.close()


    
