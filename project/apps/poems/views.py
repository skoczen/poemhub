from annoying.decorators import render_to
from poems.models import Poem


@render_to("poems/home.html")
def home(request):
    return locals()


@render_to("poems/poem.html")
def poem(request, poet=None, title=None):
    poem = Poem.objects.get(slug__iexact=title, author__slug__iexact=poet)
    return locals()


@render_to("poems/revisions.html")
def revisions(request, poet=None, title=None):
    poem = Poem.objects.get(slug__iexact=title, author__slug__iexact=poet)
    revisions = poem.revisions
    return locals()
