from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from quality_control.models import BugReport, FeatureRequest


def index(request):
    bug_report_url = reverse('quality_control:bug_report')
    feature_request_url = reverse('quality_control:feature_request')
    html = (f"<h1>Система контроля качества</h1>"
            f"<a href='{bug_report_url}'>Список всех багов</a><br>"
            f"<a href='{feature_request_url}'>Запросы на улучшение</a>")
    return HttpResponse(html)


def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список всех багов:</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}, статус: {bug.status}</a></li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)


def feature_list(request):
    features = FeatureRequest.objects.all()
    feature_html = '<h1>Список всех запросов на улучшение:</h1><ul>'
    for feature in features:
        feature_html += f'<li><a href="{feature.id}/">{feature.title}, статус: {feature.status}</a></li>'
    feature_html += '</ul>'
    return HttpResponse(feature_html)


class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_report_url = reverse('quality_control:bug_report')
        feature_request_url = reverse('quality_control:feature_request')
        html = (f"<h1>Система контроля качества</h1>"
                f"<a href='{bug_report_url}'>Список всех багов</a><br>"
                f"<a href='{feature_request_url}'>Запросы на улучшение</a>")
        return HttpResponse(html)


class BugDetail(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        response_html = f'<h1>{bug.title}</h1><p>Описание: {bug.description}</p><p>Статус: {bug.status}</p><p>Уровень приоритета: {bug.priority}</p><p>Проект: {bug.project}</p><p>Связанная задача: {bug.task}</p>'
        return HttpResponse(response_html)


class FeatureDetail(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = f'<h1>{feature.title}</h1><p>Описание: {feature.description}</p><p>Статус: {feature.status}</p><p>Уровень приоритета: {feature.priority}</p><p>Проект: {feature.project}</p><p>Связанная задача: {feature.task}</p>'
        return HttpResponse(response_html)
