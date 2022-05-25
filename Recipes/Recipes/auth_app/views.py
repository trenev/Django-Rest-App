from django.contrib.auth import get_user_model
from rest_framework import generics as api_generic_views, permissions
from rest_framework.authtoken import views as api_views


from Recipes.auth_app.serializers import CreateUserSerializer

UserModel = get_user_model()


class RegisterView(api_generic_views.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (
        permissions.AllowAny,
    )


class LoginView(api_views.ObtainAuthToken):
    permission_classes = (
        permissions.AllowAny,
    )


class LogoutView(api_views.APIView):
    permission_classes = (
        permissions.IsAuthenticated,
    )
