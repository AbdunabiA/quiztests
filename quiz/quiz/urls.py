from django.contrib import admin
from django.urls import path

from quizapp.views import IndexView, QuizView, QuizDataView, QuizSaveView
from natijaapp.views import ResultView, SignupView, LoginView, logoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', IndexView.as_view(), name='index'),
    path('index/<int:pk>', QuizView.as_view(), name='quiz'),
    path('result/', ResultView.as_view(), name='result'),
    path('', SignupView.as_view(), name='signup'),
    path('logout/', logoutView, name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('<int:pk>/data/', QuizDataView.as_view(), name='quiz-data'),
    path('<int:pk>/save/', QuizSaveView.as_view(), name='quiz-save'),
]
