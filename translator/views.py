from django.shortcuts import render
from googletrans import Translator

from . import translate


# Create your views here.

def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST['my_textarea']
        output = translate.translate(original_text)
        return render(request, 'translator.html', {'output_text': output, 'original_text': original_text})
    else:
        return render(request, 'translator.html')


def translate_app(request):
    if request.method == "POST":
        lang = request.POST.get("lang", None)
        txt = request.POST.get("txt", None)
        translator = Translator()
        tr = translator.translate(txt, dest=lang)
        return render(request, 'translator.html', {"result": tr.text, "txt": txt})
    else:
        return render(request, 'translator.html')
