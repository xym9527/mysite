import  datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question
# Create your tests here.

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        :return:
        """
        time = timezone.now()+datetime.timedelta(days=2)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False,'{0} 测试用例不通过'.format(self.__class__.__name__))
