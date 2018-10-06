from django.forms import ModelForm

from questions.models import AnswerComment

class ReplyToAnswerForm(ModelForm):
    class Meta:
        model = AnswerComment
        fields = ("description",)
