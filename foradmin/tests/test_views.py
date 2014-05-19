import json
from django.test import TestCase
from foradmin.models import ApiLog, UserSession

from django.contrib.auth import authenticate
from forcompany.views import fill_info

SAMPLE_ID = 'test@test.com'
SAMPLE_PASSWORD = 'test'

class UserSessionTest(TestCase):

    default_setup_api_log_count = 2

    def setUp(self):
        self.assertTrue(self.helper_registration())
        self.assertTrue(self.helper_check_api_log_count(1))
        self.assertTrue(self.helper_check_api_log_distinct_user_session_id_count(1))
        self.assertTrue(self.helper_login())
        self.assertTrue(self.helper_check_api_log_count(2))
        self.assertTrue(self.helper_check_api_log_distinct_user_session_id_count(1))


    # helper function part ----- start
    def helper_registration(self, id=SAMPLE_ID, password=SAMPLE_PASSWORD):
        response = self.client.post('/user/registration',
                                    {'email':SAMPLE_ID,
                                     'password':SAMPLE_PASSWORD,
                                     'password_confirm':SAMPLE_PASSWORD })
        response_dict = json.loads(response.content)
        if response_dict['result'] == 'success':
            return True
        else:
            return False

    def helper_logout(self):
        response = self.client.post('/user/logout')
        response_dict = json.loads(response.content)
        if response_dict['result'] == 'success':
            return True
        else:
            return False

    def helper_login(self):
        response = self.client.post('/user/login', {'email':SAMPLE_ID, 'password':SAMPLE_PASSWORD})
        response_dict = json.loads(response.content)
        if response_dict['result'] == 'success':
            return True
        else:
            return False

    def helper_check_api_log_count(self, count):
        api_log_count = ApiLog.objects.count()
        if api_log_count == count:
            return True
        else:
            return False

    def helper_check_api_log_distinct_user_session_id_count(self, count):
        api_log_distinct_user_session_id_count = ApiLog.objects.distinct('user_session_id').count()
        return api_log_distinct_user_session_id_count == count


    # helper function part ----- end

    def test_user_anonymous_session_created(self):
        self.assertTrue(self.helper_check_api_log_distinct_user_session_id_count(1))

    def test_user_anonymous_session_equal_after_re_login(self):
        self.assertTrue(self.helper_logout())
        self.assertTrue(self.helper_check_api_log_count(self.default_setup_api_log_count+1))
        self.assertTrue(self.helper_check_api_log_distinct_user_session_id_count(1))
        self.assertTrue(self.helper_login())
        self.assertTrue(self.helper_check_api_log_count(self.default_setup_api_log_count+2))
        self.assertTrue(self.helper_check_api_log_distinct_user_session_id_count(1))
        


    # def helper_response_result_success( self, response ):
    #     response_json = json.loads( response.content )
    #     self.assertEqual( response_json['result'], 'success' )
    #
    # def test_classes_get_sub_category_list(self):
    #     response = self.client.post('/classes/dance', data={} )
    #     # self.assertEqual( response.content , "" )
    #     self.helper_response_result_success( response )
    #
    # def test_classes_get_classes_list(self):
    #     response = self.client.post('/classes/dance/jazz', data={} )
    #     self.helper_response_result_success( response )

    # def test_classes_get_classes_in_overflow_page_num(self):
        # response = self.client.post('/classes/dance/jazz/9999', data={} )
        # {"error_message": "page end", "data": null, "result": "fail"}

    # def test_classes_inquire_about_classes(self):
    #     response = self.client.post('/classes/')