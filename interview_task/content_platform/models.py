from django.db import models
from django.contrib.auth.models import User


class Content(models.Model):
    """A content item (game, video, artwork, music)"""

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    CATEGORY_CHOICES = (("G", "game"), ("V", "video"), ("A", "artwork"), ("M", "music"))
    category = models.CharField(
        max_length=1, choices=CATEGORY_CHOICES, null=False, blank=False
    )
    thumbnail_url = models.URLField(null=True, blank=True)
    content_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class Rating(models.Model):
    """A rating user gives to a content item"""

    content = models.ForeignKey(
        Content, on_delete=models.CASCADE, related_name="rating"
    )
    rated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rating")

    RATING_CHOICES = (
        ("N", "N/A"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    )
    rating = models.CharField(
        max_length=1, choices=RATING_CHOICES, null=True, blank=True, default="N"
    )

    def __str__(self):
        return f"{self.content} - rated '{self.rating}'"
