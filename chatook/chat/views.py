from django.views.generic.list import ListView
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

from forms import NewMessageForm
from usuarios.models import User_model
from .models import Message


def newMessageView(request, pk):
    """
    View handling new message.
    TODO: quit from receivers the user who writes. Sorry but time is up.
    """
    sender = User_model.objects.get(pk=pk)
    if request.method == 'POST':
        form = NewMessageForm(request.POST)
        if form.is_valid():
            receiver_id = request.POST['receiver']
            receiver_object = User_model.objects.get(pk=receiver_id)
            receiver_object.notified = True # Notify the user
            receiver_object.seen = False
            receiver_object.save()
            text = request.POST['text']
            message = Message(sender=sender, text=text, receiver=receiver_object)
            message.save()
            return HttpResponseRedirect(reverse('chat' , args=[pk,receiver_id]))
    else:
        form = NewMessageForm(initial={})
    return render(request, 'chat/new_message.html', {'form':form, 'sender':sender})

def chatListView(request, pk, pk2):
    """
    View for handling list of chats between two users.
    """
    sender = User_model.objects.get(pk=pk)
    receiver = User_model.objects.get(pk=pk2)
    chats = Message.objects.all().filter(sender=sender).order_by('date_sent')
    if request.method == 'POST':
        print request.POST.get('text_box')
        message = Message(sender=sender, text=request.POST.get('text_box'), receiver=receiver)
        message.save()
    return render(request, 'chat/chat.html', {'sender':sender, 'receiver':receiver, 'chats':chats})
