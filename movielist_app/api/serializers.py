from rest_framework import serializers
from movielist_app.models import Movie


#model serialisers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
    def validate(self,data):
        if data['name'] == data['description']:   #desc and title should not be same chekcing for objects based validation
            raise serializers.ValidationError("Title and Description cannot be same ")
        else:
            return data

    def validate_name(self,value):

        if len(value) <2:
            raise serializers.ValidationError("Movie Name Not Valid")
        else:
            return value




# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Movie Name Not Valid")
#
#
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     activate = serializers.BooleanField()
#
#     def create(self,validated_data):
#           return  Movie.objects.create(**validated_data)
#
#
#     def update(self,instance, validated_data):
#
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.activate = validated_data.get('activate', instance.activate)
#         instance.save()
#         return instance
#
#     def validate(self,data):
#         if data['name']==data['description']:   #desc and title should not be same chekcing for objects based validation
#             raise serializers.ValidationError("Title and Description cannot be same ")
#         else:
#             return data
#
#     # def validate_name(self,value):
#     #
#     #     if len(value) <2:
#     #         raise serializers.ValidationError("Movie Name Not Valid")
#     #     else:
#     #         return value
