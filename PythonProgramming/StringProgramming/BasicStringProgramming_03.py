print('******* format method *******')

word = 'python'
myword = 'I know {}'.format(word)
print(myword)

line = 'I love {} {} {}'.format('python','java','C')
print(line)
#Index
line = 'I love {2} {0} {1}'.format('python','java','C')
print(line)
#key
line = 'I love {p} {j} {c}'.format(p='python', j='java', c='C')
print(line)