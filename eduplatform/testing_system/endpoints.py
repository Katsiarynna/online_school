from itertools import chain

from django.db.models import Subquery
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, ListAPIView

from .models import \
    (Course, Topic, Article, Test,
     Question, Answer, Attempt)
from .serializers import \
    (CourseSerializer, ArticleSerializer, TestSerializer, TopicSerializer,
     QuestionSerializer, AnswerSerializer, AttemptSerializer, TopicArticleSerializer)

ALL_COURSES = Course.objects.all()
ALL_TOPICS = Topic.objects.all()
ALL_ARTICLES = Article.objects.all()
ALL_TESTS = Test.objects.all()
ALL_QUESTIONS = Question.objects.all()
ALL_ANSWERS = Answer.objects.all()
ALL_ATTEMPTS = Attempt.objects.all()


class CourseViewSet(ModelViewSet):
    queryset = ALL_COURSES
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser]


class TopicViewSet(ModelViewSet):
    queryset = ALL_TOPICS
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAdminUser]


class ArticleViewSet(ModelViewSet):
    queryset = ALL_ARTICLES
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser]


class TestViewSet(ModelViewSet):
    queryset = ALL_TESTS
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAdminUser]


class QuestionViewSet(ModelViewSet):
    queryset = ALL_QUESTIONS
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]


class AnswerViewSet(ModelViewSet):
    queryset = ALL_ANSWERS
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAdminUser]


class AttemptViewSet(ModelViewSet):
    queryset = ALL_ATTEMPTS
    serializer_class = AttemptSerializer
    permission_classes = [permissions.IsAdminUser]


class CourseTopicAPIView(ListCreateAPIView):
    queryset = ALL_TOPICS
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        course = self.kwargs["id"]
        return Topic.objects.filter(course_id=course)


class TopicArticleAPIView(ListCreateAPIView):
    queryset = ALL_TOPICS
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        course = self.kwargs["id"]
        return Article.objects.filter(topic_id=course)


class TestQuestionAPIView(ListCreateAPIView):
    queryset = ALL_TOPICS
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        test = self.kwargs["id"]
        return Question.objects.filter(test_id=test)


class QuestionAnswerAPIView(ListCreateAPIView):
    queryset = ALL_TOPICS
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        question = self.kwargs["id"]
        return Answer.objects.filter(question_id=question)


class CourseContentAPIView(ListAPIView):
    serializer_class = TopicArticleSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        course = self.kwargs["id"]
        topics = Topic.objects.filter(course=course)
        articles = Article.objects.filter(topic__in=Subquery(topics.values("pk")))
        content = list(chain(set(topics), set(articles)))
        return content


