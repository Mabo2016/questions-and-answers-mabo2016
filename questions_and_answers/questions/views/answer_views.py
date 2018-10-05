from django.views import generic
from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import F
from django.contrib.auth.decorators import login_required

from questions.models import Answer
from questions.models import Question
from questions.forms import PostAnswerForm

class AnswerListView(generic.ListView):
    model = Answer
    paginate_by = 50

class AnswerDetailView(generic.DetailView):
    model = Answer

@login_required
def post_answer(request, pk):
    if request.method == 'POST':
        form = PostAnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.save()

            answer.refresh_from_db()
            answer.author = request.user
            question = get_object_or_404(Question, pk=pk)
            answer.question = question
            answer.save()

            return HttpResponseRedirect(reverse('question_detail', args=(pk,)))
    else:
        form = PostAnswerForm()

    return render(request, 'questions/answer_post.html', {'form': form})

def vote_answer_up(request, pk):
    Answer.objects.filter(pk=pk).update(up_votes_count=F('up_votes_count') + 1)
    return HttpResponseRedirect(reverse('question_detail', args=(pk,)))

def vote_answer_down(request, pk):
    Answer.objects.filter(pk=pk).update(down_votes_count=F('down_votes_count') + 1)
    return HttpResponseRedirect(reverse('question_detail', args=(pk,)))
