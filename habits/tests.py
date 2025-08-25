from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="test@test.com",
            password='123qwe')
        self.habit = Habit.objects.create(
            user=self.user,
            place="Парк",
            time="7:00:00",
            action="Прогулка",
            duration='110'
        )
        self.client.force_authenticate(user=self.user)

    def test_habits_retrieve(self):
        url = reverse("habits:habits_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.habit.place)

    def test_habits_create(self):
        url = reverse("habits:habits_create")
        data = {
            "user": self.user.pk,
            "place": "Парк",
            "time": "7:00:00",
            "action": "Прогулка",
            "duration": '110',
            "frequency": 1,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habits_update(self):
        url = reverse("habits:habits_update", args=(self.habit.pk,))
        data = {
            "place": "Магазин",
            "duration": '46',
            "frequency": 2,
        }
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.get(pk=self.habit.pk).place, "Магазин")

    def test_habits_delete(self):
        url = reverse("habits:habits_delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_create_error_duration(self):
        url = reverse("habits:habits_create")
        data = {
            "user": self.user.pk,
            "place": "Парк",
            "time": "7:00:00",
            "action": "Прогулка",
            "duration": '440',
            "frequency": 1,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_pleasant_habit_with_reward_error(self):
        url = reverse("habits:habits_create")
        data = {
            "user": self.user.pk,
            "place": "Парк",
            "time": "7:00:00",
            "action": "Прогулка",
            "duration": '100',
            "frequency": 1,
            "reward": "Печенька",
            "is_pleasant": True,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_habit_frequency_error(self):
        url = reverse("habits:habits_create")
        data = {
            "user": self.user.pk,
            "place": "Парк",
            "time": "7:00:00",
            "action": "Прогулка",
            "duration": '100',
            "frequency": 8,
            "reward": "Печенька",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
