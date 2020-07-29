import simplejson as json
Jsontxt="Output/JsonFile.json"
Caltxt = "Output/calender.json"
Summtxt = "Output/summary.json"
def DayChat(day):
    file2=open(Jsontxt,'r')
    data=json.load(file2)
    file1 = open(Summtxt , 'r')
    dat = json.load(file1)
    first_person = dat['ash']['name']
    out=[]
    date='01/02/2020'
    flag = 0
    for dat in data.values():
        if dat['type']=='msg':
            if dat['day']==day:
                flag=1
                if dat['name']== first_person :
                    Sj=False
                    print('XXXXXXXXXXXXX', dat['name'], Sj)
                else:
                    Sj=True
                    print('XXXXXXXXXXXXX', dat['name'], Sj)
                dict1={'time':dat['time'],'msg':dat['msg'],'Sj':Sj}
                out.append(dict1)
                date=dat['date']
                # print(dat)
            else:
                flag=0
        else:
            if flag==1:
                # print({'msg':dat['extra'],'Sj':Sj})
                out.append({'msg':dat['extra'],'Sj':Sj})
                # print(dat)
    output={'date':date,'data':out}

    return output

def date():
    file2 = open(Jsontxt, 'r')
    data = json.load(file2)
    out = []
    for dat in data.values():
        if dat['type']=='msg':
            if {'day':dat['day'],"date":dat['date']} not in out:
                out.append({'day':dat['day'],"date":dat['date']})

    return out