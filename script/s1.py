import requests, json, xlwt  # 导入模块

# 拼装大数据模型请求
def bigdata_apl(result):
    url = "http://java-bigdata-algo-model-inner.qschou.com:9001/qsc/services/apl"
    payload = {
        "params": {
            "uuid": "%s",
            "biz": "qsc_eb",
            "virtadp": "bigdata_rec_bx_liebiao",
            "adp": "60",
            "channel": "orion"
        }
    }
    data = json.dumps(payload)%result
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data = data).json()
    jsonStr = json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
    return jsonStr

# 读文件、写文件
def txtFn():
    num = []
    book = xlwt.Workbook()  # 创建workbook 对象
    sheet = book.add_sheet('sheet1')  # 创建工作表sheet
    sheet.write(0, 0, 'uuid')   # 往表中写内容,(行, 列, 内容)
    sheet.write(0, 1, '结果')
    with open('serious_uid.txt', 'a+') as f:  # 使用 with open（） as 读写文件
        f.seek(0)  # 移动文件读取指针到指定位置
        for i in f.readlines():
            data = i.replace('\n', '')
            num.append(data)
    i = 1
    for j in num:
        print(i, j)
        sheet.write(i, 0, j)
        k = bigdata_apl(j)
        sheet.write(i, 1, k)  # 写入返回
        i += 1
    book.save('serious_uid.xls')

txtFn()


