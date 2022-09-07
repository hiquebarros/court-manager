from rest_framework.test import APITestCase
from model_bakery import baker
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ErrorDetail
from users.models import User

from django.urls import reverse


class TestCourt_typeView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        
        cls.list_len = 5
        cls.court_type_sample = baker.make("court_types.Court_type", _quantity=cls.list_len)

        cls.court_type_data = {
            "sport": "test sport",
            "type": "test type"
        }

        user = User.objects.create_superuser(username="admin", password="1234")
        token, _ = Token.objects.get_or_create(user=user)
        cls.token_key = token.key


    def test_list_court_types(self):
        print("test list court types")

        response = self.client.get(reverse("court_types-view"))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.list_len, len(response.data))

        for index, court_type in enumerate(self.court_type_sample):
            sample_dict = vars(court_type)
            listed_dict = response.data[index]

            listed_dict.pop("id")    
            
            for key, data in listed_dict.items():
                self.assertEqual(data, sample_dict[key])
    
    
    def test_create_court_type(self):
        print("test create court type")

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_key)
        response = self.client.post(reverse("court_types-view"), data=self.court_type_data)

        excepted_keys = (
            "id",
            "sport",
            "type"
        )

        response_keys = tuple(response.data)
        self.assertTupleEqual(excepted_keys, response_keys)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        for key, data in self.court_type_data.items():
            self.assertEqual(response.data[key], data)


    def test_create_court_type_missing_data(self):
        print("test create court_type missing data")

        empty_data = {}

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_key)
        response = self.client.post(reverse("court_types-view"), empty_data)

        error_msg = ErrorDetail('This field is required.', 'required') 

        for _, data in response.data.items():
            self.assertEqual(*data, error_msg)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_create_court_type_with_wrong_data(self):
        print("test create court_type with wrong data")

        wrong_data = {"test": "wrong field", "another_test": "wrong field"}

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_key)
        response = self.client.post(reverse("court_types-view"), wrong_data)
        
        error_msg = ErrorDetail('This field is required.', 'required') 

        for _, data in response.data.items():
            self.assertEqual(*data, error_msg)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_create_court_type_with_extra_data(self):
        print("test create court_type with extra data")


        wrong_data = {"test": "wrong field", "another_test": "wrong field", "sport": "test sport", "type": "test type"}

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_key)
        response = self.client.post(reverse("court_types-view"), wrong_data)
        
        excepted_keys = (
            "id",
            "sport",
            "type"
        )

        response_keys = tuple(response.data)
        self.assertTupleEqual(excepted_keys, response_keys)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        for key, data in self.court_type_data.items():
            self.assertEqual(response.data[key], data)


    def test_delete_court_type(self):
        print("test delete court_type")

        target_id = str(self.court_type_sample[0].id)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_key)
        response = self.client.delete(reverse("court_types-detail-view", kwargs={"court_type_id": target_id}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    

    def test_delete_court_type_passing_wrong_id(self):
        print("test delete court_type passing wrong id")

        target_id = '12345'

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_key)
        response = self.client.delete(reverse("court_types-detail-view", kwargs={"court_type_id": target_id}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

