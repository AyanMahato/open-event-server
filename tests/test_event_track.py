"""Copyright 2015 Rafal Kowalski"""
import unittest

from setup_database import Setup
from open_event import app
from open_event.helpers.data import save_to_db
from object_mother import ObjectMother


class TestEvent(unittest.TestCase):
    def setUp(self):
        self.app = Setup.create_app()

    def tearDown(self):
        Setup.drop_db()

    def test_api_tracks(self):
        event = ObjectMother.get_event()
        track = ObjectMother.get_track()
        with app.test_request_context():
            save_to_db(event,"Event saved")
            save_to_db(track, "Track saved")
        self.assertEqual(self.app.get('/get/api/v1/event/1/tracks').status_code, 200)
        self.assertEqual(self.app.get('/admin/login/').status_code, 200)

if __name__ == '__main__':
    unittest.main()