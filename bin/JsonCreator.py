import simplejson as json

#This python code breaks the data into json format of date,time,name,day,msg line by line
def CreateJson(raw_path , json_path):
    file = open(raw_path, 'r', encoding='utf8', errors='ignore')
    file3 = open(json_path, 'w', encoding='utf8', errors='ignore')

    i = 1

    date = ''
    Date = ''
    day = 1
    JSON = {}
    for z in file:
        # print(z[:21])
        str = ''
        Date = ''

        for letters in z:
            if letters == '-' and ',' in str and str[2] == '/' and str[5] == '/' :
                for let in str:
                    if let == ',':
                        if Date != date:
                            # print('date',date,"Date",Date)
                            date = Date
                            print("\t\tDAY ", day, "     ", Date)
                            day = day + 1
                    else:
                        Date = Date + let

                try:
                    TimeMsg = z[z.index(',') + 2:]
                    time = TimeMsg[:TimeMsg.index('m') + 1]

                except:
                    print("xxxxxx Some debugging Needed", z)
                    break
                try:
                    st = TimeMsg.index('-')
                    end = TimeMsg[3:].index(':')
                    name = TimeMsg[st + 2:end + 3]
                    msg = TimeMsg[end + 5:TimeMsg.index('\n')]
                except:
                    print("continuing")
                    continue
                # print(name,'////',msg,'////',time,'////',day,'////',Date)
                dict = {'type': 'msg', 'day': day, 'date': date, 'time': time, 'name': name, 'msg': msg}
                JSON[i] = dict
                i = i + 1
                # print(dict)
                # print(TimeMsg)
                break
            else:
                str = str + letters
            if letters == '\n':
                # print('XXX',str,end='')
                dict1 = {'type': 'extra', 'extra': str}
                # print(dict1)
                JSON[i] = dict1
                i = i + 1

    print(JSON)
    json.dump(JSON, file3, indent=4)