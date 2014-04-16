from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404
from annoying.decorators import render_to
from poems.models import Poem, Poet


@render_to("poems/home.html")
def home(request):
    return locals()


def my_writing(request):
    try:
        poet = request.user.get_profile()
        return HttpResponseRedirect(reverse("poems:poet", args=(poet.slug,)))
    except:
        return HttpResponseRedirect(reverse("django.contrib.auth.views.login",))

@render_to("poems/poet.html")
def poet(request, poet=None):
    poet = Poet.objects.get(slug__iexact=poet)
    if poet.user == request.user:
        is_me = True
        poems = Poem.objects.filter(author=poet)
    else:
        is_me = False
        poems = Poem.objects.filter(author=poet, is_draft=False)
    return locals()


@render_to("poems/poem.html")
def poem(request, poet=None, title=None):
    poem = Poem.objects.get(slug__iexact=title, author__slug__iexact=poet)
    is_mine = poem.author.user == request.user
    if not is_mine and poem.is_draft:
        raise Http404("Poem not found. Maybe it never was, maybe it's a draft and you're not logged in!")
    return locals()


@render_to("poems/revisions.html")
def revisions(request, poet=None, title=None):
    poem = Poem.objects.get(slug__iexact=title, author__slug__iexact=poet)
    is_mine = poem.author.user == request.user
    revisions = poem.revisions
    return locals()
