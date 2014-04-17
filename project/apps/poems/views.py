from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from annoying.decorators import render_to, ajax_request
from poems.models import Poem, Poet, PoemRevision


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


@ajax_request
@csrf_exempt
def save_revision(request, poet=None, title=None):
    poem = Poem.objects.get(slug__iexact=title, author__slug__iexact=poet)
    is_mine = poem.author.user == request.user
    if not is_mine:
        raise Http403("Either this isn't your poem, or you're not logged in!")
    data = request.POST
    if "body" not in data or "title" not in data:
        raise Exception("Hm, you're missing either the title, or the body.")
    poem.title = data["title"]
    poem.body = data["body"]
    poem.save()

    return {"success": True}


@render_to("poems/revisions.html")
def revisions(request, poet=None, title=None):
    poem = Poem.objects.get(slug__iexact=title, author__slug__iexact=poet)
    is_mine = poem.author.user == request.user
    if is_mine:
        revisions = poem.revisions
    elif poem.show_draft_revisions:
        if (poem.show_published_revisions):
            revisions = poem.revisions
        else:
            revisions = poem.revisions.filter(is_draft=True)
    else:
        if poem.show_published_revisions:
            revisions = poem.revisions.filter(is_draft=False)
        else:
            revisions = poem.revisions.none()

    return locals()


@render_to("poems/revision.html")
def revision(request, poet=None, pk=None):
    poem = PoemRevision.objects.get(pk=pk, author__slug__iexact=poet)
    is_mine = poem.author.user == request.user
    assert is_mine

    return locals()
