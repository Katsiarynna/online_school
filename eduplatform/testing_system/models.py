from django.db import models
from mentorship.mixins import DateTimeMixin
from mentorship.models import Teacher, Student


class Course(models.Model, DateTimeMixin):
    name = models.CharField(max_length=100, default="name")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.pk} - {self.name} - {self.price}$"

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"


class Topic(models.Model, DateTimeMixin):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.pk} - {self.name}"

    class Meta:
        verbose_name = "topic"
        verbose_name_plural = "topics"


class Article(models.Model, DateTimeMixin):
    title = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"


class Test(models.Model, DateTimeMixin):
    title = models.CharField(max_length=100)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=150)
    is_open = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} - {self.title} - {self.is_open}"

    class Meta:
        verbose_name = "test"
        verbose_name_plural = "tests"


class Question(models.Model, DateTimeMixin):
    text = models.CharField(max_length=100)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    is_important = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} - {self.text} - {self.is_important}"

    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"


class Answer(models.Model, DateTimeMixin):
    text = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk} - {self.text} - {self.is_correct}"

    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"


class Attempt(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(default=0)
    selected_answers = models.ManyToManyField(Answer, blank=True)

    def __str__(self):
        return f"{self.pk} - {self.score}"

    class Meta:
        verbose_name = "attempt"
        verbose_name_plural = "attempts"
