from django.db import models
from cloudinary.models import CloudinaryField


class DiaryIntro(models.Model):
    """Stores the opening message and the '7:22' seal settings."""
    
    title = models.CharField(max_length=100, default="7:22")
    opening_note = models.TextField(
        help_text="The very first text she sees before opening the diary."
    )
    wax_seal_color = models.CharField(
        max_length=20,
        default="#8b0000",
        help_text="HEX color for the wax seal."
    )

    def __str__(self):
        return "Diary Entry Configuration"


class DiaryPage(models.Model):
    """The actual pages of the old diary."""

    page_number = models.PositiveIntegerField(
        unique=True,
        help_text="The order of the page. 1 is the cover/first page."
    )

    chapter_title = models.CharField(
        max_length=200,
        default="A New Chapter",
        help_text="The title displayed under 'The Queen in Motion'."
    )

    # 🔥 CLOUDINARY IMAGE FIELD (THIS FIXES EVERYTHING)
    photo = CloudinaryField(
        'image',
        help_text="Upload a high-quality picture of her."
    )

    message = models.TextField(
        help_text="Write your romantic 1600s style message here."
    )

    question = models.CharField(
        max_length=255,
        default="Shall we proceed, my love?",
        help_text="The question above the 'YES' button."
    )

    is_finale = models.BooleanField(
        default=False,
        help_text="Check this ONLY for the last page (the collage page)."
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['page_number']

    def __str__(self):
        return f"Page {self.page_number} - {self.chapter_title}"
