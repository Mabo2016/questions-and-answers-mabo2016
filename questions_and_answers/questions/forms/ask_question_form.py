from django.forms import ModelForm

from questions.models import Question

class AskQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ("title", "description",)
