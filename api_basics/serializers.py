from rest_framework import serializers
from .models import Articles


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = ['ID','ph','temp','BOD','COD','TSS','DO','watercons','Alkalinity','EBOD','ETSS','ENH','ANO','Eph','FMLSS','ADO','ANH']