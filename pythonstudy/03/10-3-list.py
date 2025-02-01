a=["고양이","강아지"]
b=["코끼리", "사자"]
c=a+b
d=[1]*5
e=[[1]]*4
f=[a, "장성준"]*2
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
A=[1,2,3]
B=[1,2,3]
C=[4,5,6]
A.append(C)
B.extend(C)
print(f"A의 결과: {A}")
print(f"B의 결과: {B}")