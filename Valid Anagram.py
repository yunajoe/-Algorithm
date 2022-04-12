


from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = Counter(s)
        b = Counter(t)
        if a.items() == b.items():
            return True
        return False
# Success

# other solution...


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic_s, dic_t = {}, {}


        # 문자열의 길이가 같다면? i가 도 같을것임
        # dic를 만들어줌
        for i in range(len(s)):
            dic_s[s[i]] = 1 + dic_s.get(s[i],0)
            dic_t[t[i]] = 1 + dic_t.get(t[i],0)


        for s in dic_s:
            if dic_s[s] != dic_t.get(s,0):
                return False
        return True



'''
   for s in dic_s:
        if dic_s[s] != dic_t.get(s,0):  # key 가 없다면 0 을 하니까.. 어찌된듯 value값만 비교해면 됨.
            return False
        return True  # 정답이 아닌 이유가 dic_s와 dic_t의 정렬이 서로 다르기 떄문에, 첫번째 key값만 달라도 False로 끝남.

'''