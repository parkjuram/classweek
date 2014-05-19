from django.db import models
from django.contrib.auth.models import User
import datetime

class Company(models.Model):
    name = models.TextField( unique=True )
    phone_number = models.TextField( null=True )
    location = models.TextField()
    zone = models.TextField( null=False, blank=True, default='' )
    naver_object_id = models.TextField(null=True)
    nearby_station = models.TextField( null=True )
    facilitiesInformation = models.TextField( null=False, blank=True, default='')
    thumbnail_image_url = models.TextField(null=False, blank=True, default='')
    # toilet, fitting_room, shower_stall, locker, parking_lot, practice_room, instrument_rental

    def __str__(self):
        return 'Company : %s' % self.name

    def __unicode__(self):
        return 'Company : %s' % self.name

class CompanyReview(models.Model):
    company = models.ForeignKey(Company, related_name='get_company_reviews')
    source = models.TextField(default='naver')
    content = models.TextField()
    score = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now )

class CompanyImage(models.Model):
    company = models.ForeignKey(Company, related_name='get_company_images')
    image_url = models.TextField()

class Category(models.Model):
    name = models.TextField( unique=True )

    def __str__(self):
        return 'Category : %s' % self.name

    def __unicode__(self):
        return 'Category : %s' % self.name

class SubCategory(models.Model):
    name = models.TextField(unique=True)
    category = models.ForeignKey(Category, related_name='get_subcategorys')
    name_kor = models.TextField(null=True)
    description = models.TextField(null=True)
    image_url = models.TextField(null=True)
    order_priority_number = models.IntegerField(null=False, default=0)

    def __str__(self):
        return 'SubCategory : %s' % self.name

    def __unicode__(self):
        return 'SubCategory : %s' % self.name

class SubCategoryRecommend(models.Model):
    image_url = models.TextField( null=True )

class Classes(models.Model):
    title = models.TextField( null=True )
    thumbnail_image_url = models.TextField( null=True )
    subCategory = models.ForeignKey( SubCategory, related_name='get_classes' )
    company = models.ForeignKey( Company )
    description = models.TextField( null=True )
    preparation = models.TextField( null=True )
    personalOrGroup = models.TextField( null=True )
    refundInformation = models.TextField( null=True )
    # countOfDay = models.IntegerField( null=True )
    priceOfDay = models.IntegerField( null=True )
    countOfMonth = models.IntegerField( null=True )
    priceOfMonth = models.IntegerField( null=True )
    image_url = models.TextField( null=True )

    class Meta:
        unique_together = (("title", "thumbnail_image_url", "subCategory", "company", "description", "preparation", "personalOrGroup", "refundInformation", "priceOfDay", "countOfMonth", "priceOfMonth", "image_url"),)

    def __str__(self):
        return '(%d)Classes : %s / %s' % (self.id, self.title, self.description )

    def __unicode__(self):
        return '(%d)Classes : %s / %s' % (self.id, self.title, self.description )

class ClassesImage(models.Model):
    classes = models.ForeignKey( Classes, related_name='get_images' )
    image_url = models.TextField()

class ClassesInquire(models.Model):
    classes = models.ForeignKey( Classes )
    user = models.ForeignKey( User )
    content = models.TextField( null=False, blank=True, default='' )
    created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now )

class Schedule(models.Model):
    classes = models.ForeignKey( Classes , related_name='get_schedules')
    # Mon=1, Tue=2, Wed, Thu, Fri, Sat, Sun
    dayOfWeek = models.CharField( max_length=27 )
    startTime = models.TextField( null=True )
    duration = models.TimeField( default='00:00:00')

    def __str__(self):
        return 'class_id=(%d), (%d)Schedule : %s %r' % (self.classes_id, self.id, self.dayOfWeek, self.startTime )

    def __unicode__(self):
        return 'class_id=(%d), (%d)Schedule : %s %r' % (self.classes_id, self.id, self.dayOfWeek, self.startTime )

class ClassesRecommend(models.Model):
    classes = models.ForeignKey( Classes, related_name='get_recommends')
    schedule = models.ForeignKey( Schedule, related_name='get_recommends')

    def __str__(self):
        return 'ClassesRecommend : %d %r %r' % (self.id, self.classes, self.schedule )