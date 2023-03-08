from django import forms
from . import models


class TvShowForm(forms.ModelForm):
    class Meta:
        model = models.TVShow
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.RatingTv
        fields = "__all__"
