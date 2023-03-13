from django.db import models
from django.utils import timezone

# Create the Post model to store blog posts in the database.
class Post(models.Model):


    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()

    # Added datetime fields
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Added a status field that will allow us to manage the status of blog posts.
    # Will be using 'Draft' and 'Published' statuses for posts.
    # A common functionality for blogs is to save posts as a draft until ready for publication.
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )

    
    # Define a default sort order
    class Meta:
        # Blog posts are usually displayed in reverse chronological order(from newest to oldest).
        # Indicate descending order by using a hyphen before the field name, '-publish'.
        # Posts will be returned in reverse chronological order by default.
        ordering = ['-publish']
        # Define a database index for the 'publish' field.
        # To improve performance for queries filtering results by this field.
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title