from rest_framework import serializers
from store import models as store_model


class CategorySerializer(serializers.ModelSerializer):
    class Mete:
        model = store_model.Category
        field = ["name"]
