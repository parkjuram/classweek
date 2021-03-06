# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from classes.models import Classes, Schedule
from datetime import datetime


class ApiLog(models.Model):
    user_session_id = models.TextField(null=False, blank=True, default='')
    path_name = models.TextField(null=False, blank=True, default='')
    view_name = models.TextField(null=False, blank=True, default='')
    request_params = models.TextField(null=False, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return 'ApiLog : %r' % self.user_session_id


class UserSession(models.Model):
    user = models.ForeignKey(User, related_name='get_sessions')
    user_session_id = models.TextField(null=False, blank=True, default='')

    class Meta:
        unique_together = ("user", "user_session_id")


class PaymentLog(models.Model):
    p_status = models.CharField(max_length=5, default='')
    p_tid = models.CharField(max_length=40, default='', primary_key=True)
    p_type = models.CharField(max_length=10, default='') # ISP(신용카드 ISP), CARD(신용카드 안심클릭), HPMN(해피머니), CULTURE(문화상품권), MOBILE(휴대폰), VBANK(가상계좌), BANK(계좌이체)
    p_auth_dt = models.CharField(max_length=14, default='') # YYYYmmddHHmmss
    p_mid = models.CharField(max_length=10, default='')
    p_oid = models.CharField(max_length=100, default='', unique=True)
    p_amt = models.CharField(max_length=8, default='')
    p_uname = models.CharField(max_length=30, default='')
    p_rmesg1 = models.CharField(max_length=500, default='')
    p_rmesg2 = models.CharField(max_length=500, default='')
    p_noti = models.CharField(max_length=1024, default='')
    p_fn_cd1 = models.CharField(max_length=4, default='')
    p_auth_no = models.CharField(max_length=30, default='')
    p_card_issuer_code = models.CharField(max_length=2, default='')
    p_card_num = models.TextField(default='')
    p_card_member_num = models.TextField(default='')
    p_card_purchase_code = models.TextField(default='')
    p_card_prtc_code = models.CharField(max_length=1, default='') # 부분취소가능 : 1, 부분취소불가능 : 0
    p_hpp_corp = models.CharField(max_length=3, default='')
    p_vact_num = models.CharField(max_length=20, default='') # 입금마감 일자 yyyymmdd
    p_vact_date = models.CharField(max_length=8, default='') # 입금마감 시간 hhmmss
    p_vact_time = models.CharField(max_length=6, default='')
    p_vact_name = models.TextField(default='')
    p_vact_bank_code = models.CharField(max_length=2, default='')
    created = models.DateTimeField(null=False, auto_now=True, default=datetime.now)

    def __unicode__(self):
        return 'PaymentLog : (p_tid)%r' % self.p_tid


class Purchase(models.Model):
    payment_log = models.OneToOneField(PaymentLog, primary_key=True)
    user = models.ForeignKey(User, related_name='get_purchases')
    classes = models.ForeignKey(Classes, related_name='get_purchases')
    schedule = models.ForeignKey(Schedule, related_name='get_purchases')
    day_or_month = models.TextField(null=False, blank=True, default='month') # day | month
    class_start_datetime = models.DateTimeField(null=False, default=datetime.now)
    class_end_datetime = models.DateTimeField(null=False, default=datetime.now)
    price = models.IntegerField(null=False, default=0)
    state = models.IntegerField(null=False, default=0) # 0:대기, 1:승인, 2:미승인, 3:환불
    created = models.DateTimeField(null=False, auto_now=True)

    def __unicode__(self):
        return 'Purchase: (payment_log)%r' % self.payment_log

class QuitReasonRequest(models.Model):
    quit_reason_code = models.IntegerField(null=False, default=0)
    request_count = models.IntegerField(null=False, default=0)

    def __unicode__(self):
        return '(%r)QuitReasonRequest : quit_reason_code(%r) request_count(%r) ' \
               % (self.id, self.quit_reason_code, self.request_count)

    def __str__(self):
        return unicode(self).encode('utf-8')

class LocationRequest(models.Model):
    location_name = models.TextField(primary_key=True)
    request_count = models.IntegerField(null=False, default=0)

    def __unicode__(self):
        return '(%r)LocationRequest : location_name(%r) request_count(%r) ' \
               % (self.id, self.location_name, self.request_count)

    def __str__(self):
        return unicode(self).encode('utf-8')

class CategoryRequest(models.Model):
    category_name = models.TextField(primary_key=True)
    request_count = models.IntegerField(null=False, default=0)

    def __unicode__(self):
        return '(%r)CategoryRequest : location_name(%r) request_count(%r) ' \
               % (self.id, self.location_name, self.request_count)

    def __str__(self):
        return unicode(self).encode('utf-8')