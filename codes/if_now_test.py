import datetime
today=datetime.date(2020,5,22)
today_weekday=today.weekday()
if today_weekday < 3:
    print('주말 언제와')
elif today_weekday == 5:
    print('주말 시작!')
elif today_weekday == 4:
    print('하루만 버티자')
else:
    print('주말이다!!!!')