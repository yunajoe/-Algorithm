def solution(numbers):    
    new = list(map(str, numbers))
    new.sort(key=lambda x: x*3, reverse = True)
    answer = str(int("".join(new)))
    return answer