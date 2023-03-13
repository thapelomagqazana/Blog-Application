from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create the Post model to store blog posts in the database.
class Post(models.Model):


    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'


    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    # Added 'author' field which defined a many-to-one relationship.
    # Meaning that each post is written by a user, and a user can write any numberof posts.
    # The 'on_delete' parameter specifies the behavior to adopt when the referenced object is deleted.
    # Using CASCADE, you specify that when the referenced user is deleted, the database will also delete all related blog posts.
    # The 'related_name' parameter to specify the name of the reverse relationship, from User to Post. 
    # This will allow us to access related objects easily from a user object by using the user.blog_posts notatation. 
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
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