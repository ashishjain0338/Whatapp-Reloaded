import simplejson as json
from fractions import Fraction
#This python code breaks the data into json format of date,time,name,day,msg line by line
def Diff(first,last):
    hrsf = int(first[:first.index(':')])
    hrss = int(last[:last.index(':')])
    if 'pm' in first:
        hrsf=hrsf+12
    if 'pm' in last:
        hrss = hrss + 12
    minf = int(first[first.index(':')+1:first.index(':')+3])
    mins = int(last[last.index(':') + 1:last.index(':')+3])

    # print(minf,mins)
    if hrss>hrsf:
        hrs=hrss - hrsf
    else:
        hrs = -(hrss - hrsf)
    if (minf>=mins):
        min=minf-mins
    else:
        min=mins - minf
    if(hrs>=1):
        # print("Delayed",first,last)
        return 0
    elif(min>=15):
        return 0
    else:
        return min

def Convert(time):
    hrs = int(time/60)
    if hrs != 0:
        return str(hrs)+"hrs " + str(time % 60) + "min"
    else:
        return str(time % 60) + "min"

def CreateJson(raw_path , json_path):
    file = open(raw_path, 'r', encoding='utf8', errors='ignore')
    file3 = open(json_path, 'w', encoding='utf8', errors='ignore')
    dateformat = False
    i = 1

    date = ''
    Date = ''
    day = 0
    JSON = {}
    for z in file:
        # print(z[:21])
        str = ''
        Date = ''

        for letters in z:
            #z represents line
            if letters == '-' and len(str) > 5 and ',' in str:
                #str represnts the starting string upto date and time
                if '/' in str:
                    for let in str:
                        if let == ',':
                            if Date != date:
                                # print('date',date,"Date",Date)
                                date = Date
                                # print("\t\tDAY ", day+1, "     ", Date)
                                day = day + 1
                        else:
                            Date = Date + let

                    try:
                        TimeMsg = z[z.index(',') + 2:]
                        j=0
                        for l in TimeMsg:
                            if(l=='m' or l == 'M'):
                                break
                            j=j+1
                            time = TimeMsg[:j + 1]
                    except:
                        print("xxxxxx Some debugging Needed", z)
                        break
                    try:
                        st = TimeMsg.index('-')
                        end = TimeMsg[3:].index(':')
                        name = TimeMsg[st + 2:end + 3]
                        msg = TimeMsg[end + 5:TimeMsg.index('\n')]
                        # print(name,'////',msg,'////',time,'////',day,'////',Date)
                        dict = {'type': 'msg', 'day': day, 'date': date, 'time': time, 'name': name, 'msg': msg}
                        if(len(date)!=10):
                            dateformat = True
                        JSON[i] = dict
                        i = i + 1
                        break
                    except:
                        #print("Exception occured")
                        day = day - 1
                else:
                    str = str + letters
            else:
                str = str + letters
            if letters == '\n':
                dict1 = {'type': 'extra', 'extra': str}
                JSON[i] = dict1
                i = i + 1

    json.dump(JSON, file3, indent=4)
    return dateformat

def DateFormat(json_path):
    file = open(json_path, 'r')

    data = json.load(file)
    # print(data)
    i = 1
    JSON = {}
    for dat in data.values():
        if dat['type'] == 'msg':
            date = dat['date']
            month = date[:date.index('/')]
            if len(month) == 1:
                month = '0' + month
            day = date[date.index('/') + 1:date[date.index('/') + 1:].index('/') + date.index('/') + 1]
            if len(day) == 1:
                day = '0' + day

            year = date[date[date.index('/') + 1:].index('/') + date.index('/') + 2:]
            if len(year) == 2:
                year = '20' + year

            DATE = day + '/' + month + '/' + year
            dat['date'] = DATE
            JSON[i] = dat
            i = i + 1
        else:
            dict1 = {'type': 'extra', 'extra': dat['extra']}
            JSON[i] = dict1
            i = i + 1

    # print(JSON)
    file2 = open(json_path, 'w')
    json.dump(JSON, file2, indent=4)

def GetNames(json_path):
    file = open(json_path, 'r')
    data = json.load(file)
    names = []
    for dat in data.values():
        if(dat["type"] == "msg"):
            if(dat['name'] not in names):
                names.append(dat['name'])
        if(len(names) == 2):
            return names

