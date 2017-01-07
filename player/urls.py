
from django.conf.urls import url

from player.views import home
from player.views import music_dl
from player.views import music_ul

urlpatterns = [
    url(r'^$', home, name="Player Home Page"),
    url(r'^music-dl/([0-9]+)$', music_dl, name="Player - Download Function"),
    url(r'^music-ul$', music_ul, name="Player - Upload Function")
]
