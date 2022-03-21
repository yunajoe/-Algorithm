#  같은 index 끼리 곱한다

new = []
def solution(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if i == j:
                new.append(a[i] * b[j])
    return sum(new)

# 통과


# 다른 사람풀이 1
def solution(a, b):

    return sum([x*y for x, y in zip(a,b)])



# 다른 사람풀이 2
def solution(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i]*b[i])
    return sum(c)


# 다른 사람풀이 3

solution = lambda x, y: sum(a*b for a, b in zip(x, y))
