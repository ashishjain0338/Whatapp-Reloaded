from django.shortcuts import render,redirect
from .provider import DayChat,date
import simplejson as json
import calendar
# Create your views here.
Jsontxt="Output/JsonFile.json"
Caltxt = "Output/calender.json"
Summtxt = "Output/summary.json"
def home(request):
    # print(date())
    if request.method=='POST':
        day=request.POST['day']
        # print(day)
        return redirect('/'+day+'/')
    return render(request,'specific_home.html',{'data':date()})

def Day(request,day):
    if request.method == 'POST':
        print(request.POST)
        flag = 0
        for keys in request.POST.keys():
            if keys == 'day':
                flag = 1
        if (flag == 1):
            flag = 0
            day=request.POST['day']
            print(day)
            return redirect('/'+day+'/')
        else:
            status = request.POST['status']
            if status=='previous':
                day=int(day)-1
            else:
                day=int(day)+1
            if day==0:
                day=1
            return redirect('/' + str(day) + '/')
    if(len(day)>0):
        data = DayChat(int(day))
        return render(request,'day.html',{"data":data['data'],'day':day,'date':data['date'],'DateDay':date()})
    else:
        return render(request,'day.html')

def Summary(request):
    file = open(Summtxt,'r')
    data = json.load(file)
    # print(data)
    file2 = open(Caltxt,'r')
    caldata = json.load(file2)
    return render(request,'Summary.html',{"data":data,'Calender':caldata})

def Calender(request):
    file2 = open(Caltxt, 'r')
    caldata = json.load(file2)
    # print('hey')
    return  render(request,'Calender.html',{'Calender':caldata})