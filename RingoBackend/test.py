f = open("req.txt", "w")
g = open("requirements.txt", 'r')

for line in g.readlines():
   h = line.split()
   t = '=='.join(h)
   t += '\n'
   f.write(t)
f.close()
g.close()
