from annoying.decorators import render_to

@render_to("main_site/home.html")
def home(request):
    return locals()

@render_to("main_site/manifesto.html")
def manifesto(request):
    return locals()

@render_to("main_site/faq.html")
def faq(request):
    return locals()

@render_to("main_site/terms.html")
def terms(request):
    return locals()
