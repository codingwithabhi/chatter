from django.conf import settings
from django.shortcuts import redirect, render,get_object_or_404
from .models import Message
from .utils import get_client_ip,is_token_valid
import json
# Create your views here.


def get_chatboard(request):
    message_list = Message.objects.all()
    ctx = {"message_list":message_list}
    return render(request, "message_list.html",ctx)

def post_message(request):
    source = get_client_ip(request)
    text = request.POST.get("message")
    Message.objects.create(source=source,text=text)
    return redirect("chat-board")

def delete_all_message(request):
    token = request.POST.get("token")
    if is_token_valid(token):
        Message.objects.all().delete()
    return redirect("chat-board")
 
def delete_message(request,pk):
    token = request.GET.get("token")
    print(request.GET)
    print(token,settings.MESSAGE_TOKEN)
    if is_token_valid(token):
        message = get_object_or_404(Message,pk=pk)
        message.delete()
    return redirect('chat-board')