import os
import json
from urllib.parse import urlsplit, parse_qsl
from serpapi import GoogleSearch
def Dummy():    # dummy function to test the search functionaility by returning raw json data
    result={
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
    
    return result
def getExperts(query:str):
  
    params = {
        "api_key": ("c7522e1e379906672ad08268ac5d1c4363828bfacb8e59607ad09df75685ff01"),                   # SerpApi API key
        "engine": "google_scholar_profiles",               # profile results search engine
        "mauthors":  f'label:{query}'  # search query
    }
    search = GoogleSearch(params)

    profile_results_data = []

    profiles_is_present = True
    while profiles_is_present:
        profile_results = search.get_dict()
        for profile in profile_results["profiles"]:
            thumbnail = profile["thumbnail"]
            name = profile["name"]
            link = profile["link"]
            author_id = profile["author_id"]
            affiliations = profile["affiliations"]
            email = profile.get("email")
            cited_by = profile.get("cited_by")
            interests = profile.get("interests")

            profile_results_data.append({
                "thumbnail": thumbnail,
                "name": name,
                "link": link,
                "author_id": author_id,
                "email": email,
                "affiliations": affiliations,
                "cited_by": cited_by,
                "interests": interests
            })

        if "next" in profile_results.get("serpapi_pagination", {}):
            # splits URL in parts as a dict() and update search "params" variable to a new page that will be passed to GoogleSearch()
            search.params_dict.update(dict(parse_qsl(urlsplit(profile_results.get("serpapi_pagination").get("next")).query)))
        else:
            profiles_is_present = False

    
    return ({'experts':profile_results_data})


def getOrganicResult():  
  data=[]  
  for result in soup.select('.gs_r.gs_or.gs_scl'):
        title = result.select_one('.gs_rt').text
        title_link = result.select_one('.gs_rt a')['href']
        publication_info = result.select_one('.gs_a').text
        snippet = result.select_one('.gs_rs').text
        cited_by = result.select_one('#gs_res_ccl_mid .gs_nph+ a')['href']
        try:
            pdf_link = result.select_one('.gs_or_ggsm a:nth-child(1)')['href']
        except: 
            pdf_link = None

        data.append({
            'title': title,
            'title_link': title_link,
            'publication_info': publication_info,
            'snippet': snippet,
            'cited_by': f'https://scholar.google.com{cited_by}',
            'related_articles': f'https://scholar.google.com{related_articles}',
            'all_article_versions': f'https://scholar.google.com{all_article_versions}',
            "pdf_link": pdf_link
        })
