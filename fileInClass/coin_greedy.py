def coinGreedy(money, cash_type):
    def coinGreedyRecursive(money, cash_type, res, idx):
        if idx >= len(cash_type): #화폐 다 사용 시 종료
            return res
        # dvmd[0] : 현재 선택한 화폐로 지불한 갯수
        # dvmd[1] : 지불 후 남은 잔액(앞으로 마저 지불해야 할 금액)
        dvmd = divmod(money, cash_type[idx])
        res[cash_type[idx]] = dvmd[0]
        return coinGreedyRecursive(dvmd[1], cash_type, res, idx+1)

    cash_type.sort(reverse=True)  # 화폐 내림차순 정렬
    return coinGreedyRecursive(money,cash_type,{},0)

def coinGreedy(money, cash_type):
    cash_type.sort(reverse=True)  # 화폐 내림차순 정렬
    remain = money #각 단계 수행 후 지불해야 할 잔액 저장
    res = {}    #화폐별 사용 매수 저장
    for cash in cash_type:  #큰 화폐부터 순차 실행
        # dvmd[0] : 현재 선택한 화폐로 지불한 갯수
        # dvmd[1] : 지불 후 남은 잔액(앞으로 마저 지불해야 할 금액)
        dvmd = divmod(remain,cash)
        res[cash] = dvmd[0]
        remain = dvmd[1]
    return res

money = int(input('액수입력 : '))
cash_type = [int(x) for x in input('화폐단위를 입력하세요 : ').split(' ')]
res = coinGreedy(money,cash_type)
for key in res:
    print('{0}원 : {1}개'.format(key,res[key]))


# def coinGreedyRecursive(remain, cash_type, res):
#     if cash_type == []:
#         return res
#     res_in_this_level = divmod(remain,cash_type[0])
#     res[cash_type[0]] = res_in_this_level[0]
#     del cash_type[0]
#     return coinGreedyRecursive(res_in_this_level[1],cash_type,res)
