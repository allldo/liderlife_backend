from django.contrib import admin

from .models import *

admin.site.register(MainSoloSlider)
admin.site.register(TagsProgram)
admin.site.register(CategoryTeam)
admin.site.register(Team)
admin.site.register(Smena)
admin.site.register(Programms)
admin.site.register(TextMain)
admin.site.register(Reserve)
admin.site.register(MainGalery)

# Блоки

class BlockTimesStacked(admin.TabularInline):
    model = BlockTimes
    extra = 1

class BlockImgSmallStacked(admin.TabularInline):
    model = BlockImgSmall
    extra = 1

class BlockImgsTeamStacked(admin.TabularInline):
    model = BlockImgsTeam
    extra = 1

class BlockEventsStacked(admin.TabularInline):
    model = BlockEvents
    extra = 1

class BlockPlaceStacked(admin.TabularInline):
    model = BlockPlace
    extra = 1

class BlockQuestionsStacked(admin.TabularInline):
    model = BlockQuestions
    extra = 1

class TemplateAdmin(admin.ModelAdmin):
    inlines = [BlockImgSmallStacked, BlockTimesStacked, BlockEventsStacked, BlockImgsTeamStacked, BlockPlaceStacked, BlockQuestionsStacked]

    class Media:
        css = {
            'all': ('css/admin.css',),
        }

admin.site.register(ImagesPlace)
admin.site.register(TagsTimes)
admin.site.register(BlockTimes)
admin.site.register(BlockImgSmall)
admin.site.register(BlockImgsTeam)
admin.site.register(BlockEvents)
admin.site.register(BlockImgPlace)
admin.site.register(BlockPlace)
admin.site.register(BlockQuestions)


admin.site.register(Template, TemplateAdmin)

admin.site.site_header = 'liderlife'
admin.site.site_title = 'Страница'