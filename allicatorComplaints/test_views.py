"""
1 - Importing test case from django
2 - Importing user model to set up test user
3 - Importing complaint model to use in tests
"""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Complaint


class TestViews(TestCase):
    """
    Creating class to run tests for views.
    """

    def test_get_view_complaint_list_page(self):
        """
        TEST GET VIEW COMPLAINT LIST PAGE
        This first test tests the behaviour of the
        ViewComplaintList class based view.
        As protected by authentication, create a testuser
        then use the force_login method to login test user.
        From there, the tests are run.
        Firstly we check that the HTTP code is 200 (successful)
        Finally, we check that the view is serving the correct
        template.
        """
        testuser = User.objects.create(
            username='testuser',
            password='pwd',
            is_active=1,
            is_staff=1
        )
        self.client.force_login(testuser, backend=None)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_add_complaint_page(self):
        """
        TEST GET ADD COMPLAINT PAGE
        This test tests the behaviour of the
        add_complaint function based view.
        As protected by authentication, create a testuser
        then use the force_login method to login test user.
        From there, the tests are run.
        Firstly we check that the HTTP code is 200 (successful)
        Finally, we check that the view is serving the correct
        template.
        """
        testuser = User.objects.create(
            username='testuser',
            password='pwd',
            is_active=1,
            is_staff=1
        )
        self.client.force_login(testuser, backend=None)
        response = self.client.get('/add-complaint')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_complaint.html')

    def test_get_edit_complaint_page(self):
        """
        TEST GET EDIT COMPLAINT PAGE
        This test tests the behaviour of the
        edit_complaint function based view.
        As protected by authentication, create a testuser
        then use the force_login method to login test user.
        From there, the tests are run.
        Firstly we check that the HTTP code is 200 (successful)
        Finally, we check that the view is serving the correct
        template.
        """
        testuser = User.objects.create(
            username='testuser',
            password='pwd',
            is_active=1,
            is_staff=1
        )
        self.client.force_login(testuser, backend=None)
        complaint = Complaint.objects.create(
            log_number='123456',
            customer_surname='Testing',
            complaint_category='Testing category',
            date_logged='2021-12-03',
            case_owner=testuser,
            welcome_email=True,
            customer_contacted=False,
            holding_correspondence=False,
            outstanding_actions=False,
            latest_update='Latest update test',
            )
        response = self.client.get(f'/edit-complaint/{complaint.log_number}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_complaint.html')

    def test_can_add_complaint(self):
        """
        TEST CAN ADD COMPLAINT
        This test tests the CREATE aspect of the
        apps CRUD functionality.
        As protected by authentication, create a testuser
        then use the force_login method to login test user.
        Following the force login, I create a test complaint
        with valid data and check that the post submission with
        valid data redirects to the ROOT directory (homepage).
        """
        testuser = User.objects.create(
            username='testuser',
            password='pwd',
            is_active=1,
            is_staff=1
        )
        self.client.force_login(testuser, backend=None)
        response = self.client.post(
            '/add-complaint',
            {
                'log_number': '1234567',
                'customer_surname': 'TestingAddComplaint',
                'complaint_category': 'TestAddComplaint',
                'date_logged': '2021-12-03',
                'case_owner': testuser,
                'welcome_email': True,
                'customer_contacted': True,
                'holding_correspondence': False,
                'outstanding_actions': True,
                'latest_update': 'Latest Update Text Area'
            })
        self.assertRedirects(response, '/')

    def test_can_delete_complaint(self):
        """
        TEST CAN DELETE COMPLAINT
        This test tests the DELETE aspect of the
        apps CRUD functionality.
        As protected by authentication, create a testuser
        then use the force_login method to login test user.
        Following the force login, I create a test complaint
        with valid data only this time I'm creating the complaint
        directly in the database. I then call the delete-complaint
        URL and cpass in the log number of the complaint.
        I run a check on the redirect url which again is directing
        to the home page. Then I assign the complaint I just deleted
        to a variable and check its length is equal to 0, as expected
        the delete function has reduced the objects in the db to 0.
        """
        testuser = User.objects.create(
            username='testuser',
            password='pwd',
            is_active=1,
            is_staff=1
        )
        self.client.force_login(testuser, backend=None)
        complaint = Complaint.objects.create(
            log_number='123456',
            customer_surname='Testing',
            complaint_category='Testing category',
            date_logged='2021-12-03',
            case_owner=testuser,
            welcome_email=True,
            customer_contacted=False,
            holding_correspondence=False,
            outstanding_actions=False,
            latest_update='Latest update test',
            )
        response = self.client.get(
            f'/delete-complaint/{complaint.log_number}/'
            )
        self.assertRedirects(response, '/')
        existing_complaint = Complaint.objects.filter(
            log_number=complaint.log_number
            )
        self.assertEqual(len(existing_complaint), 0)
