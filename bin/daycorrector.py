#this is for working with one json file the FullChat
import simplejson as json
#This code corrects the day accordingly
file=open('Intermediate/Combined.txt','r')
file2=open('Intermediate/Previous.txt','w')
data=json.load(file)
print(data)
date=''
i=0
for dat in data.values():
    if dat['type']=='msg':
        if dat['date']!=date:
            date=dat['date']
            i = i + 1
            dat['day']=i
        else:
            dat['day']=i

list1=[]
for dat in data.values():
    if dat['type']=='msg':
        if (dat['date'],dat['day']) not in list1:
            list1.append((dat['date'],dat['day']))

json.dump(data,file2,indent=4)
for items in list1:
    print(items)

def DayChat(day):
    file2=open('Fullchat1','r')
    data=json.load(file2)
    out=[]

    for dat in data.values():
        if dat['type']=='msg':
            if dat['day']==day:
                flag=1
                if dat['name']=='Ashish Jain':
                    Sj=False
                else:
                    Sj=True
                dict1={'time':dat['time'],'msg':dat['msg'],'Sj':Sj}
                out.append(dict1)
                date=dat['date']
                # print(dat)
            else:
                flag=0
        else:
            if flag==1:
                print({'msg':dat['extra'],'Sj':Sj})
                out.append({'msg':dat['extra'],'Sj':Sj})
                # print(dat)
    output={'date':date,'data':out}

    return output

# out=DayChat(32)
# print(out)