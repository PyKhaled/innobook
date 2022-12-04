from rest_framework.test import APITestCase
from rest_framework import status
from contacts.models import Contact, Number
from django.urls import reverse


class ContactTestCase(APITestCase):
    def test_create_new_contact_with_one_number(self):
        url = reverse('contacts-list')
        data = {
            "name": 'Ahmed Khaled',
            "numbers": [
                {"label": 'mobile', "dial": "+201003830742"},
                {"label": 'mobile', "dial": "+201003830742"}
            ]
        }

        res = self.client.post(url, data, format='json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(len(res.data['numbers']), len(data['numbers']))
        self.assertTrue(res.data['name'], data['name'])


    def test_create_new_contact_with_multiple_numbers(self):
        url = reverse('contacts-list')
        data = {
            "name": 'Ahmed Khaled',
            "numbers": [
                {"label": 'mobile', "dial": "+201003830742"}
            ]
        }

        res = self.client.post(url, data, format='json')

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(len(res.data['numbers']), len(data['numbers']))
        self.assertTrue(res.data['name'], data['name'])


    def test_get_all_contacts(self):
        for x in range(5):
            c = Contact.objects.create(name=f"test name {x}")
            c.numbers.create(label='123123', dial='013324234')

        url = reverse('contacts-list')
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 5)

