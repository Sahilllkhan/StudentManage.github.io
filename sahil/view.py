from django.http import HttpResponse,HttpResponseRedirect
from distutils.util import execute
from django.shortcuts import render
from tabledata.models import tabledata
from tabledata.models import passouts
from tabledata.models import fee
from datetime import date
from tabledata.models import feetable


def home(request):
    return render(request,"index.html")

def registration(request):
    try:
        if request.method=="POST":
            reg="Ducat"
            name=request.POST.get('name')
            fname=request.POST.get('fathername')
            mname=request.POST.get('mothername')
            phone_no=request.POST.get('phoneno')
            addr=request.POST.get('address')
            city=request.POST.get('city')
            gender=request.POST.get('gender')
            course=request.POST.get('course')
            btime=request.POST.get('btime')
            photo=request.FILES['photo']
            fee=request.POST.get('fee')

            data=tabledata(
                regno=reg,
                name=name,
                fname=fname,
                mname=mname,
                phone_no=phone_no,
                address=addr,
                city=city,
                gender=gender,
                course=course,
                btime=btime,
                photo=photo,
                fee=fee,
                remfee=fee,
                )
            data.save()

            data=tabledata.objects.all().order_by('-id')[0]
            fid=data.id
            regno="Ducat"+str(fid)
            data1=tabledata(
                id=fid,
                regno=regno,
                name=name,
                fname=fname,
                mname=mname,
                phone_no=phone_no,
                address=addr,
                city=city,
                gender=gender,
                course=course,
                btime=btime,
                photo=photo,
                fee=fee,
                remfee=fee,
                )
            data1.save()         
    except:
        pass
    return render(request,"registration.html")

def view(request):
    return render(request,"view.html")

def viewall(request):
    data=tabledata.objects.all()
    data1={
        'alldata':data
    }
    return render(request,"viewall.html",data1)

def viewbybatchtime(request):
    try:
        if request.method=="POST":
            fbtime=request.POST.get('btime')
            url="/fviewbybatchtime/"+fbtime
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"viewbybatchtime.html")

def fviewbybatchtime(request,fbtime):
    b_time=tabledata.objects.filter(btime=fbtime)
    data1={
        'btimedata':b_time
    }
   
    return render(request,"viewbybatchtime1.html",data1)

def viewbyregno(request):
    try:
        if request.method=="POST":
            regno=request.POST.get('regno')
            url="/fviewbyregno/"+regno
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"viewbyregno.html")

def fviewbyregno(request,fregno):
    regno=tabledata.objects.get(regno=fregno)
    data1={
        'regnodata':regno
    }
    return render(request,"viewbyregno1.html",data1)

def viewbyname(request):
    try:
        if request.method=="POST":
            fnme=request.POST.get('name')
            url="/fviewbyname/"+fnme
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"viewbyname.html")

def fviewbyname(request,fname):
    d_name=tabledata.objects.filter(name=fname)
    data1={
        'namedata':d_name
    }
    return render(request,"viewbyname1.html",data1)


def delete(request):
    try:
        if request.method == "POST":
            regno=request.POST.get("regno")
            fregno=tabledata.objects.get(regno=regno)
            
            regno=fregno.regno
            name=fregno.name
            fname=fregno.fname
            mname=fregno.mname
            phone_no=fregno.phone_no
            address=fregno.address
            city=fregno.city
            gender=fregno.gender
            course=fregno.course
            btime=fregno.btime
            photo=fregno.photo
            fee=fregno.fee
            remfee=fregno.remfee
            data=passouts(regno=regno,name=name,fname=fname,mname=mname,phone_no=phone_no,address=address,city=city,gender=gender,course=course,btime=btime,photo=photo,fee=fee,remfee=remfee)
            data.save()
            fregno.delete()

            url="/delete/"
            return HttpResponseRedirect(url)


    except:
        pass
    return render(request,"delete.html")



def update(request):
    try:
        if request.method=="POST":
            fupdate = request.POST.get('regno')
            url = '/update1/'+fupdate
            
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"update.html")

def update1(request,fupdate):
    get_id = tabledata.objects.get(regno=fupdate)
    
    uid = get_id.id
    
    data1 = {
        'data1' : get_id
    }
    try:
        if request.method=="POST":
            name = request.POST.get("name")
            fname = request.POST.get("fathername")
            mname = request.POST.get("mothername")
            phone = request.POST.get("phoneno")
            address = request.POST.get("address")
            city = request.POST.get("city")
            gender = request.POST.get("gender")
            course = request.POST.get("course")
            btime = request.POST.get("btime")
            photo = request.POST.get("photo")
            fee = request.POST.get("fee")
           
            
            data = tabledata(
                id=uid,
                regno=fupdate,
                name=name,
                fname=fname,
                mname=mname,
                phone_no=phone,
                address=address,
                city=city,
                gender=gender,
                course=course,
                btime=btime,
                photo=photo,
                fee=fee,
            
                )
            data.save()
    except:
        pass
        
    return render(request,"update1.html",data1)

def fee(request):
    return render(request,"fees.html")

def viewfee(request):
    try:
        if request.method=="POST":
            regnos=request.POST.get('regno')

            url="/fviewfee/"+regnos
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"viewfee.html")

def fviewfee(request,fregno):
     
    fregno=tabledata.objects.get(regno=fregno)
    data1={
        'fee':fregno
    }
    
    return render(request,"viewfee1.html",data1)

def subfee(request):
    try:
        if request.method=="POST":
            regno=request.POST.get('regno')

            url="/subdatafee/"+regno
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"submitfee.html")

def subdatafee(request,fregno):
    fregno=tabledata.objects.get(regno=fregno)
    data={
        'regno':fregno
    }
    try:
        if request.method=="POST":
            reg_no=fregno.regno
            fees=request.POST.get('fee')
            today1=date.today()
            totalfee=fregno.remfee
            rem=int(totalfee)-int(fees)
            subfees=feetable(regno=reg_no,fee=fees,totalfee=totalfee,date=today1,rem=rem)
            subfees.save()
             
            uid=fregno.id
            
            sahil= tabledata(
                id=uid,
                regno=fregno.regno,
                name=fregno.name,
                fname=fregno.fname,
                mname=fregno.mname,
                phone_no=fregno.phone_no,
                address=fregno.address,
                city=fregno.city,
                gender=fregno.gender,
                course=fregno.course,
                btime=fregno.btime,
                photo=fregno.photo,
                fee=fregno.fee,
                remfee=rem,
            
                )
            sahil.save()


    except:
        pass
    return render(request,"submitfee1.html",data)

def passoutdata(request):
    data=passouts.objects.all()
    data1={
        'alldata':data
    }
    return render(request,"passout.html",data1)

