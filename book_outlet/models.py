from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=6)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return '{}, {} ({})'.format(self.city, self.street, self.postal_code)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(to=Address, on_delete=models.RESTRICT, null=True)

    def full_name(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self) -> str:
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])
    author = models.ForeignKey(to=Author, on_delete=models.RESTRICT, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='', null=False,
                            blank=True,
                            # editable=False,
                            db_index=True)

    def __str__(self) -> str:
        return '{} ({})'.format(self.title, self.rating)

    def get_absolute_url(self) -> str:
        return reverse('book-detail', args=[self.slug])

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
