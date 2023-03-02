from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from songs.models import Song


class NonAuthenticatedSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = (
            "name",
            "album",
            "rank",
            "writer",
        )

    def save(self, **kwargs):
        raise NotImplementedError("This serializer is read-only.")


class AuthenticatedSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class SongRankingViewSet(APIView):
    queryset = Song.objects.all()

    def get_queryset(self):
        return self.queryset.order_by("rank")

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return AuthenticatedSongSerializer
        else:
            return NonAuthenticatedSongSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(self.get_queryset(), many=True)
        return Response(serializer.data)
