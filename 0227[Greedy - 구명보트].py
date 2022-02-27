# 최대 2명.. 두개씩 리스트 합을 했을때 합을 리턴 
# 0,1 // 0,2 // 0, 3// >> 1,2 // 1,3 // >> 2,3 
# 1명했을 때.. 합을 리텁.. 

# 1차시도 .. 실패! 
# 2명했을때 limit 넘는것을 삭제해줘야 하는데.. 음 했다가 실패했음
def solution(people, limit):
    answer = 0
    total = 0 
    two = []
    one = []
    for i in range(len(people)):
        for j in range(i+1,len(people)):
            a = people[i]
            b = people[j]
            result = a + b
            two.append(result)             
    for t in range(len(two)):
        if two[t] <= limit:
            answer = answer + 1  
    
    for p in range(len(people)):
        if people[p] <= limit:
            answer = answer + 1
    return answer


# 2차시도 

def solution(people, limit):
    answer = 0   
    lowest = 0
    highest = len(people)-1
    
    people.sort()
    while lowest <= highest:
        if people[lowest] + people[highest] <= limit:
            answer = answer + 1
            lowest = lowest + 1
            highest = highest - 1
        else:
            answer = answer + 1
            highest = highest -1

    
    return answer
        

            
            
            
            