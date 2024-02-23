from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .endpoints import \
    (UserViewSet, TeacherViewSet, StudentViewSet, GroupViewSet, EmailViewSet,
     GroupStudentAPIView, GroupMembersAPIView, RegisterUserViewSet,
     EmailListCreateView, EmailDetailView)


router = DefaultRouter()
router.register("user", UserViewSet)
router.register("teacher", TeacherViewSet)
router.register("student", StudentViewSet)
router.register("group", GroupViewSet)
router.register("register", RegisterUserViewSet, basename="user_register")
router.register("email", EmailViewSet, basename="email")


urlpatterns = [
    path("", include(router.urls)),
    path("group/<id>/students", GroupStudentAPIView.as_view(), name="group_students"),
    path("group/<id>/members", GroupMembersAPIView.as_view(), name="group_members"),
    path('emails/', EmailListCreateView.as_view(), name='email-list'),
    path('email/<int:pk>/', EmailDetailView.as_view(), name='email-detail'),
]


