import requests
import json
url = 'https://enroll.spbstu.ru/applications-manager/api/v1/admission-list/form?applicationEducationLevel=BACHELOR&directionEducationFormId=2&directionId=863'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }
r = requests.get(url, headers = headers)
with open('test.json', 'w', encoding="utf-8") as output_file:
  output_file.write(r.text)


with open("test.json", "r", encoding="utf-8") as read_file:
    data = json.load(read_file)
b = input('приоритет 1 или 0(любой)')
k = 1
with open('данные.txt', 'w', encoding="utf-8") as write_file:
    data['list'] = sorted(data['list'], key=lambda x: x['fullScore'], reverse=True)
    for i in data['list']:
        if b == 0:
            write_file.write('Снилс' + ' ' + str(i['userSnils']) + '\n')
            write_file.write("Приоритет" + ' ' + str(i['priority']) + '\n')
            write_file.write("Сумма" +' ' + str(i['fullScore'])+ '\n')
            for j in i['subjects']:
                write_file.write('{}:{}'.format(j['title'], j['score'])+ '\n')
            write_file.write(''.join(['<З' for x in range(15)]) + '\n')
        else:
            if i['priority'] == 1:
                if i['userSnils'] == '167-586-447 25':
                    print(k)
                write_file.write(str(k)+'\n')
                write_file.write('Снилс' + ' ' + str(i['userSnils']) + '\n')
                write_file.write("Сумма" + ' ' + str(i['fullScore']) + '\n')
                write_file.write(''.join(['<З' for x in range(15)]) + '\n')
                k+=1
    print(data['log']['datetime'])