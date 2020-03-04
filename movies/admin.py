from django.contrib import admin
from .models import Category, Actor, Genre, Movie, MovieShots, RatingStar, Rating, Reviews
from django.utils.safestring import mark_safe

# CKUploader Widjet
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())
    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ''' Категории фильмов '''
    list_display = ("id", "name", "url",)
    list_display_links = ("name", )


class ReviewsInLine(admin.TabularInline):
    ''' Отзывы на странице фильма '''
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


class MovieShotsInLine(admin.TabularInline):
    ''' Кадры из фильма на странице фильма '''
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="110" height="100">')

    get_image.short_description = "Изображение"


class MovieAdmin(admin.ModelAdmin):
    ''' Фильмы '''
    list_display = ("id", "title", "category", "url", "draft")
    list_display_links = ("title", )
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [MovieShotsInLine, ReviewsInLine]
    save_on_top = True
    #save_as = True  // Добавляет вместо "Сохранить и добавить новый объект" ---> "Сохранить как новый объект"
    list_editable = ("draft", )
    form = MovieAdminForm
    actions = ["publish", "unpublish"]
    readonly_fields = ("get_image", )
    fieldsets = (
        (None, {
            'fields': ("title", "tagline")
        }),
        (None, {
            'fields': ("description", ("poster", "get_image"))
        }),
        (None, {
            'fields': (("year", "world_premier", "country"), )
        }),
        (None, {
            'fields': (("genres", "category"), )
        }),
        ("Режиссеры и актеры", {
            'classes': ("collapse",), # Скрытие названия группы
            'fields': (("directors", "actors"), )
        }),
        (None, {
            'fields': (("budget", "fees_in_russia", "fees_in_world"), )
        }),
        ("Опции", {
            'fields': (("url", "draft"), )
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="90" height="110">')

    def unpublish(self, request, queryset):
        ''' Снять с публикации '''
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        elif 2 <= row_update < 5:
            message_bit = f"{row_update} записи были обновлены"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        ''' Опубликовать '''
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        elif row_update == 2 or 3 or 3 or 4:
            message_bit = f"{row_update} записи были обновлены"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permission = ("change", )

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permission = ("change", )

    get_image.short_description = "Изображение постера"


class ReviewsAdmin(admin.ModelAdmin):
    ''' Отзывы '''
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")


class ActorAdmin(admin.ModelAdmin):
    ''' Режиссеры и актеры '''
    list_display = ("name", "age", "get_image", "director")
    list_display_links = ("name", )
    readonly_fields = ("get_image",)
    #list_editable = ("director", )
    list_filter = ("director", )
    search_fields = ("name", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')
        
    get_image.short_description = "Изображение"


class GenreAdmin(admin.ModelAdmin):
    ''' Жанры '''
    list_display = ("name", "url")
    list_display_links = ("name", )


class RatingAdmin(admin.ModelAdmin):
    ''' Рейтинги '''
    list_display = ("star", "movie", "ip")
    list_display_links = ("star", "movie")


class MovieShotsAdmin(admin.ModelAdmin):
    ''' Кадры из фильмов '''
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="50">')

    get_image.short_description = "Кадры из фильма"


# admin.site.register(Category, CategoryAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(MovieShots, MovieShotsAdmin)
admin.site.register(RatingStar)

# Change site title
admin.site.site_title = "Кино Маркет Django"
admin.site.site_header = "Кино Маркет Django"