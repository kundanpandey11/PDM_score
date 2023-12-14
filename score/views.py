from django.shortcuts import render
from .forms import PDMScoreForm

# Create your views here.
def str_to_float(value):
    if "." not in value:
        value += ".0"
    value = float(value) 
    return value 

def calculate_pdm_score(w1=0.5, w2=0.3, w3=0.2, nsr=0.7, rb=0.1, sensitivity=0.8):
    score = (w1 * nsr) + (w2 * sensitivity) - (w3 * rb)
    return score 


def index(request):
    if request.method == "POST":
        w1 = str_to_float(request.POST['w1'])
        nsr = str_to_float(request.POST['nsr'])
        w2 = str_to_float(request.POST['w2'])
        sensitivity = str_to_float(request.POST['sensitivity'])
        w3 = str_to_float(request.POST['w3'])
        rb = str_to_float(request.POST['rb'])
        score = calculate_pdm_score(w1=w1, w3=w3, w2=w2, sensitivity=sensitivity, rb=rb, nsr=nsr)
        context = {
            "w1":w1, "w2" : w2, "w3" : w3, 
            "nsr" : nsr, "sensitivity": sensitivity, "rb": rb,
            "pdm_score": score
            
        }
    else:
        context = {}

    return render(request, "index.html", context)




