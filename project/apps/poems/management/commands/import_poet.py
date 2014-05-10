# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
import codecs
import datetime
import json
from poems.models import Poem, Poet


def load_from_source(source):
    source = json.loads(source)
    poet = Poet.objects.get_or_create(public_domain=True, archive=True, archive_name=source["name"])[0]
    poet.wikipedia_url = source["wikipedia_url"]
    poet.birthdate = datetime.datetime.strptime(source["birthdate"], "%Y-%m-%d")
    poet.deathdate = datetime.datetime.strptime(source["deathdate"], "%Y-%m-%d")
    poet.save()
    print "Importing the poems of %s:" % poet

    for p in source["poems"]:
        poem = Poem.objects.get_or_create(author=poet, public_domain=True, imported=True, title=p["title"])[0]
        print " %s" % poem
        poem.body = p["body"].replace("  ", "&nbsp;&nbsp;")
        pub_date = None
        if p["publication_date"]:
            pub_date = datetime.datetime.strptime(p["publication_date"], "%Y-%m-%d")
        poem.is_draft = False
        poem.published_at = pub_date
        poem.written_on = pub_date
        poem.started_at = pub_date
        poem.show_draft_revisions = False
        poem.show_published_revisions = False
        poem.approximate_publication_date = p["approximate_publication_date"] or False
        poem.source_url = p["source_url"] or None
        poem.save(force_longest_line_recalc=True)


class Command(BaseCommand):

    def handle(self, *args, **options):
        if len(args) == 0:
            print "You must provide the name of the file to import"
        f = codecs.open(args[0], "r", "utf-8")
        source = f.read()
        load_from_source(source)
        