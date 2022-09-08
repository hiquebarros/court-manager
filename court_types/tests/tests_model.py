from django.test import TestCase

from model_bakery import baker

from court_types.models import Court_type


class Court_typeTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.court_type_data = {"sport":"futsal", "type":"quadra"}

        cls.court_type_sample = baker.make(Court_type)
        cls.court_type_sample_specific = baker.make(Court_type, **cls.court_type_data)

    
    def test_court_type_fields(self):
        print("test court_type fields")
        
        court_type_sample_specific_object = vars(self.court_type_sample_specific)
        
        self.assertEqual(bool(self.court_type_sample_specific.id), True)
        
        for key, data in self.court_type_data.items():
            self.assertEqual(court_type_sample_specific_object[key], data)
    

    def test_court_type_parameters(self):
        print("test court_type parameters")
        sport_max_length = self.court_type_sample._meta.get_field("sport").max_length
        type_max_length = self.court_type_sample._meta.get_field("type").max_length

        self.assertEqual(sport_max_length, 60)
        self.assertEqual(type_max_length, 60)

