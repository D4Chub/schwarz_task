import django_filters

from .models import Books, Genres, Authors


class BookFilter(django_filters.FilterSet):

    class Meta:
        model = Books
        fields = '__all__'

    genre = django_filters.TypedChoiceFilter(
        field_name='genre__name',
        choices=[(genre.name, genre.id) for genre in Genres.objects.all()],
        label='Жанр'
    )
    author = django_filters.TypedChoiceFilter(
        field_name='author__name',
        choices=[(author.name, author.id) for author in Authors.objects.all()],
        label='Автор'
    )
