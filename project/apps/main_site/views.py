from annoying.decorators import render_to

@render_to("main_site/home.html")
def home(request):
    return locals()

@render_to("main_site/ui-mock.html")
def ui_mock(request):
    return locals()

@render_to("main_site/detail-mock.html")
def detail_mock(request):
    return locals()
