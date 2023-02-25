from django.db import models

class TVShow(models.Model):

    GENRE = (
        ('HORROR', 'HORROR'),
        ('COMEDY', 'COMEDY'),
        ('FANTASY', 'FANTASY'),
        ('THRILLER', 'THRILLER'),
        ('MELODRAMME', 'MELLODRAMME')
    )



    title = models.CharField('Название фильма', max_length=100)
    description = models.TextField('Описание фильма')
    image = models.ImageField(upload_to='')
    quantity = models.PositiveIntegerField('Колличество фильмов')
    genre = models.CharField(max_length=100, choices=GENRE)
    video = models.URLField()
    price = models.PositiveIntegerField('Цена билета', null=True)

    def __str__(self):
        return self.title



class RatingTv(models.Model):
    RATING = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    choise_show = models.ForeignKey(TVShow, on_delete=models.CASCADE,
                                    related_name='comment_object')
    rate = models.CharField(max_length=100, null=True, choices=RATING)
    created_date = models.DateTimeField(auto_now_add=True)