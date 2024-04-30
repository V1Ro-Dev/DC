from django.http import HttpResponse
from django.urls import reverse


def index(request):
    bug_report_url = reverse('quality_control:bug_report')
    feature_request_url = reverse('quality_control:feature_request')
    html = (f"<h1>Система контроля качества</h1>"
            f"<a href='{bug_report_url}'>Список всех багов</a><br>"
            f"<a href='{feature_request_url}'>Запросы на улучшение</a>")
    return HttpResponse(html)


def bug_list(request):
    return HttpResponse(f"<h1> Список отчетов об ошибках </h1>")


def feature_list(request):
    return HttpResponse(f"<h1> Список запросов на улучшение </h1>")


def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")


def feature_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")
