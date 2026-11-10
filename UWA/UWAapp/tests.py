from django.test import TestCase
from django.urls import reverse


class PublicSiteTests(TestCase):
    def test_primary_pages_render(self):
        for route in ('home', 'about', 'destinations', 'conservation', 'plan', 'contact'):
            with self.subTest(route=route):
                response = self.client.get(reverse(f'UWAapp:{route}'))
                self.assertEqual(response.status_code, 200)

    def test_destination_directory_links_to_detail_pages(self):
        response = self.client.get(reverse('UWAapp:destinations'))
        self.assertContains(response, reverse('UWAapp:destination-detail', args=['bwindi-impenetrable']))

        detail = self.client.get(reverse('UWAapp:destination-detail', args=['bwindi-impenetrable']))
        self.assertEqual(detail.status_code, 200)
        self.assertContains(detail, 'Mountain gorilla trekking')

    def test_information_pages_link_to_relevant_next_steps(self):
        response = self.client.get(reverse('UWAapp:conservation'))
        self.assertContains(response, 'href="/plan-your-visit/"')

        response = self.client.get(reverse('UWAapp:plan'))
        self.assertContains(response, 'href="/destinations/"')

    def test_unknown_destination_returns_not_found(self):
        response = self.client.get(reverse('UWAapp:destination-detail', args=['not-a-real-place']))
        self.assertEqual(response.status_code, 404)
