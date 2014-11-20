from django.test import TestCase



# Create your tests here.
class SomeTests(TestCase):
    fixtures = ['test001.json']
    def test_t1_show_contacts_on_main_page(self):
        response = self.client.get('/')
        self.assertEqual(response.context['name'], 'Serge')
        self.assertEqual(response.context['last_name'], 'Sergeev')
        self.assertEqual(response.context['date_of_birth'], '1976-01-31')
        self.assertEqual(response.context['bio'], 'Test bio')
        self.assertEqual(response.context['email'], 'simne@github.com')
        self.assertEqual(response.context['jabber'], 'simne@jabber.ru')
        self.assertEqual(response.context['skype'], 'simne100')
        self.assertEqual(response.context['other_contacts'], 'Other contacts test')

