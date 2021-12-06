from django.test import TestCase
from django.contrib.auth.models import User
from .models import Complaint
# from django.test import Client


class TestViews(TestCase):

    def test_get_view_complaint_list_page(self):
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
