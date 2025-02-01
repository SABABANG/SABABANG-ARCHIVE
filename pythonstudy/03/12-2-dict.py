a={"한국":"서울", "영국":"런던", "프랑스":"파리", 
   "독일":"베를린", "미국":"워싱턴D.C", "몽골":"울란바토르"}
print(f"a: {a}, 갯수: {len(a)}")
del a["미국"]
print(f"a: {a}, 갯수: {len(a)}")
p=a.pop("몽골")
print(a)
print(f"팝업됨: {p}")
a.clear()
print(f"a:{a}, 갯수:{len(a)}, 자료형:{type(a)}")