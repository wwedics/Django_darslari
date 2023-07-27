from django.urls import path

from .views import HomePageView,AboutPageView,PostPageView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('post/', PostPageView.as_view(), name = 'post')
]
 