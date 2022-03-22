def solution(numbers):
    numbers.sort()
    result = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            result.append(numbers[i]+numbers[j])
    return list(set(result))


# 정확성: 77.8

def solution(numbers):
    numbers.sort()
    result = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            result.append(numbers[i]+numbers[j])
    return sorted(list(set(result)))

# 통과!
