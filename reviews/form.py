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
            "image",
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = (
            "review",
            "user",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget.attrs = {
            "placeholder": "댓글을 작성해 주세요",
        }
        self.fields["content"].help_text = None
