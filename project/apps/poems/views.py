from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
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
        poems = Poem.objects.filter(author=poet)
    else:
        poems = Poem.objects.filter(author=poet, is_draft=False)
    return locals()


@render_to("poems/poem.html")
def poem(request, poet=None, title=None):
    poem = Poem.objects.get(slug__iexact=title, author__slug__iexact=poet)
    is_mine = poem.author.user == request.user
    return locals()


@render_to("poems/revisions.html")
def revisions(request, poet=None, title=None):
    poem = Poem.objects.get(slug__iexact=title, author__slug__iexact=poet)
    is_mine = poem.author.user == request.user
    revisions = poem.revisions
    return locals()
