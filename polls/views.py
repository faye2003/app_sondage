from django.shortcuts import get_object_or_404, render
from django.shortcuts import Http404

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    # output = ", ".join([q.question_text for q in latest_question_list])
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {
        "question": question
    })

# def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {
#         "question": question
#     })


def results(request, question_id):
    response = "Vous regardez les résultats de la question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Vous avez voté sur la question %s." % question_id)