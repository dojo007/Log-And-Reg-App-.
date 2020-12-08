from django.http import HttpRequest
from django.test import TestCase


# Create your tests here.
from logreg.models import User, Role, Permission
from logreg.views import delete_user


class UserTestCases(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test_user@gmail.com", first_name="f", last_name="l")
        role = Role.objects.create(name="admin")
        permission = Permission.objects.create(name="Can delete Users", codename="can_delete_users")
        role.permissions.add(permission)
        self.user.global_role = role
        self.user.save()
        self.request = HttpRequest()
        self.request.user = self.user

    def test_delete_user_with_permission(self):
        d_user = User.objects.create(email="delete_user@gmail.com", first_name="d", last_name="u")

        delete_user(request=self.request, id=d_user.id)
        self.assertFalse(User.objects.filter(email="delete_user@gmail.com").exists())

    def test_delete_user_without_permission(self):
        d_user = User.objects.create(email="delete_user@gmail.com", first_name="d", last_name="u")
        dummy_user = User.objects.create(email="dummy@gmail.com")
        dummy_user.global_role = Role.objects.create(name="sales")
        dummy_user.save()
        # set
        self.request.user = dummy_user
        delete_user(request=self.request, id=d_user.id)
        self.assertTrue(User.objects.filter(email="delete_user@gmail.com").exists())