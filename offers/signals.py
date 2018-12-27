from django.db.models.signals import post_save
from .models import Offer
from django.dispatch import receiver
import channels.layers
from asgiref.sync import async_to_sync
import json
from django.http import HttpResponse
from django.shortcuts import render, redirect
#@receiver(post_save, sender=Offer)
#def do_something_when_user_updated(sender, instance, created, **kwargs,):
#    if created:
#        x = instance.name
#        print(x)
#        print("offer is created")
#        #return render('offers/index.html', x)
#        return redirect('offers/index.html', x)


def send_message(event):
    '''
    Call back function to send message to the browser
    '''
    message = event['message']
    channel_layer = channels.layers.get_channel_layer()
    # Send message to WebSocket
    async_to_sync(channel_layer.send)(text_data=json.dumps(
        message
    ))


@receiver(post_save, sender=Offer, dispatch_uid='update_job_status_listeners')
def update_job_status_listeners(sender, instance, created, **kwargs):
    '''
    Sends job status to the browser when a Job is modified
    '''

    group_name = "chat_dhanraj"
    #message = {
    #    'message': instance.name,

    #}

    channel_layer = channels.layers.get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': 'chat_message',
            'message': instance.name
        }
    )
