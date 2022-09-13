from addresses.models import Address
from django.urls import reverse
from facilities.models import Facility
from model_bakery import baker
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from users.models import User


class AddressViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = baker.make("users.User", is_owner=True)

        cls.user_2 = baker.make("users.User", is_owner=True)

        cls.user_not_owner = baker.make("users.User")

        cls.sport_facility = baker.make("facilities.Facility", user=cls.user)

        cls.address_data = {
            "street": "Antonio Azevedo",
            "number": "401",
            "zipcode": "12345",
            "state": "SP"
        }

        cls.address_data_2 = {
            "street": "Azevedo",
            "number": "01",
            "zipcode": "2345",
            "state": "RJ"
        }

        Token.objects.create(user=cls.user)

        Token.objects.create(user=cls.user_2)

        Token.objects.create(user=cls.user_not_owner)

        cls.sport_facility.address_id = Address.objects.create(**cls.address_data_2)

        cls.sport_facility.save()

    def test_create_address_view(self):
        print("test create_address_view")
        token = Token.objects.get(user__id=self.user.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.post(reverse("sport_facility_address", kwargs={"facility_id": self.sport_facility.id}), self.address_data)

        self.assertEqual(response.status_code, 201)


        expected_keys = ["id", "street", "number", "zipcode", "state"]

        for key in expected_keys:
            self.assertIn(key, response.data)

        for key in response.data.keys():
            self.assertIn(key, expected_keys)

    def test_detail_address_view(self):
        print("test detail_address_view")
        token = Token.objects.get(user__id=self.user.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        response = self.client.get(reverse("sport_facility_address", kwargs={"facility_id": self.sport_facility.id}))

        self.assertEqual(response.status_code, 200)


        for key, data in self.address_data_2.items():
            self.assertEqual(response.data[key], data)

    def test_update_address_view(self):
        print("test update_address_view")

        token = Token.objects.get(user__id=self.user.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

        updated = {"street": "Rua Cezamo"}

        response = self.client.patch(reverse("sport_facility_address", kwargs={"facility_id": self.sport_facility.id}), updated)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data["street"], updated["street"])

    def test_address_views_permissions(self):
        print("test address_views_permissions")

        not_a_owner_token = Token.objects.get(user__id=self.user_not_owner.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + not_a_owner_token.key)

        response = self.client.post(reverse("sport_facility_address", kwargs={"facility_id": self.sport_facility.id}), self.address_data)

        self.assertEqual(response.status_code, 403)

        not_the_owner_token = Token.objects.get(user__id=self.user_2.id)

        self.client.credentials(HTTP_AUTHORIZATION="Token " + not_the_owner_token.key)

        response = self.client.get(reverse("sport_facility_address", kwargs={"facility_id": self.sport_facility.id}))

        self.assertEqual(response.status_code, 403)
