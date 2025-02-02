from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from personal import models
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})

## def results_view(request, question_id):
   ## question = get_object_or_404(Question, pk=question_id)
    ##return render(request, 'results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
        pk=request.POST['choice']
        )
    except (KeyError, Choice.DoesNotExist):
 # Redisplay the question voting form
        return render(request, 'polls/template/detail.html', {
        'question': question,
        'error_message': "You didn't select a choice."
     })
    else:
        selected_choice.votes += 1
        selected_choice.save()
# Always return an HttpResponseRedirect after successfully
# dealing with POST data. This prevents data from being
# posted twice if a
# user hits the Back button.
    return HttpResponseRedirect(
    reverse('polls:results', args=(question_id,))
    )

## def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
   # return render(request, "polls/template/poll.html", context)