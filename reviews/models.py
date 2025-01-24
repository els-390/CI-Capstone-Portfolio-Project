from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    """
    Stores a single review entry related to :model:`auth.User`
    and :model:`projects.Project`.
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer"
        )
    reviewer_name = models.CharField(max_length=100)
    review_title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.PositiveSmallIntegerField(
        choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)],
        default=5
    )
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.review_title} - {self.author}"
