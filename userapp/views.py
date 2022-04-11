from django.shortcuts import render
from userapp.models import userdb
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def user(request):
    return render(request, 'userdetails.html')
def getdata(request):
    if request.method =='POST':
        img_a=request.FILES['abc']
        fname_a=request.POST.get('fname')
        lname_a=request.POST.get('lname')
        pass_a=request.POST.get('password')
        number_a=request.POST.get('number')
        email_a=request.POST.get('email')
        data=userdb(fname=fname_a,lname=lname_a,password=pass_a,number=number_a,email=email_a,abc=img_a)
        data.save()
    return redirect('user')
def tableview(request):
    obj = userdb.objects.all()
    return render(request,'viewuserdetails.html',{'obj':obj})
def edit(request,id):
    obj = userdb.objects.filter(id=id)
    return render(request, 'edit.html',{'obj':obj})
def update(request,id):
    if request.method == 'POST':
        fname_c=request.POST.get('fname')
        lname_c=request.POST.get('lname')
        pass_c=request.POST.get('password')
        number_c=request.POST.get('number')
        email_c=request.POST.get('email')
        try:
            image_c=request.FILES['abc']
            fs = FileSystemStorage() 
            file = fs.save(image_c.name, image_c)
        except MultiValueDictKeyError:
            file=userdb.objects.get(id=id).abc  
    userdb.objects.filter(id=id).update(fname=fname_c,lname=lname_c,password=pass_c,number=number_c,email=email_c,abc=file)
    return redirect('user')

def delete(request,id):
    userdb.objects.get(id=id).delete()
    return redirect('user')