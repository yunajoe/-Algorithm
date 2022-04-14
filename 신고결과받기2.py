def solution(id_list, report, k):
    report2 = list(set(report))
    answer = {name : 0 for name in id_list}
    dic = {name:[] for name in id_list }
    for i in report2:
        report = i.split()[0]
        reported = i.split()[1]
        dic[report] = reported  # {"muzi":"neo","frodo":"neo","apeach":"muzi","neo":[]}
        # 같은 key값일때 value가 나타나지 않음 key값은 하나
        # 따라서  dic[reported].append(report)  이렇게 변경해주면은
        '''
        {"muzi":["apeach"],"frodo":["apeach","muzi"],"apeach":[],"neo":["frodo","muzi"]}

        '''

    return dic


______________________________________________
def solution(id_list, report, k):
    report2 = list(set(report))
    answer = {name : 0 for name in id_list}
    dic = {name:[] for name in id_list }
    for i in report2:
        report = i.split()[0]
        reported = i.split()[1]
        dic[reported].append(report)  # {"muzi":"neo","frodo":"neo","apeach":"muzi","neo":[]}
    # reported 를 key로 놓은 이유는? len(value) > k 를 통해서 정지가 되어 있는 아이디를 찾기 위해서다

    for x, y in dic.items():  # x는 reported y는 report한 사람
        if len(y) >= k:
            for person in y:
                answer[person] = answer[person] + 1

    final = []
    for i in answer.values():
        final.append(i)
    return final


