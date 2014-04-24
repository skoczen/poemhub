from django import forms
from poems.models import Fantastic, Poem, Read


class PoemForm(forms.ModelForm):
    title = forms.CharField(required=False, widget=forms.HiddenInput())
    body = forms.CharField(required=False, widget=forms.HiddenInput())
    is_draft = forms.BooleanField(required=False, widget=forms.HiddenInput())
    audio_url = forms.CharField(required=False, widget=forms.TextInput())
    video_url = forms.CharField(required=False, widget=forms.TextInput())

    class Meta:
        model = Poem
        fields = (
            "title",
            "body",
            # "slug",
            "written_on",
            "is_draft",
            # "display_type",
            "allow_comments",
            "show_draft_revisions",
            "show_published_revisions",
            "audio_url",
            "video_url",
        )


class FantasticForm(forms.ModelForm):
    on = forms.BooleanField(required=False, widget=forms.HiddenInput())
    reader = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Fantastic
        fields = (
            "on",
        )


class ReadForm(forms.ModelForm):
    reader = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Read
        fields = (
            # "reader",
        )


class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=255, label='Publication Name', help_text="The name your poems will be published under.")

    def save(self, user):
        user.first_name = self.cleaned_data['first_name']
        user.save()
