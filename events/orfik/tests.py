import os


from django.test import TestCase, Client
from django.conf import settings
from django.utils import timezone
from events.orfik import models
from django.contrib.auth.models import User
from django.core.files import File


BASE_DIR = settings.BASE_DIR

class OrfikTestCase(TestCase):
    def setUp(self):
        "Setup players to test"
        user = User()
        user.username='Jon Smith'
        user.set_password('password')
        user.save()
        plr = models.Player()
        plr.nickname='Jon'
        plr.user = user
        plr.save()
        q = models.Question()
        q.number = 100
        q.text = 'Question Text'
        q.answer='answer'
        q.save()
        ans = models.Attempt()
        ans.player = plr
        ans.question = q
        ans.value = 'answer'
        ans.save()
        # Assign for testing
        self.user = user
        self.question = q
        self.ans = ans
        self.plr = plr
        self.c = Client(assert_csrf_checks=True)

    def test_player_is_accessible(self):
        player = self.plr
        self.assertEqual(player.max_level, 0)
        self.assertEqual(player.user, User.objects.get(username='Jon Smith'))

    def test_player_str_function_works(self):
        player = self.plr
        self.assertEqual(player.__str__(), 'Jon')

    def test_question_with_picture_only(self):
        q = models.Question()
        q.number = 1
        f = open(os.path.join(BASE_DIR, 'static', 'images/logo.png'), 'rb')
        q.image = File(f)
        q.answer = 'asd'
        q.save()

    def test_question_without_text_and_picture(self):
        q = models.Question()
        q.number = 2
        q.answer = 'asd'
        q.save()

    def test_aid_with_text_only(self):
        a = models.Aid()
        a.text = 'asdfasfafasf'
        a.question = self.question
        a.save()

    def test_aid_with_image_only(self):
        a = models.Aid()
        a.question = models.Question.objects.first()
        f = open(os.path.join(BASE_DIR, 'static', 'images/logo.png'), 'rb')
        a.image = File(f)
        a.save()

    def test_aid_without_text_or_image(self):
        a = models.Aid()
        a.question = models.Question.objects.last()
        a.save()

    def test_wrong_attempt_fails(self):
        ans = self.ans
        self.assertEqual(ans.is_correct(), False)

    def test_correct_attempt_passes(self):
        ans = self.ans
        ans.value = 'asd'
        ans.save()
        self.assertEqual(ans.is_correct(), True)
