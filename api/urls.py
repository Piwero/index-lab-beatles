from django.urls import (
    include,
    path,
)
from drf_spectacular.views import (
    SpectacularJSONAPIView,
    SpectacularSwaggerView,
)

app_name = "api"

urlpatterns = [
    path("v1/", include("api.v1.urls")),
    path("swagger.json", SpectacularJSONAPIView.as_view(), name="schema"),
    path(
        "swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger",
    ),
]
