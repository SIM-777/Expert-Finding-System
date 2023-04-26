from django.shortcuts import render,redirect
from django.db import IntegrityError
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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
def GetExperts(query,university_name,citation_num):
  raw_expert_list={}
  expert_list=[]
  if query!='':
    print("Query is : " + query)
    if (university_name!='' and citation_num!=''):
       print ("Citation number is " + citation_num)
       raw_expert_list=Dummy()  # get data from API with University Name
       for profile in raw_expert_list["experts"]:
         if profile["cited_by"] >= int(citation_num):
          expert_list.append(profile)
    elif (university_name!='' and citation_num==''):
        raw_expert_list=Dummy() #get data from API with University Name
        expert_list=raw_expert_list.copy()

    elif (university_name=='' and citation_num!=''):
        raw_expert_list=Dummy() #get data from API as usual
        for profile in raw_expert_list["experts"]:
         if profile["cited_by"] >= int(citation_num):
           expert_list.append(profile)
    else:
        raw_expert_list=Dummy()
                   
  return expert_list  

def showExperts(request):
 
 if request.method=="POST": 
  query=request.POST["query"]
  university_name=request.POST.get("university_name",False)
  citation_num=request.POST.get("citation_num",False)
  expert_list=GetExperts(query,university_name,citation_num)
  expert_dict={"experts": expert_list}
  return render(request,"expert.html",expert_dict)   #passing data to the html template.
    
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
            try:
              e.save()
              messages.success(request,"Data saved successfully")
              return HttpResponse(status=204)
              
            except IntegrityError as e:
              messages.success(request,"Data already exists!")
              return HttpResponse(status=204) 
        

def view_report(request,name,affiliations):
      print (name,affiliations)
      return redirect("expert_bio")

def manage_results(request):
    if request.GET.get('q')!=None:
           q=request.GET.get('q')
           expert_objects=expert.objects.filter((Q(expert_name__icontains=q)|
                                         Q(expert_affiliation__icontains=q)|
                                         Q(expert_interests__icontains=q)),user=request.user)
                                        
           expert_dict={"expert_objects":expert_objects}
    else:       
       
      expert_objects=(expert.objects.filter(user=request.user))
      expert_dict={"expert_objects": expert_objects}
  
    return render(request,"saved_results.html",expert_dict)
def search_experts_from_db(request):
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
    expert_objects=expert.objects.filter(Q(expert_name__name__icontains=q)|
                                         Q(expert_affiliation__name__incontains=q)|
                                         Q(expert_interests__name__icontains=q))
    expert_dict={"expert_objects":expert_objects}
    return render(request,"saved_results.html",expert_dict)

def delete_result(request,id):
   e=expert.objects.get(expert_id=id,user=request.user)
  
   e.delete()
   #return redirect("manage_results")
   return redirect(request.META.get('HTTP_REFERER'))
def navbar(request):
   return render(request,"navbar.html")


def Testing():
   experts=Dummy()
   for expert in experts["experts"]:
      print (type(expert["cited_by"]))