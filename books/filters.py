import django_filters

from .models import Books, Genres, Authors


class BookFilter(django_filters.FilterSet):
    genre = django_filters.ModelChoiceFilter(
        field_name='genre',
        queryset=Genres.objects.all(),
        label='Жанр'
    )
    author = django_filters.ModelChoiceFilter(
        field_name='author',
        queryset=Authors.objects.all(),
        label='Автор'
    )

    class Meta:
        model = Books
        fields = '__all__'
