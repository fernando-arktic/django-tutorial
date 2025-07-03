from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/votes
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('post_list/', views.post_list, name='post_list'),
    path('add_post/', views.add_post, name='add_post')
]