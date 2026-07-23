from django.db import models
from django.utils.text import slugify


class ResearchArea(models.Model):

    title = models.CharField(
        max_length=150,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    short_description = models.CharField(
        max_length=250,
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="research/",
        blank=True,
        null=True,
    )

    icon = models.CharField(
        max_length=50,
    )

    featured = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):

        return self.title

    class Meta:

        ordering = ["title"]

        verbose_name = "Research Area"

        verbose_name_plural = "Research Areas"


class Project(models.Model):

    title = models.CharField(
        max_length=200,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    category = models.ForeignKey(
        ResearchArea,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    short_description = models.CharField(
        max_length=300,
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True,
    )

    github_link = models.URLField(
        blank=True,
    )

    paper_link = models.URLField(
        blank=True,
    )

    featured = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):

        return self.title

    class Meta:

        ordering = ["-created_at"]

        verbose_name = "Project"

        verbose_name_plural = "Projects"


class Publication(models.Model):

    title = models.CharField(
        max_length=300,
    )

    authors = models.CharField(
        max_length=300,
    )

    journal = models.CharField(
        max_length=200,
    )

    year = models.PositiveIntegerField()

    link = models.URLField(
        blank=True,
    )

    featured = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):

        return self.title

    class Meta:

        ordering = ["-year"]

        verbose_name = "Publication"

        verbose_name_plural = "Publications"


class TeamMember(models.Model):

    name = models.CharField(
        max_length=150,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    designation = models.CharField(
        max_length=150,
    )

    # Controls the display order on the website
    display_order = models.PositiveIntegerField(
        default=0,
    )

    photo = models.ImageField(
        upload_to="team/",
        blank=True,
        null=True,
    )

    email = models.EmailField(
        blank=True,
    )

    bio = models.TextField()

    research_interest = models.TextField(
        blank=True,
    )

    linkedin = models.URLField(
        blank=True,
    )

    google_scholar = models.URLField(
        blank=True,
    )

    researchgate = models.URLField(
        blank=True,
    )

    personal_website = models.URLField(
        blank=True,
    )

    featured = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):

        return self.name

    class Meta:

        ordering = ["display_order"]

        verbose_name = "Team Member"

        verbose_name_plural = "Team Members"

class News(models.Model):

    title = models.CharField(
        max_length=200,
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
    )

    short_description = models.CharField(
        max_length=250,
    )

    content = models.TextField()

    image = models.ImageField(
        upload_to="news/",
        blank=True,
        null=True,
    )

    featured = models.BooleanField(
        default=False,
    )

    published_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):

        return self.title

    class Meta:

        ordering = ["-published_date"]

        verbose_name = "News"

        verbose_name_plural = "News"


class ContactMessage(models.Model):

    name = models.CharField(
        max_length=100,
    )

    email = models.EmailField()

    subject = models.CharField(
        max_length=200,
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):

        return self.name

    class Meta:

        ordering = ["-created_at"]

        verbose_name = "Contact Message"

        verbose_name_plural = "Contact Messages"


class Gallery(models.Model):

    CATEGORY_CHOICES = [

        ("Research", "Research"),
        ("Laboratory", "Laboratory"),
        ("Conference", "Conference"),
        ("Workshop", "Workshop"),
        ("Event", "Event"),
        ("Achievement", "Achievement"),

    ]

    title = models.CharField(
        max_length=200,
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Research",
    )

    image = models.ImageField(
        upload_to="gallery/",
    )

    description = models.TextField(
        blank=True,
    )

    featured = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):

        return self.title

    class Meta:

        ordering = ["-created_at"]

        verbose_name = "Gallery Image"

        verbose_name_plural = "Gallery Images"


class Partner(models.Model):

    name = models.CharField(
        max_length=150,
    )

    logo = models.ImageField(
        upload_to="partners/",
    )

    website = models.URLField(
        blank=True,
    )

    featured = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):

        return self.name

    class Meta:

        ordering = ["name"]

        verbose_name = "Partner"

        verbose_name_plural = "Partners"


class Achievement(models.Model):

    CATEGORY_CHOICES = [

        ("Award", "Award"),
        ("Grant", "Grant"),
        ("Patent", "Patent"),
        ("Recognition", "Recognition"),
        ("Competition", "Competition"),
        ("Publication", "Publication"),

    ]

    title = models.CharField(
        max_length=250,
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="achievements/",
        blank=True,
        null=True,
    )

    year = models.PositiveIntegerField()

    featured = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:

        ordering = ["-year"]

        verbose_name = "Achievement"

        verbose_name_plural = "Achievements"

    def __str__(self):

        return self.title



class SiteSettings(models.Model):

    site_name = models.CharField(
        max_length=200,
        default="Viksit Bharat Research Lab",
    )

    tagline = models.TextField(
        blank=True,
    )

    address = models.TextField(
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    phone = models.CharField(
        max_length=50,
        blank=True,
    )

    linkedin = models.URLField(
        blank=True,
    )

    twitter = models.URLField(
        blank=True,
    )

    github = models.URLField(
        blank=True,
    )

    youtube = models.URLField(
        blank=True,
    )

    footer_text = models.CharField(
        max_length=300,
        default="All Rights Reserved.",
    )

    class Meta:

        verbose_name = "Website Settings"

        verbose_name_plural = "Website Settings"

    def __str__(self):

        return self.site_name
