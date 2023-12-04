from .models import User, Teacher,Student,Group

USER_DATA = {
    'password': 'qwert',
    'first_name': 'Name_test',
    'last_name': 'Surname_test',
    'email': 'test@mail.ru',
}


def create_user():
    user = User.objects.create_user(
        password='qwert',
        first_name='Name_test',
        last_name='Surname_test',
        email='test@mail.ru')
    return user
