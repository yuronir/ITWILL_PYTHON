###
# https://global.appen.com/projects/904/users/183302/view_stats?tab=user_reported_time
# 월간 총 업무시간을 그대로 복사한 monthdata.txt를 이용해 월 급여 확인(US달러)
###

sum = 0.0
with open('monthdata.txt', 'r') as f:
    for i in f:
        try:
            time = float(i.split()[6])
            sum += time
        except Exception:
            continue

print(sum)  ## US 달러