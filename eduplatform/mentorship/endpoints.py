from django.http import HttpResponse
from rest_framework import permissions, mixins, generics
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from itertools import chain
from rest_framework.routers import DefaultRouter

from .models import User, Teacher, Student, Group, Email
from .serializers import \
    (UserSerializer, TeacherSerializer, StudentSerializer,
     GroupSerializer, TeacherStudentSerializer, RegisterSerializer, EmailSerializer)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAdminUser]


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAdminUser]


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


class EmailViewSet(ModelViewSet):
    queryset = Email.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]


router = DefaultRouter()
router.register(r'emails', EmailViewSet, basename='email')


class GroupStudentAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        gruop = self.kwargs["id"]
        return Student.objects.filter(group__in=gruop)


class GroupMembersAPIView(ListAPIView):
    serializer_class = TeacherStudentSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        gruop = self.kwargs["id"]
        students = Student.objects.filter(group__in=gruop)
        teacher = Teacher.objects.filter(group=gruop)
        members = list(chain(set(students), set(teacher)))
        return members


class RegisterUserViewSet(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse(f"User {serializer.data['email']} created!", status=201)


class EmailListCreateView(ListCreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        user = self.request.user
        return Email.objects.filter(recipient=user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class EmailDetailView(generics.RetrieveAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    permission_classes = [permissions.IsAdminUser]
