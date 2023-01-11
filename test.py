with open('requirements_copy.txt', 'r') as f:
   with open('requirements.txt', 'a') as g:
      for l in f.readlines():
         list1 = l.split()
         list2 = list1[:2]
         str1 = list1[0] + "==" +  list1[1] + '\n'
         g.write(str1)
