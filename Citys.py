import requests
import re


class citys:
    def get_citysAll(self):
        url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9047'
        print('正在获取市级信息...')
        rqs = requests.get(url)
        reStr = r'(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|(.*?)@'
        reBack = re.findall(reStr, rqs.text.replace("var station_names =\'@", ''))
        global dict_Name_Station
        dict_Name_Station = {}
        for i in reBack:
            dict_Name_Station[i[1]] = {'A1': i[0], 'Num': int(i[5]), 'Station': i[2], 'Name_Suo': i[3],
                                       'Name_Jian': i[4]}
        global dict_Station_Name
        dict_Station_Name = {}
        for i in reBack:
            dict_Station_Name[i[2]] = {'A1': i[0], 'Num': int(i[5]), 'Name': i[1], 'Name_Suo': i[3], 'Name_Jian': i[4]}
        print('市级信息获取完毕!')

    def get_NameToStation(name):
        try:
            return dict_Name_Station[name]['Station']
        except KeyError as e:
            return

    def get_StationToName(station):
        try:
            return dict_Station_Name[station]['Name']
        except KeyError as e:
            return


if __name__ == '__main__':  # print('error Timeout')

    print(citys.get_NameToStation('w州'))
