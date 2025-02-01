my_list=[1,2,3]
l1,l2,l3=my_list
print(f"리스트언패킹: {l1}, {l2}, {l3}")

my_tuple=(1,2,3,(4,5,6))
t1,t2,t3,t4=my_tuple
print(f"튜플언패킹: {t1},{t2},{t3},{t4}")
t1,t2,t3,(t4,t5,t6)=my_tuple
print(f"튜플언패킹: {t1},{t2},{t3},{t4},{t5},{t6}")

a,b=100,200
print(f"a: {a}, b: {b}")
a,b=b,a
print(f"a: {a}, b: {b}")