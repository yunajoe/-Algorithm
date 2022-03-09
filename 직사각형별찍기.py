a, b = map(int, input().strip().split(' '))
result = (a * b) + 1

for i in range(1,result, a):
    print(a * "*")
    
# 통과!! 

# 다른 사람 풀이   
a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*', end='')
    print('')
    
    
# 다른 사람 풀이 2   
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)