def solution(n):
    binary_num = bin(n)[2:]
    one_count = binary_num.count("1")
    
    while True:
        n = n + 1
        if bin(n)[2:] == one_count:
            answer = n 
            break
    return answer
        





solution(30)
    