import  simplejson as json
file2=open('Intermediate/Previous.txt','r')
file=open('Intermediate/summary.txt','w')
data=json.load(file2)
ash={'ind':{'msg':0,'char':0,'word':0,'lg':['','',''],'LG':[]},'extra':{'msg':0,'char':0,'word':0,'lg':['','',''],'LG':[]}}
sim={'ind':{'msg':0,'char':0,'word':0,'lg':['','',''],'LG':[]},'extra':{'msg':0,'char':0,'word':0,'lg':['','',''],'LG':[]}}
for dat in data.values():
    if dat['type']=='msg':
        if dat['name'] == 'Ashish Jain' or dat['name'] in ' Ashish':
            ash['ind']['msg']=ash['ind']['msg']+1
            ash['ind']['char']=ash['ind']['char']+len(dat['msg'])
            if len(dat['msg'])>len(ash['ind']['lg'][2]):
                if len(dat['msg']) > len(ash['ind']['lg'][1]):
                    if len(dat['msg']) > len(ash['ind']['lg'][0]):
                        ash['ind']['lg'][2] = ash['ind']['lg'][1]
                        ash['ind']['lg'][1] = ash['ind']['lg'][0]
                        ash['ind']['lg'][0] = dat['msg']
                    else:
                        ash['ind']['lg'][2] = ash['ind']['lg'][1]
                        ash['ind']['lg'][1] = dat['msg']
                else:
                    ash['ind']['lg'][2]=dat['msg']
            for words in dat['msg']:
                if words==' ':
                    ash['ind']['word']=ash['ind']['word']+1
            Sj = False
        else:
            sim['ind']['msg'] = sim['ind']['msg'] + 1
            sim['ind']['char'] = sim['ind']['char'] + len(dat['msg'])
            if len(dat['msg'])>len(sim['ind']['lg'][2]):
                if len(dat['msg']) > len(sim['ind']['lg'][1]):
                    if len(dat['msg']) > len(sim['ind']['lg'][0]):
                        sim['ind']['lg'][2] = sim['ind']['lg'][1]
                        sim['ind']['lg'][1] = sim['ind']['lg'][0]
                        sim['ind']['lg'][0] = dat['msg']
                    else:
                        sim['ind']['lg'][2] = sim['ind']['lg'][1]
                        sim['ind']['lg'][1] = dat['msg']
                else:
                    sim['ind']['lg'][2]=dat['msg']
            for words in dat['msg']:
                if words==' ':
                    sim['ind']['word'] = sim['ind']['word'] + 1
            Sj = True
    else:
        if Sj:
            sim['extra']['msg'] = sim['extra']['msg'] + 1
            sim['extra']['char'] = sim['extra']['char'] + len(dat['extra'])
            if len(dat['extra'])>len(sim['extra']['lg'][2]):
                if len(dat['extra']) > len(sim['extra']['lg'][1]):
                    if len(dat['extra']) > len(sim['extra']['lg'][0]):
                        sim['extra']['lg'][2] = sim['extra']['lg'][1]
                        sim['extra']['lg'][1] = sim['extra']['lg'][0]
                        sim['extra']['lg'][0] = dat['extra']
                    else:
                        sim['extra']['lg'][2] = sim['extra']['lg'][1]
                        sim['extra']['lg'][1] = dat['extra']
                else:
                    sim['extra']['lg'][2]=dat['extra']
            for words in dat['extra']:
                if words == ' ':
                    sim['extra']['word'] = sim['extra']['word'] + 1
        else:
            ash['extra']['msg'] = ash['extra']['msg'] + 1
            ash['extra']['char'] = ash['extra']['char'] + len(dat['extra'])
            if len(dat['extra'])>len(ash['extra']['lg'][2]):
                if len(dat['extra']) > len(ash['extra']['lg'][1]):
                    if len(dat['extra']) > len(ash['extra']['lg'][0]):
                        ash['extra']['lg'][2] = ash['extra']['lg'][1]
                        ash['extra']['lg'][1] = ash['extra']['lg'][0]
                        ash['extra']['lg'][0] = dat['extra']
                    else:
                        ash['extra']['lg'][2] = ash['extra']['lg'][1]
                        ash['extra']['lg'][1] = dat['extra']
                else:
                    ash['extra']['lg'][2]=dat['extra']
            for words in dat['extra']:
                if words == ' ':
                    ash['extra']['word'] = ash['extra']['word'] + 1


print(ash,'\n',sim)
for msg in ash['ind']['lg']:
    for dat in data.values():
        if dat['type']=='msg':
            if dat['msg']==msg:
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

ash['ind']['wpm']=float(ash['ind']['word'])/ash['ind']['msg']
ash['ind']['cpw']=float(ash['ind']['char'])/ash['ind']['word']
ash['extra']['wpm']=float(ash['extra']['word'])/ash['extra']['msg']
ash['extra']['cpw']=float(ash['extra']['char'])/ash['extra']['word']
sim['ind']['wpm']=float(sim['ind']['word'])/sim['ind']['msg']
sim['ind']['cpw']=float(sim['ind']['char'])/sim['ind']['word']
sim['extra']['wpm']=float(sim['extra']['word'])/sim['extra']['msg']
sim['extra']['cpw']=float(sim['extra']['char'])/sim['extra']['word']
data={'ash':ash,'sim':sim}
# for x in [ash['ind'],ash['extra'],sim['ind'],sim['extra']]:
#     for y in x:
#         print(y,":",x[y])
#
json.dump(data,file,indent=4)

# msg=''
# for dat in data.values():
#     if dat['type']=='msg':
#         if dat['name'] == 'Ashish Jain' or dat['name'] in ' Ashish':
#             if len(dat['msg'])>len(msg):
#                 msg=dat['msg']
#
# print(msg,len(msg))