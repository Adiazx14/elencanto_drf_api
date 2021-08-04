from django.urls import path
from store.views import user_views as views

urlpatterns = [
    path('login/',
         views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('profile/', views.UserView.as_view()),
    path('', views.UserListView.as_view()),
    path('register', views.UserRegister.as_view()),
]
