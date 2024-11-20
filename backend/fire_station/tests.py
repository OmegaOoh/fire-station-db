"""Module on test fire-station."""
import json
from typing import Any
import django.test
from django import urls
from django.contrib.auth.models import User
from django.utils import timezone


class EquipmentsTest(django.test.TestCase):
    """Test case for equipments."""

    def setUp(self):
        """Set up the common URL."""
        self.url = urls.reverse("fire-station:equipments")
        self.user = User.objects.create_user(username="user", password="password")
        self.client.force_login(self.user)

    def create_equipments(self, data : dict[str, Any] = None):
        """Create equipment."""
        if not data:
            data = {"item_name": "equipments", "issue_date": timezone.now().strftime('%Y-%m-%d')}

        response = self.client.post(
            path=self.url,
            data = data
        )
        return response

    def test_no_equipments(self):
        """If no equipments, return empty list."""
        response = self.client.get(self.url)
        res_dict = json.loads(response.content)
        self.assertEqual(res_dict, [])

    def test_usable_equipments(self):
        """Usable equipments data should be returned."""
        data = {"item_name": "Helmet", "issue_date": timezone.now().strftime('%Y-%m-%d')}
        response = self.create_equipments(data = data)
        res_dict = json.loads(response.content)
        data["id"] = 1
        self.assertEqual(res_dict, [data])
