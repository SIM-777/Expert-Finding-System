from django.shortcuts import render,redirect
from django.http import HttpResponse
import yake
# Create your views here.



def index(request):
    return render(request, "index.html",)
    
def profile(request):
    return render(request, "profile.html",)
def search(request):
    return render(request, "search.html")

def GetExperts(request):
    
    input=request.POST.get("query")
    university=request.POST.get("university")
    citations=request.POST.get("citations")
    
    return render(request,"expert.html")

def showExperts(request):
    context={
        "experts":[
  {
    "thumbnail": "https://scholar.googleusercontent.com/citations?view_op=small_photo&user=JicYPdAAAAAJ&citpid=2",
    "name": "Geoffrey Hinton",
    "link": "https://scholar.google.com/citations?hl=en&user=JicYPdAAAAAJ",
    "author_id": "JicYPdAAAAAJ",
    "email": "Verified email at cs.toronto.edu",
    "affiliations": "Emeritus Prof. Comp Sci, U.Toronto & Engineering Fellow, Google",
    "cited_by": 638900,
    "interests": [
      {
        "title": "machine learning",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Amachine_learning",
        "link": "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:machine_learning"
      },
      {
        "title": "psychology",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Apsychology",
        "link": "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:psychology"
      },
      {
        "title": "artificial intelligence",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Aartificial_intelligence",
        "link": "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:artificial_intelligence"
      },
      {
        "title": "cognitive science",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Acognitive_science",
        "link": "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:cognitive_science"
      },
      {
        "title": "computer science",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Acomputer_science",
        "link": "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:computer_science"
      }
    ]
  },
  {
    "thumbnail": "https://scholar.googleusercontent.com/citations?view_op=small_photo&user=kukA0LcAAAAJ&citpid=3",
    "name": "Yoshua Bengio",
    "link": "https://scholar.google.com/citations?hl=en&user=kukA0LcAAAAJ",
    "author_id": "kukA0LcAAAAJ",
    "email": "Verified email at umontreal.ca",
    "affiliations": "Professor of computer science, University of Montreal, Mila, IVADO, CIFAR",
    "cited_by": 605714,
    "interests": [
      {
        "title": "Machine learning",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Amachine_learning",
        "link": "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:machine_learning"
      },
      {
        "title": "deep learning",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Adeep_learning",
        "link": "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:deep_learning"
      },
      {
        "title": "artificial intelligence",
        "serpapi_link": "https://serpapi.com/search.json?engine=google_scholar_profiles&hl=en&mauthors=label%3Aartificial_intelligence",
        "link": "https://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=label:artificial_intelligence"
      }
    ]
  }
        ]
    }
    return render(request,"expert.html",context)    
    
