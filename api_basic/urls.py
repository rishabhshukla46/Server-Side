from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView, ArticleList, ArticleDetail

urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('generic/article/', ArticleList.as_view()),
    path('generic/article/<int:pk>/', ArticleDetail.as_view()),
]