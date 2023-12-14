from django.shortcuts import render
from .forms import PDMScoreForm

# Create your views here.


def index(request):
    if request.method == "POST":
        w1 = request.POST['w1']
        w2 = request.POST['w2']
        w3 = request.POST['w3']
        
        print("weights :: {}".format(w1))
        
        return render(request, "index.html")
    else: 
        return render(request, "index.html")



def calculate_pdm_score(w1=0.5, w2=0.3, w3=0.2, nsr=0.7, rb=0.1, sensitivity=0.8):
    score = (w1 * nsr) + (w2 * sensitivity) - (w3 * rb)
    print(score)
    return score 
