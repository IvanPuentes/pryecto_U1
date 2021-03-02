from django.views.generic.base import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'

class AndroidPageView(TemplateView):
    template_name = 'android.html'
    
class CPageView(TemplateView):
    template_name = 'C.html'

class JavaPageView(TemplateView):
    template_name = 'Java.html'
    
class HtmlPageView(TemplateView):
    template_name = 'html.html'

class IosPageView(TemplateView):
    template_name = 'ios.html'