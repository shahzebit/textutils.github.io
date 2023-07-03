# python code for views of url
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse('home')
    return render(request, "index.html")


def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    if (removepunc == "on"):
        punctuations = "!?';:\|/><-=,.()[]{}@..."
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext= analyzed

        params = {'purpose': 'Performed the operations', 'analyzed_text': analyzed}
    if (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Performed the operations', 'analyzed_text': analyzed}
        djtext= analyzed

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !='\n':
                analyzed = analyzed + char
        params = {'purpose': 'Performed the operations', 'analyzed_text': analyzed}
        djtext = analyzed
    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Performed the operation', 'analyzed_text': analyzed}
        djtext = analyzed
    if (charcount == "on"):
        analyzed = 0
        for char in djtext:
                analyzed = analyzed + 1
        params = {'purpose': 'Performed the operations ', 'analyzed_text': analyzed}
        djtext = analyzed
    if charcount != "on" and extraspaceremover != "on" and newlineremover != "on" and fullcaps != "on" and removepunc != "on":
        return HttpResponse("Invalid operation Try again")
    return render(request, 'analyze.html', params)
