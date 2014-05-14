from django.contrib import admin
from poems.models import Backup, Fantastic, Poem, PoemRevision, Poet, Read

BASE_POEM_LIST_DISPLAY = [
    "title",
    "author",
    "longest_line",
    "is_draft",
    "allow_comments",
    "show_draft_revisions",
    "show_published_revisions"
]


class PoemAdmin(admin.ModelAdmin):
    list_display = BASE_POEM_LIST_DISPLAY
    search_fields = ["title", "body", ]
    model = Poem


admin.site.register(Poem, PoemAdmin)


class PoemRevisionAdmin(admin.ModelAdmin):
    list_display = ["revised_at", ] + BASE_POEM_LIST_DISPLAY
    search_fields = ["title", "body", ]
    model = PoemRevision


admin.site.register(PoemRevision, PoemRevisionAdmin)


class PoetAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "slug", "premium_user",)
    model = Poet


admin.site.register(Poet, PoetAdmin)


class FantasticAdmin(admin.ModelAdmin):
    list_display = ("poem", "reader", "on", "marked_at",)
    model = Fantastic


admin.site.register(Fantastic, FantasticAdmin)


class ReadAdmin(admin.ModelAdmin):
    list_display = ("poem", "reader", "read_at",)
    model = Read


admin.site.register(Read, ReadAdmin)



class BackupAdmin(admin.ModelAdmin):
    list_display = ("poet", "backup_at",)
    model = Backup


admin.site.register(Backup, BackupAdmin)
