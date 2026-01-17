from django.db import models


from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.PositiveIntegerField(null=True, blank=True)
    photo = models.ImageField(
        upload_to='authors/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Book(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('archived', 'Archived'),
    )

    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    description = models.TextField(blank=True)
    published_year = models.PositiveIntegerField()
    pages = models.PositiveIntegerField()
    cover = models.ImageField(
        upload_to='books/',
        blank=True,
        null=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


