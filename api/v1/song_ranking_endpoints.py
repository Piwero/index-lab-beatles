from rest_framework import (
    serializers,
    viewsets,
)

from songs.models import Song


class NonAuthenticatedSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = (
            "name",
            "album",
            "rank",
        )

    def save(self, **kwargs):
        raise NotImplementedError("This serializer is read-only.")


class AuthenticatedSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"


class SongRankingViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return AuthenticatedSongSerializer
        else:
            return NonAuthenticatedSongSerializer
