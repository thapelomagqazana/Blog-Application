from django.db import models
from django.utils import timezone

# Create the Post model to store blog posts in the database.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    # Added datetime fields
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    # Define a default sort order
    class Meta:
        # Blog posts are usually displayed in reverse chronological order(from newest to oldest).
        # Indicate descending order by using a hyphen before the field name, -publish.
        # Posts will be returned in reverse chronological order by default.
        ordering = ['-publish']

    def __str__(self):
        return self.title