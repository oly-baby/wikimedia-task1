from django.test import TestCase, Client
from django.urls import reverse
from .models import Bug

# Create your tests here.


class BugModelTest(TestCase):
    def test_create_bug(self):
        bug = Bug.objects.create(
            bug_description="Test Bug",
            bug_type="error",
            bug_report_date="2023-10-07",
            bug_status="TO do"
        )
        self.assertIsInstance(bug, Bug)

    def test_bug_string_representation(self):
        bug = Bug.objects.create(
            bug_description="Test Bug",
            bug_type="error",
            bug_report_date="2023-10-07",
            bug_status="TO do"
        )
        self.assertEqual(str(bug), "Test Bug")

    def test_valid_bug_type_choices(self):
        bug = Bug.objects.create(
            bug_description="Test Bug",
            bug_type="error",
            bug_report_date="2023-10-07",
            bug_status="TO do"
        )
        self.assertIn(bug.bug_type, dict(Bug.BUG_TYPE).keys())

    def test_optional_bug_report_date(self):
        bug = Bug.objects.create(
            bug_description="Test Bug",
            bug_type="error",
            bug_status="TO do"
        )
        self.assertIsNone(bug.bug_report_date)


class IndexViewTest(TestCase):
    def test_index_view(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_view_with_bugs(self):
        Bug.objects.create(
            bug_description="Test Bug 1",
            bug_type="error",
            bug_status="TO do"
        )
        Bug.objects.create(
            bug_description="Test Bug 2",
            bug_type="new features",
            bug_status="Done"
        )
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertQuerysetEqual(response.context['all_bug'], Bug.objects.all(), ordered=False)


class CreateBugViewTest(TestCase):
    def test_create_bug_view_GET(self):
        client = Client()
        response = client.get(reverse('add_bug'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_bug.html')

    def test_create_bug_view_POST(self):
        client = Client()
        data = {
            'bug_description': 'Test Bug',
            'bug_type': 'error',
            'bug_status': 'TO do',
        }
        response = client.post(reverse('add_bug'), data)
        self.assertEqual(response.status_code, 302)  # Redirect
        self.assertRedirects(response, reverse('index'))


class ViewBugViewTest(TestCase):
    def setUp(self):
        self.bug = Bug.objects.create(
            bug_description="Test Bug",
            bug_type="error",
            bug_status="TO do"
        )

    def test_view_bug_view(self):
        client = Client()
        response = client.get(reverse('view_bug', args=(self.bug.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_bug.html')
        self.assertEqual(response.context['bug'], self.bug)

    def test_view_bug_view_with_invalid_bug(self):
        client = Client()
        response = client.get(reverse('view_bug', args=(999,)))
        self.assertEqual(response.status_code, 404)