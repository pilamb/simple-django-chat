# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import models

from usuarios.models import User_model


class Message(models.Model):
    sender = models.ForeignKey(User_model, related_name="sender")
    text = models.TextField()
    receiver = models.ForeignKey(User_model, related_name="receiver")
    date_sent = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
