from Stations import stations
from Citys import citys
# import time
from datetime import date, datetime, timedelta
import re

citys.get_citysAll(citys)
print('-' * 55)
# stations.findStation("2018-02-12","温州","杭州")
isright_train_date = isright_from_station = isright_to_station = False
while True:
    time_now = datetime.now()
    time_strat = time_now.strftime("%Y-%m-%d")
    time_end = (time_now + timedelta(days=29)).strftime("%Y-%m-%d")
    print('日期范围【{}---{}】，如：{}'.format(time_strat, time_end, time_strat))
    train_date = input('请输入出发日期：')
    try:
        temp_date = datetime.strptime(train_date, "%Y-%m-%d").strftime("%Y-%m-%d")
        if temp_date > time_strat and temp_date < time_end:
            train_date = temp_date
            isright_train_date = True
            break
        else:
            print('日期不在有效范围内')
            print('-' * 55)
    except ValueError as e:
        print('你这个输的是什么玩意儿?')
        print('-' * 55)

while True:
    from_station = input('请输入出发地：')
    re_from_station_back = citys.get_NameToStation(from_station)
    # print(re_from_station_back)
    if re_from_station_back:
        isright_from_station = True
        break
    print('未找到' + from_station + ',请重新输入!')

while True:
    to_station = input('请输入到达站：')
    re_to_station_back = citys.get_NameToStation(to_station)
    # print(re_from_station_back)
    if re_to_station_back:
        isright_to_station = True
        break
    print('未找到' + to_station + ',请重新输入!')

if isright_train_date and isright_from_station and isright_to_station:
    stations.findStation(train_date, from_station, to_station)
