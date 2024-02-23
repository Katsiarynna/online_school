from django.db import models
from django.contrib.auth.models import User
from mentorship.models import User
from mentorship.mixins import DateTimeMixin

class Room(models.Model, DateTimeMixin):
    name = models.CharField(max_length=100)
    online = models.ManyToManyField(to=User, blank=True)

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f'{self.name} ({self.get_online_count()})'

    class Meta:
        verbose_name = "room"
        verbose_name_plural = "rooms"


class Message(models.Model, DateTimeMixin):
    room = models.ForeignKey(to=Room, related_name='message', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.user.first_name}: {self.content}'

    class Meta:
        verbose_name = "message"
        verbose_name_plural = "messages"


class ConversationRequest(models.Model, DateTimeMixin):
    from_user = models.ForeignKey(User, related_name='requests_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='requests_received', on_delete=models.CASCADE)
    message = models.TextField()

    @property
    def __str__(self):
        return f"Request from {self.from_user} to {self.to_user}"

    class Meta:
        verbose_name = "request"
        verbose_name_plural = "requests"
