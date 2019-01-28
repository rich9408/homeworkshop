### 문제1. List는 for문을 실행하면 모든 요소를 순차적으로 돌면서 반복문을 수행합니다. 임의의 리스트 my_list의 값을 하나씩 출력하는 코드를 아래에 작성하시오.

```python
my_list = [1,2,3,4]
for i in my_list:
    print(i)
```



### 문제 2. 위의 값을 인덱스와 함께 출력하는 코드

```python
my_list = [1,2,2,3,4]
for i in my_list:
    print((my_list.index(i), i))
```



### 문제 3.  다음 반복문을 수행하도록 빈칸을 채워라



```python
# key값
my_dict = {"a":1, "b":2}
for key in my_dict:
    print(key)
    
    
# value값
my_dict = {"a":1, "b":2}
for value in my_dict.values():
    print(value)

    
# key, value값
my_dict = {"a":1, "b":2}
for key,value in my_dict.items():
    print((key, value))    

```



### 문제 4.  result에 저장된 값은?

```python
def my_func(a,b):
    c = a+b
    print(c)
    
result = my_func(1,5)


답 : None
```



