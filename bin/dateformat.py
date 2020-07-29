import simplejson as json
#mm-dd-yy to dd-mm-yyyy
file=open('Json.txt','r')
file2=open('DateCorrect.txt','w')
data=json.load(file)
print(data)
i=1
JSON={}
for dat in data.values():
    if dat['type']=='msg':
        date=dat['date']
        month=date[:date.index('/')]
        if len(month)==1:
            month='0'+month
        day=date[date.index('/')+1:date[date.index('/')+1:].index('/')+date.index('/')+1]
        if len(day)==1:
            day='0'+day

        year=date[date[date.index('/')+1:].index('/')+date.index('/')+2:]
        if len(year)==2:
            year='20'+year

        DATE=day+'/'+month+'/'+year
        dat['date']=DATE
        JSON[i] = dat
        i = i + 1
    else:
        dict1 = {'type': 'extra', 'extra': dat['extra']}
        JSON[i] = dict1
        i = i + 1


print(JSON)
json.dump(JSON,file2,indent=4)