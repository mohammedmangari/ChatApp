from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse



def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    time = '04:27' 
    return render(request, 'room.html', {
        'username':username,
        'room':room,
        'time': time,
        'room_details': room_details
        })

def check(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


def send(request):
    message =request.POST['message']
    username= request.POST['username']
    room_id = request.POST['room_id']

    newMessage = Message.objects.create(value = message, user = username, room = room_id) 
    newMessage.save()

    return HttpResponse('Message envoi avec secce')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})





