""" Collections:
    * Tuple
    * List
    * str """

def setTitle(title, char="*"):
    line = len(title) * char
    print (line)
    print (title)
    print (line, "\n")
    
    

""" Tuples"""
setTitle ("Tuples")
tuple1 = ("Hola", 1, "Mundo")
tuple2 = ((1,2), (3,4))

for i in tuple1:
    print (i)


for i in tuple2:
    print (i[0])

""" Str"""
setTitle ("Strings")
edad = 25
colors = ';'.join(['#45ff23','#2321fa', '#1298a3', str(edad)])
print (colors)

departure, separator, arrival = "London:Edinburgh".partition(':')
print (departure)

text1 = "The age of {0} is {1}".format('Jim', 32)
text2 = "Current position {latitude} {longitude}".format(latitude="40N", longitude="50E")
value = 6 * 4
text3 = f"6 * 4 is {value}"
print (text1, '\n', text2, '\n', text3)


""" Range """
setTitle ("Range")
range(5)
range (0,5)
x = list(range(0,10,2))
print (x)
t = [6, 365, 345,21334, 324231]
for p in enumerate (t):
    print (p)


""" List """
setTitle ("List")
l = [4, -5, 10]
print (l[-1])
s = l[1:3]
print (s)
w = "the quick brown fox jumps".split()
i = w.index("fox")
print (w, "\n", i)

""" Dictionaries """
setTitle ("Dictionaries")

urls = {"plural": "www.plural",
        "google": "www.google",
        }
print (urls["google"])

""" Set """
setTitle ("Sets")
p = {6, 8, 34, 23, 565656}
print(p)
