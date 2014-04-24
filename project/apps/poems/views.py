from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from annoying.decorators import render_to, ajax_request
from poems.models import Fantastic, Poem, Poet, PoemRevision, Read
from poems.forms import FantasticForm, PoemForm, ReadForm


@render_to("poems/home.html")
def home(request):
    return locals()


def my_writing(request):
    try:
        poet = request.user.get_profile()
        return HttpResponseRedirect(reverse("poems:poet", args=(poet.slug,)))
    except:
        return HttpResponseRedirect("%s?next=%s" % (reverse("account_login",), reverse("poems:my_writing")))


@render_to("poems/explore.html")
def explore(request):
    return locals()


@render_to("poems/my_reading.html")
@login_required
def my_reading(request):
    return locals()


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
    if is_mine:
        form = PoemForm(instance=poem)
    else:
        fantastic_form = FantasticForm()
        read_form = ReadForm()

    if not is_mine and poem.is_draft:
        raise Http404("Poem not found. Maybe it never was, maybe it's a draft and you're not logged in!")
    return locals()


@ajax_request
def save_revision(request, poet=None, title=None):
    new_url = None
    poem = Poem.objects.get(slug__iexact=title, author__slug__iexact=poet)
    old_slug = poem.slug
    was_published = not poem.is_draft
    is_mine = poem.author.user == request.user
    if not is_mine:
        raise Exception("Either this isn't your poem, or you're not logged in!")

    success = False
    form = PoemForm(request.POST, instance=poem)
    if form.is_valid():
        new_poem = form.save()
        success = True
        if old_slug != new_poem.slug or not was_published and not new_poem.is_draft:
            new_url = reverse("poems:poem", args=(poem.author.slug, new_poem.slug,))
    else:
        print form

    return {"success": success, "new_url": new_url}


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


def new(request):
    poet = Poet.objects.get(user=request.user)
    poem = Poem.objects.create(author=poet)
    return HttpResponseRedirect("%s?editing=true" % reverse("poems:poem", args=(poem.author.slug, poem.slug,)))


@ajax_request
def this_was_fantastic(request, poem_id):
    poem = Poem.objects.get(pk=poem_id)

    fantastic_form = FantasticForm(request.POST)
    if fantastic_form.is_valid():
        fantastic = fantastic_form.save(commit=False)
        fantastic.poem = poem
        if request.user.is_authenticated():
            fantastic.reader = request.user.get_profile()
        else:
            fantastic.reader = None
        fantastic.save()

        return {"success": True, "num_people": poem.num_fantastics}

    return {"success": False}


@ajax_request
def mark_read(request, poem_id):
    poem = Poem.objects.get(pk=poem_id)
    read_form = ReadForm(request.POST)
    if read_form.is_valid():
        read = read_form.save(commit=False)
        read.poem = poem
        if request.user.is_authenticated():
            read.reader = request.user.get_profile()
        else:
            read.reader = None
        read.save()

    return {"success": True, "num_reads": poem.num_reads}