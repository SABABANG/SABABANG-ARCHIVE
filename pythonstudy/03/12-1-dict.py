a={"한국":"서울", "영국":"런던"}
b={"미국":"워싱턴D.C", "독일":"베를린", "영국":"런던"}
print(f"a: {a}")
print(f"b: {b}")

kor=a["한국"]
ger=b["독일"]
eng=a.get("영국")
usa=b.get("미국")
print(f"한국:{kor}, 독일:{ger}, 영국:{eng}, 미국:{usa}")

a.update(b)
print(f"a: {a}")

usa=a.get("미국")
print(f"미국: {usa}")

k=a.get("안정해짐")
print(f"{k}")