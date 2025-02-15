from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app.models import Crud
from django.db.models import Q
def signup(request):
    if request.method=='POST':
        u_name=request.POST.get('u_name')
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        sex=request.POST.get('sex')
        email=request.POST.get('email')
        password=request.POST.get('password')
        my_user=User.objects.create_user(u_name,email,password)
        my_user.save()
        return redirect('login')
    return render(request,'signup.html')
def Login(request):
    if request.method == 'POST':
        uname= request.POST.get('uname')
        pass1= request.POST.get('pass')
        user = authenticate(username=uname,password=pass1)
        
        if user is not None:
            login(request, user)  # Log
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!")
    return render(request,'login.html')
@login_required(login_url='login')
def home(request):
    return render(request,'index.html')

def crud(request):
    
    user=Crud.objects.all()
    if request.method=='POST':
        name=request.POST.get('f_name')
        email=request.POST.get('email')
        role=request.POST.get('option')
        CrUd=Crud(name=name,email=email,role=role)
        CrUd.save()
        return redirect('crud')
    # if request.method=='POST':
    #         st=request.GET.get('search_name')
    #         if st!=None:
    #             user=Crud.objects.filter(email__icontainsS=st)
        
        

    return render(request,'crud.html',{'user':user})

def delete_data(request,id):
    pi=Crud.objects.get(id=id)
    pi.delete()
    return redirect('crud')
def edit_data(request):
    user=Crud.objects.all()
    context={'user':user}

    return redirect(request,'crud.html',context)
    
# def update_data(request,id):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         role=request.POST.get('option')
#         em=Crud(id=id,name=name,email=email,role=role)
#         em.save()
#         return redirect('crud')
#     return render(request,'crud.html')

def update_data(request, id):
    user = get_object_or_404(Crud, id=id)  # Fetch the existing user or return 404

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        role = request.POST.get('option')

        # Update the existing user instead of creating a new one
        user.name = name
        user.email = email
        user.role = role
        user.save()

        return redirect('crud')  # Redirect to the correct view name

    return render(request, 'crud.html', {'user': user})  # Rend

# def search(request):
#     se=Crud.objects.all()
#     if request.method=='GET':
#         st=request.GET.get('search_name')
#         if st!=None:
#             se=Crud.objects.filter(email__icontains=st)
    
#     return render(request,'crud.html',{'user':se})