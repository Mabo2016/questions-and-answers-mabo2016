from django.urls import path
from questions import views

urlpatterns = [
    path("", views.index_view.show_index, name="index"),
    path("questions", views.question_views.QuestionListView.as_view(), name="questions"),
    path("question/<int:pk>", views.question_views.QuestionDetailView.as_view(), name="question_detail"),
    path("question/question_ask", views.question_views.ask_question, name="ask_question"),
    path("question/question_vote_up/<int:pk>", views.question_views.vote_question_up, name="vote_question_up"),
    path("question/question_vote_down/<int:pk>", views.question_views.vote_question_down, name="vote_question_down"),
    path("question/<int:pk>/answer_post", views.answer_views.post_answer, name="post_answer"),
    path("question/<int:pk>/questioncomment_post", views.comment_views.post_comment_to_question, name="reply_to_question"),
    path("question/<int:pk>/answercomment_post", views.comment_views.reply_to_answer, name="reply_to_answer"),
]
