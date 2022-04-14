def solution(id_list, report, k):
    report2 = list(set(report))
    dic = {}
    for name in report2:
        key = name.split()[0]
        value = name.split()[1]
        if key not in dic:
            dic[key] = value
        else:
            dic[key] = dic[key] + "," + value
    return dic

#  {"apeach":"muzi,frodo","muzi":"frodo,neo","frodo":"neo"}


   c = []
    for x, y in dic.items():
        c.append(y.split(","))

    result = np.concatenate(c).tolist()
    return result

# ["neo","frodo","muzi","neo","frodo"]


 result = np.concatenate(c).tolist()
    dic_count = {}
    for i in result:
        dic_count[i] = 1 + dic_count.get(i,0)
    return dic_count
     {"neo":2,"frodo":2,"muzi":1}
     {"con":1}


     ------------------------------
import numpy as np
def solution(id_list, report, k):
    report2 = list(set(report))
    dic = {}
    for name in report2:
        key = name.split()[0]
        value = name.split()[1]
        if key not in dic:
            dic[key] = value
        else:
            dic[key] = dic[key] + "," + value


    # {"frodo":"neo","apeach":"muzi,frodo","muzi":"neo,frodo"}

    c = []
    for x, y in dic.items():
        c.append(y.split(","))
    result = np.concatenate(c).tolist()
    # ["neo","frodo","muzi","frodo","neo"] // ["con"]
    dic_count = {}  # {"neo":2,"frodo":2,"muzi":1}   // {"con":1}
    for i in result:
        dic_count[i] = 1 + dic_count.get(i,0)

    for x, y in dic_count.items():
        if y >= k:
            reported_name = x
    else:
        return list(map(int, list(len(id_list)*"0")))

    # 실패.. 4.2 ??!?!?!??

# 다른사람풀이 1

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic_report = {id: [] for id in id_list} # 해당 유저를 신고한 ID
    for i in set(report):
        i = i.split()
        dic_report[i[1]].append(i[0])
    # dic_report {"muzi":["apeach"],"frodo":["apeach","muzi"],"apeach":[],"neo":["muzi","frodo"]}

    for key, value in dic_report.items():
        if len(value) >= k:
            for j in value:
                answer[id_list.index(j)] += 1

    return answer

# 다른사람풀이 2

def solution(id_list, report, k):
    answer = []
    a = list(set(report))
    dictionary2 = {name : 0 for name in id_list}
    dictionary = {name : [] for name in id_list}
    for i in a:
        dictionary[i.split()[1]].append(i.split()[0])

    for i in dictionary:
        if len(dictionary[i]) >= k:
            for j in dictionary[i]:
                dictionary2[j] += 1

    for i in dictionary2:
        answer.append(dictionary2[i])

    return answer
-------------------------------------------------

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic_report = {id: [] for id in id_list}  # 신고한 ID들
    # {"muzi":[],"frodo":[],"apeach":[],"neo":[]}
    report2 = list(set(report))
    for i in report2:
        key = i.split()[0]
        value = i.split()[1]
        dic_report[value].append(key)
    # dic_report {"muzi":["apeach"],"frodo":["apeach","muzi"],"apeach":[],"neo":["muzi","frodo"]}


    for x, y in dic_report.items():
        if len(y) >= k: # "frodo", "neo"가 reported 됨.. 따라서 애네들을 신고한 사람을 count 해주면됨
            dic = []
            for name in y:
                loc = id_list.index(name)  #  # 0,2,0,1
                dic.append(loc)
            print(dic)

--------------------------------------------------------


