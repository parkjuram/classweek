# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from classweek.custom_modules.INImx import INImx
import logging

logger = logging.getLogger(__name__)

def payment_startweb_test_view(request):
    logger.debug("this is a debug message!")

    payment_next_url = request.build_absolute_uri(reverse('payment_next_test', args=[]))
    payment_return_url = request.build_absolute_uri(reverse('payment_return_test', args=[]))
    return render(request, 'payment_startweb_test.html',
                  {'payment_next_url': payment_next_url,
                   'payment_return_url': payment_return_url})

@csrf_exempt
def payment_next_test_view(request):
    inimx = INImx(request)

    inimx.reqtype = "PAY"
    inimx.inipayhome = "/home/ts/INIpay50/" # 로그기록 경로 (이 위치의 하위폴더에 log폴더 생성 후 log폴더에 대해 777 권한 설정)

    logger.debug('def payment_next_test_view(request):')
    logger.debug( request.GET )
    logger.debug( request.POST )

    # print inimx.P_TID

    return HttpResponse('payment_next_test_view')

@csrf_exempt
def payment_return_test_view(request):

    logger.debug('def payment_return_test_view(request):')
    logger.debug( request.GET )
    logger.debug( request.POST )

    return HttpResponse('payment_return_test_view')