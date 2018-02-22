import requests
from Citys import citys
from prettytable import PrettyTable


class stations:
    def findStation(traindate, fromstation, tostation):
        train_date = traindate
        from_station = citys.get_NameToStation(fromstation)
        to_station = citys.get_NameToStation(tostation)
        payload = {
            'leftTicketDTO.train_date': train_date,
            'leftTicketDTO.from_station': from_station,
            'leftTicketDTO.to_station': to_station,
            'purpose_codes': 'ADULT'
        }
        # print(payload)
        url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ'
        print('正在搜索车次...')
        reqs = requests.get(url, params=payload)  # , params=payload
        print('车次搜索完成!')
        html_result = reqs.text
        c = html_result.split('|')
        x = PrettyTable(
            ['序号', '车次', '出发站-到达站', '出发时间-到达时间', '历时', '商务座', '一等座', '二等座', '高级软卧', '软卧', '动卧', '硬卧', '软座', '硬座',
             '无座',
             '其他', '备注'])
        for i in range(0, int(len(c) / 36)):
            way = i * 36
            table_XuHao = i + 1
            table_Checi = c[3 + way]
            table_ChufaDaodaZhan = citys.get_StationToName(c[6 + way]) + '-' + citys.get_StationToName(c[7 + way])
            table_ChufaDaodaTime = c[8 + way] + '-' + c[9 + way]
            table_LiShi = c[10 + way]
            table_Site_Shangwu = c[32 + way] if c[32 + way] else '- -'
            table_Site_Yideng = c[31 + way] if c[31 + way] else '- -'
            table_Site_Erdeng = c[30 + way] if c[30 + way] else '- -'
            table_Site_GaojiRuanwo = c[21 + way] if c[21 + way] else '- -'
            table_Site_Ruanwo = c[23 + way] if c[23 + way] else '- -'
            table_Site_Donwo = c[33 + way] if c[33 + way] else '- -'
            table_Site_Yingwo = c[28 + way] if c[28 + way] else '- -'
            table_Site_Ruanzuo = c[24 + way] if c[24 + way] else '- -'
            table_Site_Yingzuo = c[29 + way] if c[29 + way] else '- -'
            table_Site_Wuzuo = c[26 + way] if c[26 + way] else '- -'
            table_Other = c[22 + way] if c[22 + way] else '- -'
            table_Say = c[1 + way]
            table_Canwebuy = c[11 + way]
            x.add_row(
                [table_XuHao, table_Checi, table_ChufaDaodaZhan, table_ChufaDaodaTime, table_LiShi,
                 table_Site_Shangwu,
                 table_Site_Yideng,
                 table_Site_Erdeng, table_Site_GaojiRuanwo, table_Site_Ruanwo, table_Site_Donwo, table_Site_Yingwo,
                 table_Site_Ruanzuo, table_Site_Yingzuo, table_Site_Wuzuo, table_Other, table_Say])

        print('开始导出车次...')
        print(x)
        print('车次获取完毕,任务完成!')




