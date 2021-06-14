import requests, json, xlwt  # 导入http请求、json格式化、excel文件内容读取模块

# 拼装广告投放请求
def template_single(result):
    url = "https://api-grows.qschou.com/api/grow/v2/template_single"
    payload = {
        "qsc_uuid": "%s",
        "product": "qsc_eb",
        "scene": 60
    }
    data = json.dumps(payload) % result  # 替换
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=data).json()
    jsonStr = json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
    return jsonStr

# 读文件、写文件
def txtFn():
    book = xlwt.Workbook()  # 创建workbook 对象
    sheet = book.add_sheet('sheet1')  # 创建工作表sheet
    sheet.write(0, 0, 'uuid')   # 往表中写内容,(行, 列, 内容)
    sheet.write(0, 1, '结果')
    with open('serious_uid.txt', 'a+') as f:  # 使用 with open（） as 读写文件
        f.seek(0)  # 移动文件读取指针到指定位置
        n = 1
        for i in f.readlines():  # 依次读取每行
            data = i.replace('\n', '').strip()
            sheet.write(n, 0, data)
            k = template_single(data)
            sheet.write(n, 1, k)  # 写入返回
            n += 1
        book.save('template_single.xls')


if __name__ == '__main__':
    txtFn()
