from django.db import connection
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
#create your views here
def home(request):
    cdata=companies.objects.all().order_by('-id')[0:6]#showing records range
    vdetail = vacancy.objects.all().order_by('-jid')[0:4]
    return render(request,'user/index.html',{"data":cdata,"vdetail":vdetail})
def adminlogin(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        res = register(email=uname, passwd=password)
        if res:
            request.session['stu']=uname
            return HttpResponse("<script>alert('Logged In successfully');window.location.href='/user/myprofile/';</script>");
    return render(request,'user/login.html')
def appliedjobs(request):
    if request.session.get('stu'):
        id=request.session.get('stu')
        cursor=connection.cursor()
        cursor.execute("select j.*,a.* from user_vacancy j,user_applyjob a where a.sid='"+id+"' and j.jid=a.jid")
        alldata=cursor.fetchall()
        return render(request,'user/Appliedjobs.html',{"alldata":alldata})
    else:
        return HttpResponse("<script>alert('Login first to see apply');window.location.href='/user/adminlogin/'</script>")
def placement(request):
    pdata=placement.objects.all().order_by('id')
    return render(request,'user/placement.html',{"place":pdata})
def registration(request):
    if request.method=='POST':
        Name=request.POST.get("name","")
        Email=request.POST.get("email","")
        Password=request.POST.get("passwd","")
        Profile=request.FILES['picture']
        DOB=request.POST.get("dob","")
        Number=request.POST.get("number","")
        Gender=request.POST.get("gender","")
        Address=request.POST.get("address","")
        Year=request.POST.get("year","")
        Qualification=request.POST.get("qualification","")
        Course=request.POST.get("Year","")
        Resume=request.FILES['resume']
        res=register(name=Name,number=Number,email=Email,dob=DOB,passwd=Password,gender=Gender,address=Address,qualification=Qualification,course=Course,year=Year,picture=Profile,resume=Resume)
        res.save()
        return HttpResponse("<script>alert('you are registered successfully');window.location.href='/user/adminlogin/'</script>")

    return render(request,'user/registration.html')
def newvacancy(request):
    if(request.GET.get('jid') is not None):
        if(request.session.get('stu')):
            jid=request.GET.get('jid')
            userid=request.session.get('stu')
            acount=applyjob.objects.filter(jid=jid,sid=userid).count() >0
            if acount:
                return HttpResponse("<script>alert('you have applied successfully');window.location.href='/user/newvacancy/'</script>");
            else:
                a=applyjob(jid=jid,sid=userid)
                a.save()
                return HttpResponse("<script>alert('you have applied successfully');window.location.href='/user/newvacancy/'</script>");
        else:
            return HttpResponse("<script>alert('Login first to apply');window.location.href='/user/adminlogin/'</script>")
    if (request.GET.get('cid') is not None):
        cid=request.GET.get('cid')
        vdetail = vacancy.objects.filter(cid=cid)
    else:
        vdetail = vacancy.objects.all().order_by('-jid')
    cdata = companies.objects.all().order_by('id')
    return render(request,'user/Newvacancy.html',{"data":cdata,"vdetail":vdetail})
def myprofile(request):
    if request.session.get('stu'):
        id=request.session.get('stu')
        userdata=register.objects.filter(email=id)[0:1]
        print(userdata)
        return render(request,'user/myprofile.html',{"userdata":userdata})
    else:
        return HttpResponse("<script>alert('Login first to apply');window.location.href='/user/adminlogin/'</script>")
def about(request):
    return render(request,'user/about.html')
def contactus(request):

    status=False
    if request.method=='POST':
        Name=request.POST.get("name","")
        Mobile=request.POST.get("mobile","")
        Email=request.POST.get("email","")
        Message=request.POST.get("msg","")
        res=contact(name=Name,email=Email,contact=Mobile,message=Message)
        res.save()
        status=True
        return HttpResponse("<script>alert('Thanks for enquiry...');window.location.href='/user/contactus/'</script>")
    return render(request,'user/contactus.html',{'S':status})
def termcondition(request):
    return render(request,'user/termcondition.html')
def privacypolicy(request):
    return render(request,'user/privacypolicy.html')