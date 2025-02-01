age=22
name="장성준"
weigh=82.3
number=12
a="제 성은 %c입니다"%name[0]
b="제 이름은 %s입니다"%name[1:3]
c="제 몸무게는 %f입니다"%weigh
d="제 나이는 %d입니다"%age
e="십진수%d는 8진수로 %o입니다"%(number, number)
f="십진수%d는 16진수로 %x입니다"%(number, number)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)