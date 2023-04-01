from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from myApp.Expert import *
import yake
import json

from .models import expert
# Create your views here.



def index(request):
    return render(request, "index.html",)
    
def profile(request):
    return render(request, "profile.html")

@login_required(login_url="login")    
def search(request):
    return render(request, "search.html")
def redirectlogin(request):
    return render(request,"login.html")
def GetExperts(request):
    
    input=request.POST.get("query")
    university=request.POST.get("university")
    citations=request.POST.get("citations")
    
    return render(request,"expert.html")

def showExperts(request):
  query=request.POST["query"]
  context=Dummy() # getting data from API
  request.session['experts']=context
  
  
  return render(request,"expert.html",context)   #passing data to the html template.
    
def expert_bio(request):
  return render(request,"bio.html")  
  
def navbar(request):
  return render(request,"navbar.html")    
def login_user(request):
    if request.method=="POST":
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request,user)
        return redirect("search")
        ...
      else:
        messages.success(request,("There was an error.Please try with a valid user name and password"))
        return redirect("redirectlogin")
        ...
    else:
      return render(request,"redirectlogin")


  
def save_result(request,id):
   Id=id
   experts=(request.session['experts'])
   interests=[]

   for exp in experts['experts']:
        if exp['author_id'] == Id:
            #for raw_interests in exp["interests"]:
              # interests.append(raw_interests["title"])  #expert_interests=interests
            e=expert(user=request.user,expert_name=exp['name'],expert_id=exp['author_id'],expert_affiliation=exp['affiliations'],expert_interests=exp["interests"])
            e.save()
   return HttpResponse(status=204)

def view_report(request,name,affiliations):
      print (name,affiliations)
      return redirect("expert_bio")

def manage_results(request):
    expert_objects=(expert.objects.filter(user=request.user))
    expert_dict={"expert_objects": expert_objects}
    for exp in expert_dict.values():
      print(exp.values())
    return render(request,"saved_results.html",expert_dict)

def delete_result(request,id):
   e=expert.objects.get(expert_id=id,user=request.user)
  
   e.delete()
   return redirect("manage_results")
