from django.urls import path
from .views import( PostCreateView,
                    PostDeleteView,
                    PostUpdateView,
                    MarketCreateView,
                    MarketUpdateView,
                    MarketDeleteView,
                    AgridoctorCreateView,
                    ProblemUpdateView,
                    ProblemDeleteView
                  )        #PostDetailView
from . import views

urlpatterns = [
     #home page
     path('',views.main_home_page,name="main-home-page"),
    
     #Agridoctor urls
     path('agridoctor/',views.agridoctor_home,name="agridoctor-home"),
     path('agridoctor/<int:pk>/',views.agridoctor_detail,name='agridoctor_detail'),
      path('agridoctor/post/new/',AgridoctorCreateView.as_view(), name='agridoctor-create'),#working create view
       path('agridoctor/<int:pk>/update',ProblemUpdateView.as_view(), name='agridoctor-update'),#working Update view
       path('agridoctor/post/<int:pk>/delete',ProblemDeleteView.as_view(),name="problem-delete"),
     #Blog urls
     path('blog/post/new/',PostCreateView.as_view(), name='blog-create'),#working create view
     path('blog/<int:pk>/',views.blog_detail,name='blog_detail'),#working detail view
     path('blog/post/<int:pk>/delete',PostDeleteView.as_view(),name="post-delete"),
     path('blog/',views.home,name='blog-home'),#working list view
     path('about/',views.about,name='blog-about'),
      path('blog/<int:pk>/update',PostUpdateView.as_view(), name='blog-update'),#working Update view
     
     #market urls
     path('market/',views.market_home,name='market-home'),#working list view
     path('market/<int:pk>/',views.market_detail,name='market_detail'),#working detail view
     path('market/post/new/',MarketCreateView.as_view(), name='market-create'),#working create view
     path('market/post/<int:pk>/update',MarketUpdateView.as_view(), name='market-update'),#working Update view
      path('market/post/<int:pk>/delete',MarketDeleteView.as_view(), name='market-delete'),#working delete view

]