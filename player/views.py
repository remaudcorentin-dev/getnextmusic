
import ipdb

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from player.models import Music

def home(request):
    context = {}

    context['playlist'] = []
    for music in Music.objects.all():
        context['playlist'].append({'url'    : '/player/music-dl/%d'%(music.id),
                                    'name'   : music.name,
                                    'artist' : music.artist})

    return render(request, "player_index.html", context=context)

def music_dl(request, music_id):
    music = Music.objects.get(id=music_id)
    response = HttpResponse(music.music_file)
    response['content_type'] = 'audio/mpeg'
    response['Content-Disposition'] = 'attachment; filename=%s'%(music.name)
    response['X-Sendfile'] = music.music_file.name
    return response

@csrf_exempt
def music_ul(request):
    file = request.FILES['file']
    name = file.name
    new_music = Music(music_file=file, name=name)
    new_music.save()
    return HttpResponse('OK', status=200)
