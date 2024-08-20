from django.db import models


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
    created_at = models.DateTimeField(auto_now_add=True)
