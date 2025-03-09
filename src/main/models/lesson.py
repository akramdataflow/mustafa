import uuid
from django.utils.translation import gettext_lazy as _
from django.db import models
from core.models import TimeStampedModel, UniqueIdentifierModel

from autoslug import AutoSlugField
from django.dispatch import receiver
from django.db.models.signals import pre_save
import mimetypes
import math
import moviepy.editor


def file_upload(instance, filename):
    file_name, extension = filename.split('.')
    return f"lessons/{uuid.uuid4().hex}_{file_name}.{extension}"


class Lesson(TimeStampedModel, UniqueIdentifierModel):
    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        ordering = ('order',)

    LOCAL = 'local'
    REMOTE = 'remote'
    STORAGE_TYPES = (
        (LOCAL, 'Local'),
        (REMOTE, 'Remote'),
    )
    VIDEO = 'video'
    AUDIO = 'audio'
    IMAGE = 'image'
    DOCUMENT = 'document'
    LINK = 'link'
    OTHER = 'other'
    MEDIA_TYPES = (
        (VIDEO, 'Video'),
        (AUDIO, 'Audio'),
        (IMAGE, 'Image'),
        (DOCUMENT, 'Document'),
        (OTHER, 'Other'),
        (LINK, 'Link'),
    )

    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(_("Name"), max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)
    body = models.TextField(_("Body"), blank=True, null=True)
    file = models.FileField(_("File"), upload_to=file_upload, blank=True, null=True)
    url = models.URLField(_("URL"), blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_preview = models.BooleanField(default=False)
    size = models.PositiveIntegerField(_("File Size"), default=0)
    duration = models.PositiveIntegerField(_("Duration"), default=60)
    media_type = models.CharField(_("Media Type"), choices=MEDIA_TYPES, default=OTHER, max_length=20)

    def __str__(self):
        return self.name
    
    @property
    def storage_type(self) -> str:
        """
        Return a string indicating the type of storage used for the file.
        'local' if the file is stored locally, 'remote' if it is stored remotely.
        """
        return self.LOCAL if self.file else self.REMOTE
    
    @property
    def html_player(self) -> str:
        """
        Return a HTML tag to render the media file as a video or audio player,
        or a link if the file is remote.
        """
        if self.file:
            return f'<video src="{self.file.url}" controls></video>'
        return f'<a href="{self.url}">Link</a>'
    
    @property
    def size_format(self) -> str:
        sizes = ['B', 'KB', 'MB', 'GB', 'TB',]
        idx = int(math.log(self.size, 1024))
        return f'{round(self.size / 1024 ** idx, 2)} {sizes[idx]}'
    
    @property
    def duration_format(self) -> str:
        minutes = math.floor(self.duration / 60)
        seconds = self.duration % 60
        hours = math.floor(minutes / 60)
        return f'{hours}:{minutes:02d}:{seconds:02d}' if hours > 0 else f'{minutes}:{seconds:02d}'


@receiver(pre_save, sender=Lesson)
def set_media_type(sender, instance, **kwargs):
    """
    Signal to set media_type from mimetypes.

    If the instance has a file, it sets the media_type from the
    mimetypes.guess_type() function. If the guessed type is not
    one of the types in the lesson's media_type choices, it sets
    the media_type to the 'OTHER' choice.

    If the file is a video, it also sets the duration from the
    moviepy VideoFileClip object.

    The instance is then saved.
    """
    if instance.file:
        mime_type = mimetypes.guess_type(instance.file.name)[0]
        mime_type_source = mime_type.split('/')[0]
        instance.media_type = mime_type_source if mime_type_source in [instance.VIDEO, instance.AUDIO, instance.IMAGE, instance.DOCUMENT] else instance.OTHER
        instance.size = instance.file.size
        if instance.media_type == instance.VIDEO:
            instance.duration = moviepy.editor.VideoFileClip(instance.file.path).duration
        instance.save()
        

    
