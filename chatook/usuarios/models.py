# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.shortcuts import reverse


class User_model(models.Model):
    nick = models.CharField(max_length=50,
                            verbose_name="Apodo o nickname.")
    join_date = models.DateTimeField(auto_now=True,
                                     verbose_name="Fecha de ingreso.")
    mail = models.EmailField(null=True,
                             blank=True,
                             verbose_name="E-mail, no requerido.")
    notified = models.BooleanField(default=True,
                                   blank=False,
                                   verbose_name="Message nuevo.")
    seen = models.BooleanField(default=False,
                               blank=False,
                               verbose_name="Message leído.")
    picture = models.ImageField(null=True,
                                blank=True,
                                help_text='Foto del perfil.',
                                upload_to="user_photo_upload")
    birth_date = models.DateTimeField(null=True)
    
    def new_notification(self):
        """
        Setter for notified.
        """
        self.notified = False

    def message_seen(self):
        """
        Setter for seen.
        """
        self.seen = True

    def __str__(self):
        return self.nick

    def get_absolute_url(self):
        return reverse('detail', kwargs={'nick': self.nick})
