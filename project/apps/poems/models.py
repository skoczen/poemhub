import datetime
from django.db import models
from django.template.defaultfilters import slugify
from main_site.models import BaseModel

POEM_DISPLAY_TYPES = [
    ("poetry", "Poetry"),
    ("prose", "Prose"),
    ("spoken_word", "Spoken Word"),
]


class Poet(BaseModel):
    user = models.ForeignKey("auth.User")
    name = models.CharField(max_length=255, blank=True, null=True, help_text="The name you would like your poetry published under.")
    premium_user = models.BooleanField(default=False)
    slug = models.CharField(max_length=255, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Poet, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" % self.name


class Collection(BaseModel):
    author = models.ForeignKey(Poet)
    title = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=800, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Collection, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" % self.title


class AbstractPoem(BaseModel):
    author = models.ForeignKey(Poet)
    title = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)

    is_draft = models.BooleanField(default=True)
    display_type = models.CharField(max_length=50, choices=POEM_DISPLAY_TYPES, default=POEM_DISPLAY_TYPES[0][0])
    allow_comments = models.BooleanField(default=True)
    show_draft_revisions = models.BooleanField(default=True)
    show_published_revisions = models.BooleanField(default=True)

    audio_url = models.TextField(blank=True, null=True)
    video_url = models.TextField(blank=True, null=True)

    def __unicode__(self, *args, **kwargs):
        return self.title

    class Meta:
        abstract = True


class Poem(AbstractPoem):
    started_at = models.DateTimeField(blank=True, null=True, editable=False, auto_now_add=True)
    published_at = models.DateTimeField(blank=True, null=True, editable=False)
    slug = models.CharField(max_length=800, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        if not self.published_at and not self.is_draft:
            self.published_at = datetime.datetime.now()

        make_revision = False
        if not self.pk:
            make_revision = True
        else:
            old_me = Poem.objects.get(pk=self.pk)
        if old_me.title != self.title or old_me.body != self.body:
            make_revision = True

        super(Poem, self).save(*args, **kwargs)

        if make_revision:
            INVALID_FIELDS = ["started_at", "published_at", "id", "pk", "slug"]
            poem_dict = {}
            for k, v in self.__dict__.items():
                if k not in INVALID_FIELDS and k[0] != "_":
                    poem_dict[k] = v
            poem_dict["poem"] = self
            PoemRevision.objects.create(**poem_dict)

    @property
    def date(self):
        if not self.is_draft:
            return self.published_at
        else:
            return self.most_recent_revision.revised_at

    @property
    def most_recent_revision(self):
        return self.poemrevision_set.all().order_by("revised_at")[0]

    @property
    def has_been_revised(self):
        return self.poemrevision_set.all().count() > 1

    @property
    def revisions(self):
        return self.poemrevision_set.all()

    @property
    def revisions_visible(self):
        return (
                (self.is_draft and self.show_draft_revisions) or
                (not self.is_draft and self.show_published_revisions)
               ) and self.has_been_revised

    def __unicode__(self):
        return "%s" % self.title


class PoemRevision(AbstractPoem):
    revised_at = models.DateTimeField(auto_now_add=True, editable=False)
    poem = models.ForeignKey(Poem)

    class Meta:
        ordering = ("-revised_at",)

    def __unicode__(self):
        return "%s (%s)" % (self.title, self.revised_at)
