print('5명의 성적을 입력하시오')
sum = 0
for i in range(5):
    sum += int(input(f'성적 {i+1} : '))
print(f'합계 : {sum}')
print(f'평균 : {sum/5}')