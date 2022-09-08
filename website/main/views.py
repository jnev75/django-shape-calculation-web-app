from django.shortcuts import render
import math

# Create your views here.
def index(request):
    return render(request, "main/input.html")

def squareCalculations(request):
    if request.POST['len'].isdigit():
        len = int(request.POST['len'])
        area = len ** 2
        perimeter = len * 4
        res = []
        res.extend([area, perimeter])
    else:
        res = "Length must be specified using digits only!"

    return res

def circleCalculations(request):
    if request.POST['len'].isdigit():
        len = int(request.POST['len'])
        area = round(math.pi * math.pow(len, 2), 2)
        perimeter = round(2 * math.pi * len, 2)
        res = []
        res.extend([area, perimeter])
    else:
        res = "Length must be specified using digits only!"
        
    return res

def triangleCalculations(request):
    if request.POST['len'].isdigit():
        len = int(request.POST['len'])
        area = (len / 2) * len
        perimeter = len * 3
        res = []
        res.extend([area, perimeter])
    else:
        res = "Length must be specified using digits only!"
        
    return res

def checkShape(request):
    shape_name = request.POST['shape'];

    match shape_name:
        case "square":
            res = squareCalculations(request)
        case "circle":
            res = circleCalculations(request)
        case "triangle":
            res = triangleCalculations(request)

    return render(
        request, "main/result.html", 
        {"shape_name": shape_name, "area": res[0], "perimeter": res[1]}
    )