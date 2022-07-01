f = open("wasteland.txt", mode="wt", encoding="utf-8")
# mode [r│w│a] selector [b│t]
f.write("Hello")
f.write("World")
f.close()

g = open("wasteland.txt", mode="rt", encoding="utf-8")
print(g.read(4))
print(g.read())
g.seek(0)
print(g.readline())
g.seek(0)
print(g.readlines())
g.close()


f = open("wasteland.txt", mode="at", encoding="utf-8")
f.close()

with open("wasteland.txt", mode="rt", encoding="utf-8") as f:
    print ([line.strip() for line in f])