def Summary(json_path,summary_path):
    file2 = open(json_path, 'r')
    file = open(summary_path, 'w')
    data = json.load(file2)
    names = GetNames(json_path)
    first_name = names[0]
    second_name = names[1]
    ash = {
        'name': first_name,
        'ind': {'msg': 0, 'char': 0, 'word': 0, 'lg': ['', '', ''], 'LG': []},
        'extra': {'msg': 0, 'char': 0, 'word': 0, 'lg': ['', '', ''], 'LG': []}
        }
    sim = {
        'name': second_name,
        'ind': {'msg': 0, 'char': 0, 'word': 0, 'lg': ['', '', ''], 'LG': []},
        'extra': {'msg': 0, 'char': 0, 'word': 0, 'lg': ['', '', ''], 'LG': []}
        }
    Sj = True
    for dat in data.values():
        if dat['type'] == 'msg':
            if dat['name'] == first_name:
                ash['ind']['msg'] = ash['ind']['msg'] + 1
                ash['ind']['char'] = ash['ind']['char'] + len(dat['msg'])
                if len(dat['msg']) > len(ash['ind']['lg'][2]):
                    if len(dat['msg']) > len(ash['ind']['lg'][1]):
                        if len(dat['msg']) > len(ash['ind']['lg'][0]):
                            ash['ind']['lg'][2] = ash['ind']['lg'][1]
                            ash['ind']['lg'][1] = ash['ind']['lg'][0]
                            ash['ind']['lg'][0] = dat['msg']
                        else:
                            ash['ind']['lg'][2] = ash['ind']['lg'][1]
                            ash['ind']['lg'][1] = dat['msg']
                    else:
                        ash['ind']['lg'][2] = dat['msg']
                for words in dat['msg']:
                    if words == ' ':
                        ash['ind']['word'] = ash['ind']['word'] + 1
                Sj = False
            else:
                sim['ind']['msg'] = sim['ind']['msg'] + 1
                sim['ind']['char'] = sim['ind']['char'] + len(dat['msg'])
                if len(dat['msg']) > len(sim['ind']['lg'][2]):
                    if len(dat['msg']) > len(sim['ind']['lg'][1]):
                        if len(dat['msg']) > len(sim['ind']['lg'][0]):
                            sim['ind']['lg'][2] = sim['ind']['lg'][1]
                            sim['ind']['lg'][1] = sim['ind']['lg'][0]
                            sim['ind']['lg'][0] = dat['msg']
                        else:
                            sim['ind']['lg'][2] = sim['ind']['lg'][1]
                            sim['ind']['lg'][1] = dat['msg']
                    else:
                        sim['ind']['lg'][2] = dat['msg']
                for words in dat['msg']:
                    if words == ' ':
                        sim['ind']['word'] = sim['ind']['word'] + 1
                Sj = True
        else:
            if Sj:
                sim['extra']['msg'] = sim['extra']['msg'] + 1
                sim['extra']['char'] = sim['extra']['char'] + len(dat['extra'])
                if len(dat['extra']) > len(sim['extra']['lg'][2]):
                    if len(dat['extra']) > len(sim['extra']['lg'][1]):
                        if len(dat['extra']) > len(sim['extra']['lg'][0]):
                            sim['extra']['lg'][2] = sim['extra']['lg'][1]
                            sim['extra']['lg'][1] = sim['extra']['lg'][0]
                            sim['extra']['lg'][0] = dat['extra']
                        else:
                            sim['extra']['lg'][2] = sim['extra']['lg'][1]
                            sim['extra']['lg'][1] = dat['extra']
                    else:
                        sim['extra']['lg'][2] = dat['extra']
                for words in dat['extra']:
                    if words == ' ':
                        sim['extra']['word'] = sim['extra']['word'] + 1
            else:
                ash['extra']['msg'] = ash['extra']['msg'] + 1
                ash['extra']['char'] = ash['extra']['char'] + len(dat['extra'])
                if len(dat['extra']) > len(ash['extra']['lg'][2]):
                    if len(dat['extra']) > len(ash['extra']['lg'][1]):
                        if len(dat['extra']) > len(ash['extra']['lg'][0]):
                            ash['extra']['lg'][2] = ash['extra']['lg'][1]
                            ash['extra']['lg'][1] = ash['extra']['lg'][0]
                            ash['extra']['lg'][0] = dat['extra']
                        else:
                            ash['extra']['lg'][2] = ash['extra']['lg'][1]
                            ash['extra']['lg'][1] = dat['extra']
                    else:
                        ash['extra']['lg'][2] = dat['extra']
                for words in dat['extra']:
                    if words == ' ':
                        ash['extra']['word'] = ash['extra']['word'] + 1
    #Calculating Longest Message details
    for msg in ash['ind']['lg']:
        for dat in data.values():
            if dat['type'] == 'msg':
                if dat['msg'] == msg:
                    ash['ind']['LG'].append(dat)
    for msg in sim['ind']['lg']:
        for dat in data.values():
            if dat['type'] == 'msg':
                if dat['msg'] == msg:
                    sim['ind']['LG'].append(dat)
    for msg in sim['extra']['lg']:
        for dat in data.values():
            if dat['type'] == 'extra':
                if dat['extra'] == msg:
                    sim['extra']['LG'].append(dat)
    for msg in ash['extra']['lg']:
        for dat in data.values():
            if dat['type'] == 'extra':
                if dat['extra'] == msg:
                    ash['extra']['LG'].append(dat)

    #For other Satistics
    if(ash['ind']['msg']):
        ash['ind']['wpm'] = float(ash['ind']['word']) / ash['ind']['msg']
    else:
        ash['ind']['wpm'] = 0
    if(ash['ind']['word']):
        ash['ind']['cpw'] = float(ash['ind']['char']) / ash['ind']['word']
    else:
        ash['ind']['cpw'] = 0
    if(ash['extra']['msg']):
        ash['extra']['wpm'] = float(ash['extra']['word']) / ash['extra']['msg']
    else:
        ash['extra']['wpm'] = 0
    if(ash['extra']['word']):
        ash['extra']['cpw'] = float(ash['extra']['char']) / ash['extra']['word']
    else:
        ash['extra']['cpw'] = 0

    if(sim['ind']['msg']):
        sim['ind']['wpm'] = float(sim['ind']['word']) / sim['ind']['msg']
    else:
        sim['ind']['wpm'] = 0
    if(sim['ind']['word']):
        sim['ind']['cpw'] = float(sim['ind']['char']) / sim['ind']['word']
    else:
        sim['ind']['cpw'] = 0
    if(sim['extra']['msg']):
        sim['extra']['wpm'] = float(sim['extra']['word']) / sim['extra']['msg']
    else:
        sim['extra']['wpm'] = 0
    if(sim['extra']['word']):
        sim['extra']['cpw'] = float(sim['extra']['char']) / sim['extra']['word']
    else:
        sim['extra']['cpw'] = 0
    data = {'ash': ash, 'sim': sim}
    json.dump(data, file, indent=4)


