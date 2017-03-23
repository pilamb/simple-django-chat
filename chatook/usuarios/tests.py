# -*- coding: utf-8 -*-

from django.test import TestCase
from django.shortcuts import reverse
from django.http import HttpResponseNotFound

from .models import User_model


def create_user(nick):
    return User_model.objects.create(nick=nick)


class User_modelTests(TestCase):
    def test_new_notification(self):
        user = create_user('User1')
        self.assertTrue(user.notified)
        user.new_notification()
        self.assertFalse(user.notified)

    def test_message_seen(self):
        user = create_user('User1')
        self.assertFalse(user.seen)
        user.message_seen()
        self.assertTrue(user.seen)

    def test_str(self):
        nick = 'User1'
        user = create_user(nick)
        self.assertEquals(nick, str(user))

    def test_get_absolute_url(self):
        user = create_user('User1')
        self.assertEquals(user.get_absolute_url(), u'/usuario/User1/')


class UsersListViewTest(TestCase):
    def test_with_no_users(self):
        url = reverse('home')
        response = self.client.get(url)

        self.assertContains(response, "No users available.")

    def test_with_users(self):
        user = create_user('Nick1')
        url = reverse('home')
        response = self.client.get(url)

        self.assertContains(response, user.nick)
        self.assertContains(response, user.get_absolute_url())


class UsersDetailViewTest(TestCase):
    def test_with_unknown_user(self):
        url = reverse('user_detail', kwargs={'pk': 6})
        response = self.client.get(url)

        self.assertTrue(isinstance(response, HttpResponseNotFound))

    def test_with_known_user(self):
        user = create_user('User1')
        url = user.get_absolute_url()

        response = self.client.get(url)

        self.assertContains(response, 'Detalle de usuario: {}'.format(user.nick))
