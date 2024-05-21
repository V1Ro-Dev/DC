from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView
from quality_control.models import BugReport, FeatureRequest


def index(request):
    return render(request, 'quality_control/index.html')


def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bugs.html', {'bug_list': bugs})


def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/features.html', {'feature_list': features})


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
    template_name = 'quality_control/bug_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        return render(request, 'quality_control/bug_detail.html', {'bug': bug})


class FeatureDetail(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        return render(request, 'quality_control/feature_detail.html', {'feature': feature})
