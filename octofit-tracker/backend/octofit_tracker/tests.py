from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test Team', description='desc')
        self.assertEqual(str(t), 'Test Team')
    def test_user_create(self):
        t = Team.objects.create(name='T', description='d')
        u = User.objects.create(name='U', email='u@test.com', team=t)
        self.assertEqual(str(u), 'U')
    def test_activity_create(self):
        t = Team.objects.create(name='T', description='d')
        u = User.objects.create(name='U', email='u@test.com', team=t)
        a = Activity.objects.create(user=u, type='Run', duration=10, date='2025-01-01')
        self.assertEqual(str(a), 'U - Run')
    def test_workout_create(self):
        w = Workout.objects.create(name='W', description='desc')
        self.assertEqual(str(w), 'W')
    def test_leaderboard_create(self):
        t = Team.objects.create(name='T', description='d')
        l = Leaderboard.objects.create(team=t, score=5)
        self.assertEqual(str(l), 'T - 5')
