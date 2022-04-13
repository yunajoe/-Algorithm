class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sorted with len(s)
        new = sorted(strs, key=len)
        first = len(new[0]) # 4
        result = []
        for x in new:
            each = list(x)
            for i in range(first):
                result.append(each[i])
        dic = {}
        for x in result:
            dic[x] = 1 + dic.get(x,0)

        answer=""
        for x, y in dic.items():
            if y == len(strs):
                answer = answer + x
        return answer

# 81 / 123 test cases passed.

'''
["cir","car"]
"cr" 이라고 output이 나왔는데
답은 c이다.

연속적인 것을 생각하지 못하고, 그냥 value값이 len(strs) 와 같은것만 생각했다..

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key = lambda x: len(x))
        first = len(strs[0])
        for i in range(first):
            for j in range(1,len(strs)):
                if strs[0][i] != strs[j][i]:
                    return strs[0][:i]
        return strs[0]


