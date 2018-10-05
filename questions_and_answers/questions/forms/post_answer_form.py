from django.forms import ModelForm

from questions.models import Answer

class PostAnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ("description",)
