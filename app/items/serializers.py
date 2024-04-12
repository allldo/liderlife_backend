from rest_framework import serializers

from .models import *

class TextMainSerializer(serializers.ModelSerializer):

    class Meta:
        model = TextMain
        fields = '__all__'
          
class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = (
            'category',
            'name',
            'description',
            'link',
            'date_added',      
            "get_preview",     
        )    


class PgTagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TagsProgram
        fields = '__all__'

class MainSoloSliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainSoloSlider
        fields = (
            'id',
            'name',
            'get_image'
        )

class MainGalerySerializer(serializers.ModelSerializer):

    class Meta:
        model = MainGalery
        fields = (
            'id',
            'name',
            'get_image'
        )

class SmenaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Smena
        fields = (
            'id',
            'programm',
            'number',
            'price',
            'date_start',
            'date_end',
        )  

class ProgrammsSerializer(serializers.ModelSerializer):
    tags_prog = PgTagsSerializer(many=True)
    programm_smena = SmenaSerializer(many=True)

    class Meta:
        model = Programms
        fields = (
            'id',
            'slug',
            'tags_prog',
            'title',
            'get_preview',
            'small_disc',
            "price_main",
            "age_main",   
            "programm_smena",
            "date_added",     
        )         

class ProgrammsSmallInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Programms
        fields = (
            'id',
            'slug',
            'title',
        )         

class ProgrammsFormInfoSerializer(serializers.ModelSerializer):
    programm_smena = SmenaSerializer(many=True)

    class Meta:
        model = Programms
        fields = (
            'id',
            'slug',
            'title',
            'programm_smena',
        )        

class CategoryTeamSerializer(serializers.ModelSerializer):
    category_team = TeamSerializer(many=True)

    class Meta:
        model = CategoryTeam
        fields = (
            'name',
            'category_team',
        )

class ReserveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reserve
        fields = '__all__'

# Шаблоны

class TagsTimesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TagsTimes
        fields = (
            'name',
        )

class ImagesPlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImagesPlace
        fields = (
            'name',
            'get_image',
        )

class BlockImgSmallSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockImgSmall
        fields = (
            'name',
            'get_image',
        )

class BlockImgPlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockImgPlace
        fields = (
            'name',
            'get_image',
        )

class BlockImgsTeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockImgsTeam
        fields = (
            'get_image',
        )

class BlockPlaceSerializer(serializers.ModelSerializer):
    images = BlockImgPlaceSerializer(many=True)
    tags = TagsTimesSerializer(many=True)

    class Meta:
        model = BlockPlace
        fields = (
            'name',
            'description',
            'images',
            'tags'
        )

class BlockTimesSerializer(serializers.ModelSerializer):
    tags = TagsTimesSerializer(many=True)

    class Meta:
        model = BlockTimes
        fields = (
            'name',
            'description',
            'get_image',
            'tags'
        )

class BlockEventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockEvents
        fields = (
            'name',
            'description',
            'get_image',
        )

class BlockQuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockQuestions
        fields = '__all__'

class TemplateSerializer(serializers.ModelSerializer):
    imgsPlace = ImagesPlaceSerializer(many=True)
    images_disc = BlockImgSmallSerializer(many=True)
    tplace = BlockPlaceSerializer(many=True)
    bl_times = BlockTimesSerializer(many=True)
    bl_events = BlockEventsSerializer(many=True)
    images_team = BlockImgsTeamSerializer(many=True)
    bquestions = BlockQuestionsSerializer(many=True)

    class Meta:
        model = Template
        fields = (
            'programm',
            'template',

            'title',
            'title_small',
            'get_preview',

            'small_disc',
            'images_disc',

            'titleTimes',
            'bl_times',
            'bl_events',

            'titleTemplate',
            'descriptionTemplateFirst',
            'descriptionTemplateSesond',
            'images_team',

            'placeTitle',
            'placeDescription',

            'placeInfoFt',
            'placeInfoSnd',
            'placeInfoTh',

            'imgsPlace',

            'tplace',

            'bquestions',

            'date_added',
            
        )