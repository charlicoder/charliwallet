from .models import Question


def count_polls(request):
    count = Question.objects.count()
    return {'count_polls': count}
