from django.shortcuts import get_object_or_404, render,redirect
from django.views import View
from JobPortal.decorators import *
from .models import *
from django.contrib.auth import login,logout,authenticate
from .forms import *
from django.contrib import messages

# ------------------------------ Registation page-------------------------------------
def registerUser(request, role):
    form=UserWithRoleForm()
    if request.method=='POST':
        form=UserWithRoleForm(data=request.POST)
        if form.is_valid():
        
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            print(password1,password2)
            if (password1==password2 ):
                user_details = {
                    'username': form.cleaned_data.get('username'),
                    'first_name':form.cleaned_data.get('first_name'),
                    'last_name': form.cleaned_data.get('last_name'),
                    'email': form.cleaned_data.get('email'),
                    'password': form.cleaned_data.get('password2'),
                }
                user= User.objects.create(
                    username=user_details.get('username'),
                    first_name=user_details.get('first_name'),
                    last_name=user_details.get('last_name'),
                    email=user_details.get('email'),
                    
                    )
                password=user_details.get('password')
                user.set_password(password)
                user.save()
                UserWithRole.objects.create(
                    username=form.cleaned_data.get('username'),
                    first_name=form.cleaned_data.get('first_name'),
                    last_name=form.cleaned_data.get('last_name'),
                    dob=form.cleaned_data.get('dob'),
                    gender=form.cleaned_data.get('gender'),
                    mobile=form.cleaned_data.get('mobile'),
                    email= form.cleaned_data.get('email'),
                    role = role
                )
                messages.success(request, "You Have registered Successfully!")
                return redirect('login', role=role)
    context={

        'form':form,
        'role': role
    }
    
    return render(request,'register.html',context)

# --------------------------------login page -------------------------------------
def loginUser(request, role):
    if request.method=="POST":
        name=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=name,password=pwd)
        login(request,user)

        if role=="admin":
            return redirect("adminpage")
        elif role =="hr":
             return redirect("hrview")
        elif role =="candidate":
            return redirect("candidateview")
    return render(request,'candidatelogin.html', context={"role": role})
 
    
#-----------------------------------logout page-----------------------------------

def logoutUser(request):
    logout(request)
    return redirect('home')

# ------------------------------- landing page -------------------------------------------------------------
def home(request) :
    if request.user.is_authenticated:
        hrs=UserWithRole.objects.all()
        context={
           'hrs':hrs,
        }   
        return render(request,'adminpage.html',context)
    else:
        return render(request,'login.html')
    


# ------------------------------- admin landing page --------------------------------------------------------
@admin_required
def adminpage(request):   
        hrs=UserWithRole.objects.all()
        context={
           'hrs':hrs,
        }     
        return render(request,'adminpage.html',context)


# ------------------------------- adding hr page -------------------------------------------------------------------
@admin_required
def Addhr(request):
    form=UserWithRoleForm()
    if request.method=='POST':
        form=UserWithRoleForm(data =request.POST,files =request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "You Have Added A HR Successsfully!")
            return redirect('adminpage')
    context={'form':form}
    return render(request,'addhr.html',context)


#---------------------------------------------------edit admin page--------------------------------------------------
@admin_required
def edit_admin_hr(request,pk):

    edit_admin_user = get_object_or_404(UserWithRole, pk=pk)

    if request.method =="POST":
        form = UserWithRoleForm(request.POST,instance=edit_admin_user)
        if form.is_valid(): 
            form.save()
            return redirect('adminpage')
    else:
        form =UserWithRoleForm(instance= edit_admin_user)
    return render(request,'addhr.html', {'form':form})


#------------------------------------delete admin page--------------------------------------------------------
@admin_required
def delete_admin_user(request,pk):
    admin_user = get_object_or_404(UserWithRole, pk=pk)
    
    admin_user.delete()
    return redirect ('adminpage')



# ------------------------------- HR landing page -------------------------------------------------------------
@hr_required
def hrview (request):
    companies=Company.objects.all()
    context={
             'companies':companies,
         }
    return render (request,'hrview.html',context)

# ------------------------------- adding job page -----------------------------------------------------------------
@hr_required
def Addjob(request):
    form=Companyform()
    if request.method=='POST':
        form=Companyform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "You Have Added A Job Successsfully!")
            return redirect('hrview')
    elif request.method == 'GET':
        initial_form_data = {
            'user': request.user,
    }
        form=Companyform(initial=initial_form_data)
    context={'form':form}
    return render(request,'addjob.html',context)

#-----------------------------------------------------edit hr page--------------------------------------------------
@hr_required
def edit_job_hr(request,pk):

    edit_hr_job = get_object_or_404(Company, pk=pk)

    
    if request.method =="POST":
        form = Companyform(request.POST,instance=edit_hr_job)
        if form.is_valid(): 
            form.save()
            return redirect('hrview')
    else:
        form =Companyform(instance= edit_hr_job)
    return render(request,'addjob.html', {'form':form})

# ---------------------------------------------delete hr page------------------------------------------------------
@hr_required
def delete_hr_job(request,pk):
    hr_user = get_object_or_404(Company, pk=pk)
    hr_user.delete()
    return redirect ('hrview')



# ------------------------------- Candidate landing page ---------------------------------------------------------
@candidate_required
def CompanyPage(request):
        companies=Company.objects.all()
        context={
            'companies':companies,
        }
        return render(request,'candidateview.html',context)
    



# ------------------------------- applying job page ---------------------------------------------------------------
@candidate_required
def applyPage(request, company_id):
    if request.method=='POST':
        form=ApplyForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            
            form.save()
            messages.success(request, "You Have Applied for Job Successfully!")
            return redirect('appliedjobs')
    elif request.method == 'GET':

        initial_form_data = {
            'candidate_user': UserWithRole.objects.get(username=request.user.username),
            'company': Company.objects.get(id=company_id),
        }
        form=ApplyForm(initial=initial_form_data)
        
    context={'form':form}
    return render(request,'apply.html',context)

# ------------------------------- view applied job page -----------------------------------------------------------

def appliedjobs(request):
     if request.user.is_authenticated:
        candidates=Candidates.objects.all()
        context={
            'candidates':candidates,
        }
        return render(request,'appliedjobs.html',context)
        