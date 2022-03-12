def solution(s):
    if s.startswith("-"):
        s = s.split("-")[1]
        answer = "-" + s
        return int(answer)
    return int(s)


