from drf_spectacular.utils import extend_schema
from rest_framework import (
    exceptions,
    serializers,
    status,
)
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

    @extend_schema(
        responses={
            200: (
                AuthenticatedSongSerializer(many=True),
                "List of songs data for auth users.",
            ),
            200: (
                NonAuthenticatedSongSerializer(many=True),
                "List of songs data for non auth users",
            ),
        }
    )
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(self.get_queryset(), many=True)
        return Response(serializer.data)

    @extend_schema(
        request=AuthenticatedSongSerializer,
        responses={
            201: AuthenticatedSongSerializer,
            400: "Non authenticated users cannot create songs.",
        },
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()

        except NotImplementedError:
            raise exceptions.ValidationError(
                "Non authenticated users cannot create songs."
            )

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
