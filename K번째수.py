# i-1, j, k-1


def solution(array, commands):
    answer = []
    for i in commands:
        data = ",".join(map(str, i))
        a, b, c = data.split(",")
        a = int(a)
        b = int(b)
        c = int(c)
        pre2 = array[a-1:b]
        pre2.sort()
        pre3 = pre2[c-1]
        answer.append(pre3)
    return answer

# 통과!


# 다른 사람 풀이 1
def solution(array, commands):
    answer = []
    for c in commands:
        i, j, k = c
        array2 = sorted(array[i-1:j])[k-1]
        answer.append(array2)
    return answer


# 다른 사람풀이 2

def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

