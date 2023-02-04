from django.views import generic


# Create your views here.
class DSView_ML(generic.TemplateView):  # TemplateView: render html model without data
    template_name: str = 'rotten_tomatoes_ML .html'


class DSView_Analyse(generic.TemplateView):  # TemplateView: render html model without data
    template_name: str = 'rotten_tomatoes_type&comment_analyse.html'
