###
# https://www.google.com/evaluation/ads/beta/rating/gwt/index.html#raterhistory/starttime=1494514800000&endtime=1496242800000
# 업무 제출 기록을 날짜별로 긁어서 날짜별 총 업무시간을 알아낼 수 있음.
# 10분 이상의 텀이 있는 경우엔 3분으로 계산
###

from datetime import datetime, timedelta

data = []
with open('worktime.txt','r',newline='') as f:
    for i in f:
        try:
            temp = i.split()
            time = datetime.strptime(temp[1], '%H:%M')
            if temp[2] == 'PM' and time.hour != 12:
                time += timedelta(hours=12)
            elif time.hour == 12 and temp[2] == 'AM':
                time -= timedelta(hours=12)
            data.append(time)
        except Exception:
            continue

res = timedelta(minutes=3)
for i in range(len(data)-1):
    # print(data[i], data[i+1])
    #print(data[i] - data[i+1])
    tm = data[i] - data[i+1]
    if tm > timedelta(minutes=10):
        tm = timedelta(minutes=3)

    res += tm
    print(data[i], data[i+1], tm, res)

print(res, res.seconds / 3600)