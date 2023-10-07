# from django.contrib.auth.backends import ModelBackend
# from .models import User  # Substitua pelo nome do seu modelo de usuário personalizado


# class CustomModelBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             # Substitua pelo campo de identificação do usuário (por exemplo, email)
#             user = User.objects.get(name=username)
#         except User.DoesNotExist:
#             return None

#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
