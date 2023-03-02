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


class NonAuthenticatedSongViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Song.objects.all()
    serializer_class = NonAuthenticatedSongSerializer
