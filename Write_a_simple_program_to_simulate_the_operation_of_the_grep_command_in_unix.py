import re

count = 0
fhand= input('do input a file name:\n')
fname = open(fhand)

scout = input(str('input what you are searching for\n'))
for check in fname:
       check = check.rstrip()
       if re.findall(scout,check) != []:
           count +=1
print (fname, "had", str(count), "that matched", scout)
     