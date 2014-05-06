from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^import/all', 'classes.views.import_all_view', name='import_all'),
    url(r'^import/category', 'classes.views.import_category_csv_file_view', name='import_category_csv_file'),
    url(r'^import/subcategory', 'classes.views.import_sub_category_csv_file_view', name='import_sub_category_csv_file'),
    url(r'^import/company', 'classes.views.import_company_csv_file_view', name='import_company_csv_file'),
    url(r'^import/classes', 'classes.views.import_classes_csv_file_view', name='import_classes_csv_file'),
    url(r'^import/schedule', 'classes.views.import_schedule_csv_file_view', name='import_schedule_csv_file'),
    url(r'^import/recommend/subcategory', 'classes.views.import_sub_category_recommend_csv_file_view', name='import_sub_category_recommend_csv_file'),
    url(r'^recommend/subcategory$', 'classes.views.recommend_subcategory_view', name='recommend_subcategory'),
    url(r'^recommend/classes$', 'classes.views.recommend_classes_view', name='recommend_classes'),
    url(r'^nowtaking$', 'classes.views.nowtaking_view', name='nowtaking'),
    url(r'^([A-Za-z_]+)$', 'classes.views.get_sub_category_list_view', name='getSubCategoryList'),
    url(r'^([A-Za-z_]+)\/([A-Za-z_]+)$', 'classes.views.getClassesList_view', name='getClassesList'),
    url(r'^([A-Za-z_]+)\/([A-Za-z_]+)\/(\d+)$', 'classes.views.getClassesList_view', name='getClassesList'),
    url(r'^(\d+)\/(\d+)$', 'classes.views.getClassesDetail_view', name='getClassesDetail'),
    url(r'^(\d+)\/inquire$', 'classes.views.inquire_view', name='inquire'),
)
