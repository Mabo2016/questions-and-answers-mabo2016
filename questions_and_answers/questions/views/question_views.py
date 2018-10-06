from django.views import generic
from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import F
from django.contrib.auth.decorators import login_required

from questions.models import Question
from questions.forms import AskQuestionForm

class QuestionListView(generic.ListView):
    model = Question
    paginate_by = 50

class QuestionDetailView(generic.DetailView):
    model = Question

@login_required
def ask_question(request):
    if request.method == 'POST':
        form = AskQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()

            question.refresh_from_db()
            question.author = request.user
            question.save()

            return HttpResponseRedirect(reverse('question_detail', args=(question.id,)))
    else:
        form = AskQuestionForm()

    return render(request, 'questions/question_ask.html', {'form': form})

def vote_question_up(request, pk):
    question = get_object_or_404(Question, pk=pk)
    Question.objects.filter(pk=pk).update(up_votes_count=F('up_votes_count') + 1)
    return HttpResponseRedirect(reverse('question_detail', args=(pk,)))

def vote_question_down(request, pk):
    question = get_object_or_404(Question, pk=pk)
    Question.objects.filter(pk=pk).update(down_votes_count=F('down_votes_count') + 1)
    return HttpResponseRedirect(reverse('question_detail', args=(pk,)))
