from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def films(request):
    movies = [
        {'name': 'The Dark Knight', 'imdb': 9.0},
        {'name': 'Inception', 'imdb': 8.8},
        {'name': 'Interstellar', 'imdb': 8.7},
        {'name': 'Joker', 'imdb': 7.5},
        {'name': 'Avatar', 'imdb': 7.9},
        {'name': 'Iron Man', 'imdb': 9.3},
    ]

    return render(request, 'films.html', {'movies': movies})
