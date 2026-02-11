from rest_framework.serializers import ModelSerializer
from .models import UserFavorite, UserCart , Post
from rest_framework.exceptions import ValidationError

class Postserializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


    def post_title(self,post_title):
        if len(post_title)<200:
            raise ValidationError("Post Title 200 ta dan kam bo'lsin (❁´◡`❁)")
        return post_title
    
    def post_desc(self,post_desc):
        if len(post_desc) <1000:
            raise ValidationError("1000dan kam so'z bo'lishi shart")
        return post_desc