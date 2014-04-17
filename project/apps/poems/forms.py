from django import forms
from poems.models import Poem


class PoemForm(forms.ModelForm):
    title = forms.CharField(required=False, widget=forms.HiddenInput())
    body = forms.CharField(required=False, widget=forms.HiddenInput())
    is_draft = forms.BooleanField(widget=forms.HiddenInput())
    audio_url = forms.CharField(required=False, widget=forms.TextInput())
    video_url = forms.CharField(required=False, widget=forms.TextInput())

    class Meta:
        model = Poem
        fields = (
            "title",
            "body",
            # "slug",
            "is_draft",
            # "display_type",
            "allow_comments",
            "show_draft_revisions",
            "show_published_revisions",
            "audio_url",
            "video_url",
        )
