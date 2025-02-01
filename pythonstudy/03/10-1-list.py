names=["장성준", "유다민", "김우영"]
a=names[0]
b=names[-1]
c=names[1:]
d=names[:-1]
e=names[0:2]
f=names[0:1]
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))
print(f,type(f))
print(f"변경전:, {names}")
names[0]="나서은"
names[1]="이서영"
names[2]="이서현"
print(f"변경후:, {names}")