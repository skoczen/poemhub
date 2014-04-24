import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from utils.slughifi import unique_slug, slughifi
from main_site.models import BaseModel

POEM_DISPLAY_TYPES = [
    ("poetry", "poetry"),
    ("prose", "Prose"),
    ("spoken_word", "Spoken Word"),
]


class Poet(BaseModel):
    user = models.ForeignKey("auth.User")
    premium_user = models.BooleanField(default=False)
    slug = models.CharField(max_length=255, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = unique_slug(self, 'name', 'slug')
        super(Poet, self).save(*args, **kwargs)

    @property
    def name(self):
        return self.user.first_name

    def __unicode__(self):
        return "%s" % self.name


class Collection(BaseModel):
    author = models.ForeignKey(Poet)
    title = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=800, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = unique_slug(self, 'title', 'slug')
        super(Collection, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" % self.title


class AbstractPoem(BaseModel):
    author = models.ForeignKey(Poet)
    title = models.TextField(blank=True, null=True, default="Title")
    body = models.TextField(blank=True, null=True, default="Body")

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
    written_on = models.DateField(blank=True, null=True, default=datetime.date.today())
    slug = models.CharField(max_length=800, blank=True, verbose_name="url")

    def save(self, *args, **kwargs):
        if not self.published_at and not self.is_draft:
            self.published_at = datetime.datetime.now()

        make_revision = False
        if not self.pk:
            make_revision = True
            self.slug = unique_slug(self, 'title', 'slug', generate_new=True)
        else:
            old_me = Poem.objects.get(pk=self.pk)
            if slughifi(old_me.title) != slughifi(self.title):
                self.slug = unique_slug(self, 'title', 'slug', generate_new=True)

            if old_me.title != self.title or old_me.body != self.body:
                make_revision = True

        super(Poem, self).save(*args, **kwargs)

        if make_revision:
            INVALID_FIELDS = ["written_on", "started_at", "published_at", "id", "pk", "slug"]
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
        return self.poemrevision_set.all().order_by("-revised_at")[0]

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

    @property
    def num_fantastics(self):
        return self.fantastic_set.filter(on=True).count()

    @property
    def num_reads(self):
        return self.read_set.all().count()        

    def __unicode__(self):
        return "%s" % self.title

    class Meta:
        ordering = ("-started_at",)


class PoemRevision(AbstractPoem):
    revised_at = models.DateTimeField(auto_now_add=True, editable=False)
    poem = models.ForeignKey(Poem)

    class Meta:
        ordering = ("-revised_at",)

    def __unicode__(self):
        return "%s (%s)" % (self.title, self.revised_at)


class Fantastic(BaseModel):
    poem = models.ForeignKey(Poem)
    marked_at = models.DateTimeField(auto_now_add=True, editable=False)
    on = models.BooleanField(default=True)

    reader = models.ForeignKey(Poet, blank=True, null=True)


class Read(BaseModel):
    poem = models.ForeignKey(Poem)
    read_at = models.DateTimeField(auto_now_add=True, editable=False)

    reader = models.ForeignKey(Poet, blank=True, null=True)

    # class Meta:
    #     ordering = ("-read_at",)


def create_user_profile(sender, instance, created, **kwargs):
    if created and not Poet.objects.filter(user=instance).count() > 0:
        Poet.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User, dispatch_uid="create_user_profile")