def date(json_path):
    file2 = open(json_path, 'r')
    data = json.load(file2)
    out = []
    for dat in data.values():
        if dat['type'] == 'msg':
            if {'day': dat['day'], "date": dat['date']} not in out:
                out.append({'day': dat['day'], "date": dat['date']})

    day = 0
    stTime = ""
    endTime = ""
    i = 0

    sum = 0
    i = -1
    day = 0
    for dat in data.values():
        if dat['type'] == 'msg':
            if dat['day'] == day:
                sum = sum + Diff(stTime, dat['time'])

                stTime = dat['time']
            else:
                day = dat['day']
                stTime = dat['time']
                i = i + 1
                if (i != 0):
                    out[i - 1]['total_time'] = sum
                sum = 0
    out[i]['total_time'] = sum
    # print(out)
    return out

def Calender(json_path,end_path):
    out=date(json_path)
    # print(out)
    data={}
    outlist=[]
    month=['January','February','March','April','May','June','July','August','September','October','November','December']
    for dict in out:
        flag = 0
        Mnum=dict['date'][3:5]
        Mname=month[int(Mnum)-1]
        day=int(dict['date'][0:2])
        year=dict['date'][6:]
        if len(outlist)!=0:
            for data in outlist:
                if data['month']==Mname and data['year']==year:
                    data['day'].append(day)
                    data['time'].append(dict['total_time'])
                    flag=1
                    break
            if flag!=1:
                outlist.append({'day':[day],'month':Mname,'year':year,'time':[dict['total_time']]})
                flag=0
        else:
            outlist.append({'day': [day], 'month': Mname, 'year': year,'time':[dict['total_time']]})

    for dict in outlist:
        dict['freq']=float(len(dict['day']))/30
        tup=str(Fraction(dict['freq']).limit_denominator())
        if len(dict['day']) >=27:
            dict['status'] = 'Kind of Daily'
        else:
            dict['status']=tup[:tup.index('/')]+' in '+tup[tup.index('/')+1:]+' days.'

        i=0
    for caldata in outlist:
        totaltime=0
        outlist[i]['time_to_read'] = []
        for time in caldata['time']:
            totaltime = totaltime + time
            outlist[i]['time_to_read'].append(Convert(time))
        outlist[i]['avg_time'] = totaltime / float(len(caldata['day']))
        outlist[i]['avg_time_pm'] = totaltime / 30.00
        i=i+1

    file = open(end_path,'w')
    json.dump(outlist,file,indent=4)
    return outlist

def Combine(old_file_path,latest_file_path,end_path):
    file = open(old_file_path, 'r', encoding='utf8', errors='ignore')
    file2 = open(latest_file_path, 'r', encoding='utf8', errors='ignore')
    file4 = open(end_path, 'w', encoding='utf8', errors='ignore')
    data1 = json.load(file)
    data2 = json.load(file2)
    for dat in data2.values():
        if(dat['type'] == 'msg'):
            date_from_terminate = dat['date']
            break

    DATA = {}
    i = 1
    for x in data1.values():
        try:
            if (x["type"] == "msg"):
                if (x["date"] == date_from_terminate):
                    print("Terminating from old chat at data =>", x["date"])
                    break
        except:
            print("Debbug it", x)
            exit(101)
        DATA[i] = x
        i = i + 1

    for x in data2.values():
        DATA[i] = x
        i = i + 1

    date = ''
    i = 0
    for dat in DATA.values():
        if dat['type'] == 'msg':
            if dat['date'] != date:
                date = dat['date']
                i = i + 1
                dat['day'] = i
            else:
                dat['day'] = i

    json.dump(DATA, file4, indent=4)