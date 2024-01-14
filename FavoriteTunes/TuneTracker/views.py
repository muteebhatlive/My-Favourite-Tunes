from django.shortcuts import render,redirect
from .models import Song, Artist
from .forms import SongForm

def song_list(request):
    songs = Song.objects.all()
    artists = Artist.objects.all()
    return render(request, 'index.html', {'songs': songs, 'artists':artists})

def song_detail(request, song_id):
    song = Song.objects.get(pk=song_id)
    return render(request, 'song_details.html', {'song': song})

def add_song(request):
    artists = Artist.objects.all() 
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            artist_id = form.cleaned_data['artist']
            artist = Artist.objects.get(pk=artist_id)

            Song.objects.create(
                title=form.cleaned_data['title'],
                artist=artist
            )

            return redirect('song_list')
    else:
        form = SongForm()

    return render(request, 'TuneTracker/song_list.html', {'form': form, 'artists': artists})

def add_artist(request):
    if request.method == 'POST':
        artist_name = request.POST.get('artistName')
        if artist_name:
            Artist.objects.create(name=artist_name)
    return redirect('song_list')
 