# -*- coding: utf-8 -*-

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from models import User_model
from chat.models import Message


class UsersListView(ListView):
    model = User_model
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = User_model
    context_object_name = 'usuario'
    slug_field = 'nick'
    def get_context_data(self, **kwargs):
        self.user = self.get_object()
        context = super(UserDetailView, self).get_context_data(**kwargs)

        if self.user.sender.all().filter(sender=self.user.pk):
            context['sender'] = self.user.sender.all().filter(
                sender=self.user.pk)
            chated = Message.objects.values_list('receiver__id').all().filter(sender=self.user.pk)
            print chated
            context['unchated'] = User_model.objects.values_list('nick').exclude(sender__in=chated)
            #self.user.receiver.values_list('nick').all().exclude(sender=self.user.pk)
            #self.user.sender.filter(~Q(sender=self.user.pk))
            print context
        else:
            context['unchated'] = User_model.objects.values_list('nick').exclude(pk=self.user.pk)
        return context
