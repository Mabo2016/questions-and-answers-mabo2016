from django.views import generic
from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import F
from django.contrib.auth.decorators import login_required

from questions.models import Answer, Question, QuestionComment
from questions.forms import PostCommentToQuestionForm, ReplyToAnswerForm

@login_required
def post_comment_to_question(request, pk):
    if request.method == 'POST':
        form = PostCommentToQuestionForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()

            comment.refresh_from_db()

            comment.author = request.user

            question = get_object_or_404(Question, pk=pk)
            comment.question = question

            comment.save()

            return HttpResponseRedirect(reverse('question_detail', args=(pk,)))
    else:
        form = PostCommentToQuestionForm()

    return render(request, 'questions/questioncomment_post.html', {'form': form})

@login_required
def reply_to_answer(request, pk):
    if request.method == 'POST':
        form = ReplyToAnswerForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()

            comment.refresh_from_db()

            comment.author = request.user

            answer = get_object_or_404(Answer, pk=pk)
            comment.answer = answer

            comment.save()

            return HttpResponseRedirect(reverse('question_detail', args=(answer.question.id,)))
    else:
        form = ReplyToAnswerForm()

    return render(request, 'questions/answercomment_post.html', {'form': form})
