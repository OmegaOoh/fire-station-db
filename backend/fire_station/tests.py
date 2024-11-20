"""Module on test fire-station."""
import json
import django.test
from django import urls
from django.contrib.auth.models import User
from django.utils import timezone
from fire_station import models


class EquipmentsTest(django.test.TestCase):
    """Test case for equipments."""

    def setUp(self):
        """Set up the common URL."""
        self.url = urls.reverse("fire-station:equipments")
        self.user = User.objects.create_user(username="user", password="password")
        self.client.force_login(self.user)

    def create_equipments(self, name: str = "equipment", date = None):
        """Create equipment."""
        if not date:
            date = timezone.now().strftime('%Y-%m-%d')

        data = {"item_name": name, "issue_date": date}

        response = self.client.post(
            path = self.url,
            data = data
        )
        eq_id = response.data.get('id')
        equipment = models.Equipment.objects.get(id=eq_id)
        return response, equipment

    def test_no_equipments(self):
        """If no equipments, return empty list."""
        response = self.client.get(self.url)
        res_dict = json.loads(response.content)
        self.assertEqual(res_dict, [])

    def test_usable_equipments(self):
        """Usable equipments data should be returned."""
        data = {"item_name": "Helmet", "issue_date": timezone.now().strftime('%Y-%m-%d')}
        response, equipment = self.create_equipments(name = data['item_name'], date = data['issue_date'])
        res_dict = json.loads(response.content)

        expected = {'id': equipment.id, 'item_name': equipment.item_name, 'issue_date': equipment.issue_date.strftime('%Y-%m-%d')}
        self.assertEqual(res_dict['equipments'], [expected])
        self.assertEqual(response.status_code, 201)

    def test_delete_equipment(self):
        """The equipments data should be deleted when destroyed."""
        data = {"item_name": "Helmet", "issue_date": timezone.now().strftime('%Y-%m-%d')}
        response, equipment = self.create_equipments(name = data['item_name'], date = data['issue_date'])

        url = self.url + f"?equipments_to_remove={equipment.id}"
        response = self.client.delete(path = url, data={})
        res_dict = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res_dict,[])

    def test_on_board_equipment(self):
        """On board equipments (unusable) data should not be returned."""
        data = {"issue_date": timezone.now().strftime('%Y-%m-%d')}
        _, usable_equipment = self.create_equipments(name="Helmet", date=data['issue_date'])
        _, on_board_equipment = self.create_equipments(name="Gloves", date=data['issue_date'])

        usable = {'id': usable_equipment.id, 'item_name': usable_equipment.item_name,
                    'issue_date': usable_equipment.issue_date.strftime('%Y-%m-%d')}
        on_board = {'id': on_board_equipment.id, 'item_name': on_board_equipment.item_name,
                    'issue_date': on_board_equipment.issue_date.strftime('%Y-%m-%d')}

        response = self.client.get(self.url)
        res_dict = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res_dict,[usable, on_board])

        fire_engine = models.FireEngine.objects.create(engine_number=1, model="Fire Engine", license_plate='license')
        fire_engine.equipments.add(on_board_equipment)

        response = self.client.get(self.url)
        res_dict = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res_dict, [usable])
