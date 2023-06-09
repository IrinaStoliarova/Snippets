from django.db import models
from django.contrib.auth.models import User

LANGS = (
    ('py', 'Python'),
    ('js', 'JavaScript'),
    ('cpp', 'C++'),
)


class Comment(models.Model):
    text = models.TextField(max_length=1000)
    creation_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    snippet = models.ForeignKey(to='Snippet', on_delete=models.CASCADE, related_name='comments')


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANGS)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="snippets",
                             blank=True, null=True)
    private = models.BooleanField(default=True)

    def __repr__(self):
        return f"Snippet: {self.name}"

    def __str__(self):
        return self.__repr__()