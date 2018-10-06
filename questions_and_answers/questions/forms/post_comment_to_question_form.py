from django.forms import ModelForm

from questions.models import QuestionComment

class PostCommentToQuestionForm(ModelForm):
    class Meta:
        model = QuestionComment
        fields = ("description",)
