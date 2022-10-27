from django import forms
from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "content",
            "movie_name",
            "grade",
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('review', 'user', )