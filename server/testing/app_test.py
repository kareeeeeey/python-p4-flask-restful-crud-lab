import json
from server.app import app
from server.models import db, Plant
import unittest

class TestPlant(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()
            plant = Plant(name="Aloe", image="https://image.com/aloe.jpg", price=15.99)
            db.session.add(plant)
            db.session.commit()

    def test_plant_by_id_get_route(self):
        '''has a resource available at "/plants/<int:id>".'''
        response = self.client.get('/plants/1')
        assert response.status_code == 200

    def test_plant_by_id_get_route_returns_one_plant(self):
        '''returns JSON representing one Plant object at "/plants/<int:id>".'''
        response = self.client.get('/plants/1')
        data = json.loads(response.data.decode())
        assert data['name'] == 'Aloe'

    def test_plant_by_id_patch_route_updates_is_in_stock(self):
        '''updates the is_in_stock field.'''
        response = self.client.patch('/plants/1', json={'is_in_stock': False})
        data = json.loads(response.data.decode())
        assert data['is_in_stock'] == False

    def test_plant_by_id_delete_route_deletes_plant(self):
        '''deletes the plant from the db'''
        response = self.client.delete('/plants/1')
        assert response.status_code == 200
        with app.app_context():
            plant = Plant.query.get(1)
            assert plant is None
