from django.contrib import admin
from questions.models import Question, Answer, QuestionComment, AnswerComment

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionComment)
admin.site.register(AnswerComment)
