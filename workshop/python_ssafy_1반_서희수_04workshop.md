### 문제 1

```python
n = 5
m = 9

k = (n*"*"+"\n")

print(k*m)
```



### 문제 2. 다음 딕셔너리에서 평균 점수를 출력하시오.

```python
student = {'python':80, 'algorithm':99, 'django': 89, 'flask' : 83}
k = 0
for val in student.values():
    k = k+val

print(k/len(student))
```



### 문제 3. 다음은 학생들의 혈액형에 대한 데이터이다. for문을 이용하여 각 혈액형별 학생수의 합계를 구하시오.

```python
blood = ['A','B','O','A','B','A','AB','AB','O','A','O','AB','O']
a, b, o, ab = 0,0,0,0

for i in blood:
    if i == "A":
        a +=1
    elif i == "B":
        b += 1
    elif i == "O":
        o +=1
    elif i == "AB":
        ab +=1

print(f"""
A형은 {a}명이고
B형은 {b}명이고
O형은 {o}명이고
AB형은 {ab}명입니다""")
 
```



