# 리스트안에 0번째 값을 지정..
# 그 값이 리스트의 1번째 값과 같은지 비교..
# 포함이 되어 있음 False
# 포함되어 있지 않으면 True..

# 1차시도 실패!
def solution(phone_book):
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i].startswith(phone_book[j]):
                return False
            if phone_book[j].startswith(phone_book[i]):
                return False
    return True

# 2차시도

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        # print(phone_book[i+1])
        # i >> 0, 1
        # phone_book[i] >> 	119, 1195524421
        # phone_book[i+1] >> 	1195524421, 97674223
        num = len(phone_book[i])
        if phone_book[i] in phone_book[i + 1][:num]:
            return False
    return True


