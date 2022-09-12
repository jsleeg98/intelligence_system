# 언어의 종류
## compile 언어
- C
- C++
## interpreter 언어
- Python

# 리스트
```commandline
a = [1, 4, 5, 6, 8]
```
* len(a) : 리스트 a의 길이 : 5
* print(a[0]) : 첫번째 원소의 값 : 1
* a[0:2] : 0부터 1까지 원소 : 1, 4

# 딕셔너리
```commandline
me = {'height' : 180}
```
* me['height'] : key가 'height'인 것의 value : 180
* me['weight] = 70 : key 'weight'를 70으로 설정

# bool 자료형
* hungry = True : hungry에 참 할당

# if 문
```commandline
hungry = True
if hungry:
    print('I'm hungry')
else:
    print('I'm not hungry')
```

# for 문
```commandline
for i in [1, 2, 3]:
    print(i)
```

# 함수
```commandline
def hello():
    print('hello world')
```

# 클래스
* 나만의 일반적 자료형 + 메소드
* OOP(Object Oriented Program) 객체지향
```commandline
class Man:
    def __init__(self, name):
        self.name = name
        print('initialized!')
    def hello(self):
        print('hello' + self.name + '!')
    def bye(self):
        print('bye' + self.name + '!')

       
m = Man('David')
m.hello()
m.bye()
```

# numpy
```commandline
import numpy as np
a = np.array([1.0, 2.0, 3.0])
b = np.array([3.0, 4.0, 5.0])

# element-wise 계산
print(a + b)
print(a * b)

a2 = np.array([[1.0, 2.0], [3.0, 4.0]])
print(a2.shape)  # 차원
print(a2.dtype)  # 값의 자료형
```

## broadcast
* shape이 다른 것 끼리의 연산에서 shape을 맞추어 자동으로 계산되는 것
```commandline
A = np.array([[1, 2],[3, 4]])
B = np.array([10])
print(A + B)  # 가능
```

