def solution(array, commands):
    answer = ""
    for i in commands:
        each = " ".join(map(str,i))
        a, b, c = each.split(" ")
        result = str(sorted(array[int(a)-1:int(b)])[int(c)-1])
        answer = answer + result
    return list(map(int,answer))


# 합계: 71.4 / 100.0


def solution(array, commands):
    answer = []
    for x in commands:
        result = sorted(array[x[0]-1:x[1]])[x[2]-1]
        answer.append(result)
    return answer
# 통과


# 다른 사람풀이


def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands)
