from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from khayyam import JalaliDatetime
from .utils import gallery_path
from .choices import PanelChoices, StorageChoices, RamChoices, OSChoices


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return super(BaseModelManager, self).get_queryset().filter(deleted=False)


class BaseModel(models.Model):
    created_time = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name=_('modified time'), auto_now=True)
    deleted_time = models.DateTimeField(verbose_name=_('deleted time'), null=True, blank=True, editable=False)
    deleted = models.BooleanField(verbose_name=_('deleted'), default=False, editable=False)

    objects = BaseModelManager()
    private_manager = models.Manager()

    class Meta:
        abstract = True

    @property
    def jalali_created_time(self):
        return JalaliDatetime(timezone.localtime(self.created_time)).strftime('%H:%M %y/%m/%d')

    @property
    def jalali_modified_time(self):
        return JalaliDatetime(timezone.localtime(self.modified_time)).strftime('%H:%M %y/%m/%d')

    def set_delete(self):
        """Perform safe delete to the all models objects"""
        self.deleted = True
        self.deleted_time = timezone.now()
        self.save()


class Gallery(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=255, blank=True, null=True)
    active = models.BooleanField(verbose_name=_('active'), default=False)

    class Meta:
        verbose_name_plural = _('Galleries')


class Pictures(models.Model):
    gallery = models.ForeignKey('Gallery', verbose_name=_('gallery'), on_delete=models.CASCADE, related_name='pictures',)
    image = models.ImageField(verbose_name=_('image'), upload_to=gallery_path)


class Mobile(BaseModel):
    title = models.CharField(verbose_name=_('title'), max_length=256)
    description = models.TextField(verbose_name=_('description'))
    gallery = models.ForeignKey('gallery', verbose_name=_('gallery'), on_delete=models.CASCADE, null=True, blank=True)
    production_date = models.DateField(verbose_name=_('production_date'), )
    size = models   .FloatField(verbose_name=_('size'), )
    panel = models.PositiveSmallIntegerField(verbose_name=_('panel'), choices=PanelChoices.choices)
    storage = models.PositiveSmallIntegerField(verbose_name=_('storage'), choices=StorageChoices.choices)
    ram = models.PositiveSmallIntegerField(verbose_name=_('ram'), choices=RamChoices.choices)
    cpu = models.CharField(verbose_name=_('cpu'), max_length=128)
    camera = models.CharField(verbose_name=_('camera'), max_length=256)
    slefi_camera = models.CharField(verbose_name=_('selfi_camera'), max_length=256)
    operating_system = models.PositiveSmallIntegerField(verbose_name=_('operating_system'), choices=OSChoices.choices )
    price = models.IntegerField(verbose_name=_('price'))

    class Meta:
        verbose_name = _('mobile')
        verbose_name_plural = _('mobiles')

    def __str__(self):
        return self.title




