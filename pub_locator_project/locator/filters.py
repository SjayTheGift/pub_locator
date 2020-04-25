from django_filters import FilterSet

from .models import PubInfo


class UserFilter(FilterSet):
    class Meta:
        model = PubInfo
        fields = ['name', 'city', 'suburb', 'open_time']
