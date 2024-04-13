from io import BytesIO
from PIL import Image
import os
from django.contrib.auth.models import User

from django.core.files import File
from django.utils import timezone
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from datetime import datetime
import json
from rest_framework.response import Response

from tinymce import models as tinymce_models

base_url = os.environ.get('BASE_URL', '')
print("Working witn base_url: ", base_url)

class TextMain(models.Model):    
    name = models.CharField("Текст на главной", max_length=255, blank=True)
    name_disc = models.CharField("Подзаголовок на главной", max_length=255, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Заголовок (на главной)"
        verbose_name_plural = "Заголовок (на главной)"

    def __str__(self):
        return self.name

class CategoryTeam(models.Model):    
    name = models.CharField("Роль участника команды", max_length=255, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_preview(self):
        if self.preview:
            return base_url + self.preview.url
        return ''

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Роль участника"
        verbose_name_plural = "Роли участника команды"

    def __str__(self):
        return self.name

class MainSoloSlider(models.Model):    
    name = models.CharField("Название", max_length=255, blank=True)
    img = models.ImageField("Фотография", upload_to='image/')
    date_added = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        if self.img:
            return base_url + self.img.url
        return ''

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Карусель на главной"
        verbose_name_plural = "Карусель на главной"

    def __str__(self):
        return self.name

class MainGalery(models.Model):    
    name = models.CharField("Название", max_length=255, blank=True)
    img = models.ImageField("Фотография", upload_to='image/')
    date_added = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        if self.img:
            return base_url + self.img.url
        return ''

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Галерея на главной"
        verbose_name_plural = "Галерея на главной"

    def __str__(self):
        return self.name

class TagsProgram(models.Model):    
    name = models.CharField("Тэг", max_length=255, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Тэг программ"
        verbose_name_plural = "Тэг програмы"

    def __str__(self):
        return self.name

class Team(models.Model):
    category = models.ForeignKey(CategoryTeam, related_name='category_team', verbose_name="Роль участника", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField("Имя фамилия участника", max_length=255)
    description = models.TextField("Краткое описание", blank=True)
    preview = models.ImageField("Фотография участника", upload_to='image/team/')
    link = models.CharField("Ссылка на hh", max_length=255, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_preview(self):
        if self.preview:
            return base_url + self.preview.url
        return ''

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Участника"
        verbose_name_plural = "Команда"

    def __str__(self):
        return self.name

class Programms(models.Model):
    tags_prog = models.ManyToManyField(TagsProgram, related_name='tags_prog_rel', verbose_name="Тэги", blank=True, null=True)
    slug = models.SlugField("Ссылка на страницу", max_length=200)
    title = models.CharField("Название программы", max_length=255)
    main_photo = models.ImageField("Основная фотография", upload_to='image/programm/')
    small_disc = models.TextField("Коротко о программе")
    price_main = models.CharField("Цена на главной", max_length=255)
    age_main = models.CharField("Возраст на главной", max_length=255)
    draft = models.BooleanField("Черновик, если (окно заполнено, то не отображается)", default=False)
    date_added = models.DateTimeField(blank=True)

    def get_preview(self):
        if self.main_photo:
            return base_url + self.main_photo.url
        return ''

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Программа"
        verbose_name_plural = "Программы"

    def __str__(self):
        return self.title

class Smena(models.Model):
    programm = models.ForeignKey(Programms, related_name='programm_smena', verbose_name="Программа", on_delete=models.CASCADE, blank=True, null=True)
    number = models.IntegerField("Номер смены")
    price = models.IntegerField("Стоимость за смену")
    date_start = models.DateField(verbose_name='Дата старта мероприятия')
    date_end = models.DateField(verbose_name='Дата конца мероприятия')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Смена"
        verbose_name_plural = "Смены"

    def __str__(self):
        return self.programm.title

class Reserve(models.Model):
    fio = models.CharField("ФИО участника", max_length=255, blank=True)
    data_uchast = models.DateField("Дата рождения участника", blank=True, null=True)
    data_parent = models.CharField("ФИО представителя участника", max_length=255)
    primechanie = models.CharField("Примечание", max_length=255, blank=True)
    phone = models.CharField("Телефон", max_length=255)
    email = models.CharField("Email", max_length=255)
    dop_phone = models.CharField("Доп телефон", max_length=255, blank=True)
    info_title = models.CharField("Откуда узнали о нас", max_length=255, blank=True)
    programm_info = models.CharField("Программа", max_length=255)
    data_smeni = models.CharField("Дата заезда", max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Бронь"
        verbose_name_plural = "Брони"

    def __str__(self):
        return self.fio

# Шаблоны

class ImagesPlace(models.Model):
    name = models.CharField("Название", max_length=255)
    img = models.ImageField("Фотография", upload_to='image/')
    date_added = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        if self.img:
            return base_url + self.img.url
        return ''

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Место проведения программы (фото)"
        verbose_name_plural = "Место проведения программы (фото)"

    def __str__(self):
        return self.name

class Template(models.Model):
    class TemplateList(models.IntegerChoices):
        LSLETO = 0, _('Лидер - успешный старт. Лето')
        LSHAG = 1, _('Лидер - шаг вперед')
        GKIDS = 2, _('Галилео кидс')
        LKADRE = 3, _('Лидер в кадре')
        SPB = 4, _('Выпускной')
        KLAGER = 5, _('Конный лагерь. Horse paradise')

    programm = models.ForeignKey(Programms, related_name='programm_template', verbose_name="Программа", on_delete=models.CASCADE, blank=True, null=True)
    template = models.IntegerField("Шаблон", default=0, choices=TemplateList.choices)     
    title = models.CharField("Название программы", max_length=255, blank=True)
    title_small = models.CharField("Название программы (Мал. часть)", max_length=255, blank=True)

    main_photo = models.ImageField("Основная фотография", upload_to='image/programm/')
    small_disc = models.TextField("Коротко о программе (Описание)", blank=True)
    titleTimes = models.CharField("Что ждет подростка в лагере? (Название)", max_length=255, blank=True)

    titleTemplate = models.CharField("Команда лагеря (Название)", max_length=255, blank=True)
    descriptionTemplateFirst = models.TextField("Команда (Описание 1)", max_length=1200, blank=True)
    descriptionTemplateSesond = models.CharField("Команда (Описание 2)", max_length=255, blank=True)

    placeTitle = models.CharField("Место проведения программы", max_length=255, blank=True)
    placeDescription = models.TextField("Коротко о программе (Описание)", blank=True)

    placeInfoFt = models.CharField("Где находится?", max_length=255, blank=True)
    placeInfoSnd = models.CharField("Проживание", max_length=255, blank=True)
    placeInfoTh = models.CharField("В номере", max_length=255, blank=True)

    imgsPlace = models.ManyToManyField(ImagesPlace, related_name='imgs_place', verbose_name="Фото (Место проведения)", blank=True)

    date_added = models.DateTimeField(auto_now_add=True)

    def get_preview(self):
        if self.main_photo:
            return base_url + self.main_photo.url
        return ''

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Шаблоны"
        verbose_name_plural = "Шаблоны"

    def __str__(self):
        return self.title

class BlockImgSmall(models.Model):
    template = models.ForeignKey(Template, related_name='images_disc', verbose_name="Шаблон", on_delete=models.CASCADE, blank=True, null=True)  
    name = models.CharField("Название", max_length=255)
    img = models.ImageField("Фотография", upload_to='image/')
    date_added = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        if self.img:
            return base_url + self.img.url
        return ''

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Коротко о программе (фото)"
        verbose_name_plural = "Коротко о программе (фото)"

    def __str__(self):
        return self.name

class BlockImgsTeam(models.Model):
    template = models.ForeignKey(Template, related_name='images_team', verbose_name="Шаблон", on_delete=models.CASCADE, blank=True, null=True)  
    img = models.ImageField("Фотография", upload_to='image/')
    date_added = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        if self.img:
            return base_url + self.img.url
        return ''

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Команда лагеря (фото)"
        verbose_name_plural = "Команда лагеря (фото)"

    def __str__(self):
        return str(self.id)

class BlockImgPlace(models.Model):
    name = models.CharField("Название", max_length=255, blank=True)
    img = models.ImageField("Фотография", upload_to='image/', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        if self.img:
            return base_url + self.img.url
        return ''

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Место лагеря (фото)"
        verbose_name_plural = "Место лагеря (фото)"

    def __str__(self):
        return self.name

class TagsTimes(models.Model):    
    name = models.CharField("Тэг", max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Тэги (Шаблон)"
        verbose_name_plural = "Тэги (Шаблоны)"

    def __str__(self):
        return self.name

class BlockTimes(models.Model):
    template = models.ForeignKey(Template, related_name='bl_times', verbose_name="Шаблон", on_delete=models.CASCADE, blank=True, null=True)    
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание", blank=True)
    img = models.ImageField("Фотография", upload_to='image/', blank=True)
    tags = models.ManyToManyField(TagsTimes, related_name='tagsTimes', verbose_name="Тэги", blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        if self.img:
            return base_url + self.img.url
        return ''

    class Meta:
        ordering = ('-date_added',)
        verbose_name = "Что ждет ребенка (блоки)"
        verbose_name_plural = "Что ждет ребенка (блоки)"

    def __str__(self):
        return str(self.id)

class BlockEvents(models.Model):
    template = models.ForeignKey(Template, related_name='bl_events', verbose_name="Шаблон", on_delete=models.CASCADE, blank=True, null=True)    
    name = models.CharField("Название", max_length=255, blank=True)
    description = models.TextField("Описание", blank=True)
    img = models.ImageField("Фотография", upload_to='image/', blank=True)

    def get_image(self):
        if self.img:
            return base_url + self.img.url
        return ''

    class Meta:
        verbose_name = "Эвенты блоки (Шаблон)"
        verbose_name_plural = "Эвенты блоки (Шаблон)"

    def __str__(self):
        return self.name

class BlockPlace(models.Model):
    template = models.ForeignKey(Template, related_name='tplace', verbose_name="Шаблон", on_delete=models.CASCADE, blank=True, null=True)    
    name = models.CharField("Название", max_length=255, blank=True)
    description = models.TextField("Описание", blank=True)
    images = models.ManyToManyField(BlockImgPlace, related_name='imsPlace', verbose_name="Фотографии", blank=True)
    tags = models.ManyToManyField(TagsTimes, related_name='tagsPlace', verbose_name="Тэги", blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        if self.img:
            return base_url + self.img.url
        return ''

    class Meta:
        verbose_name = "Место проведения блоки (Шаблон)"
        verbose_name_plural = "Место проведения блоки (Шаблон)"

    def __str__(self):
        return self.name

class BlockQuestions(models.Model):
    template = models.ForeignKey(Template, related_name='bquestions', verbose_name="Шаблон", on_delete=models.CASCADE, blank=True, null=True)    
    name = models.CharField("Название", max_length=255, blank=True)
    description = tinymce_models.HTMLField("Описание")
    date_added = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        if self.img:
            return base_url + self.img.url
        return ''

    class Meta:
        verbose_name = "Вопрос ответ"
        verbose_name_plural = "Вопрос ответ"

    def __str__(self):
        return self.name