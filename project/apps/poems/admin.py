from django.contrib import admin
from poems.models import Poem, PoemRevision, Poet

BASE_POEM_LIST_DISPLAY = [
    "author",
    "title",
    "is_draft",
    "allow_comments",
    "show_draft_revisions",
    "show_published_revisions"
]


class PoemAdmin(admin.ModelAdmin):
    list_display = BASE_POEM_LIST_DISPLAY
    model = Poem


admin.site.register(Poem, PoemAdmin)


class PoemRevisionAdmin(admin.ModelAdmin):
    list_display = ["revised_at",] + BASE_POEM_LIST_DISPLAY
    model = PoemRevision


admin.site.register(PoemRevision, PoemRevisionAdmin)


class PoetAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "premium_user",)
    model = Poet


admin.site.register(Poet, PoetAdmin)
