from django.core import serializers
from django.db.models import Prefetch
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from core.models import Article, ArticleTranslate


@csrf_exempt
def articles(request):
    qs = Article.objects.prefetch_related(
        Prefetch('articletranslate_set', queryset=ArticleTranslate.objects.select_related('language')))
    qs = qs.filter(articletranslate__language__name='English')\
        .values('articletranslate__name', 'articletranslate__body', 'date')

    # return JsonResponse(list(qs), content_type='application/json', safe=False)
    return JsonResponse(list(qs), content_type='application/json', safe=False)

