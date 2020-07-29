import simplejson as json
from fractions import Fraction
file_name_to_process = 'Intermediate/Previous.txt'
end_file = 'Intermediate/calender.txt'

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
    elif(min>=30):
        return 0
    else:
        return min

def Convert(time):
    hrs = int(time/60)
    if hrs != 0:
        return str(hrs)+"hrs " + str(time % 60) + "min"
    else:
        return str(time % 60) + "min"

def date():
    file2 = open(file_name_to_process, 'r')
    data = json.load(file2)
    out = []
    for dat in data.values():
        if dat['type']=='msg':
            if {'day':dat['day'],"date":dat['date']} not in out:
                out.append({'day':dat['day'],"date":dat['date']})

    day=0
    stTime=""
    endTime=""
    i=0

    sum=0
    i=-1
    day=0
    for dat in data.values():
        if dat['type'] == 'msg':
            if dat['day'] == day:
                sum =sum + Diff(stTime,dat['time'])

                stTime = dat['time']
            else:
                day = dat['day']
                stTime = dat['time']
                i=i+1
                if(i!=0):
                    out[i-1]['total_time'] = sum
                sum = 0
    out[i ]['total_time'] = sum
    # print(out)
    return out

def Calender():
    out=date()
    print(out)
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
                    print('appending',dict['total_time'])
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

    file = open(end_file,'w')
    json.dump(outlist,file,indent=4)
    print('hey')
    return outlist

Calender()