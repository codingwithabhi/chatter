from django.urls import path
from .import views

urlpatterns = [
    path('chat-board/',views.get_chatboard,name='chat-board'),
    path('chat-board/post-message/',views.post_message,name='post-message'),
    path('chat-board/delete-all-message/',views.delete_all_message,name='delete-all-message'),
    path('chat-board/delete/<int:pk>/',views.delete_message,name='delete-message'),
]