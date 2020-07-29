import simplejson as json
file=open('DontDelete/Previous.txt','r',encoding='utf8', errors='ignore')
file2=open('Intermediate/JsonSJJuneS.txt','r',encoding='utf8', errors='ignore')
# file3=open('data3.txt','r',encoding='utf8', errors='ignore')
file4=open('Intermediate/Combined.txt','w',encoding='utf8', errors='ignore')
data1=json.load(file)
data2=json.load(file2)
# data3=json.load(file3)
date_from_terminate = "08/06/2020"
DATA={}
print(data1)
print(data2)
i=1
for x in data1.values():
    try:
        if(x["type"] == "msg"):
            if(x["date"] == date_from_terminate):
                print("Terminating from first chat at data =>",x["date"])
                break
    except:
        print("Debbug it",x)
        exit(101)
    DATA[i]=x
    i=i+1

for x in data2.values():
    DATA[i]=x
    i=i+1

# for x in data3.values():
#     DATA[i]=x
#     i=i+1
print(i)
print(DATA)
json.dump(DATA,file4,indent=4)