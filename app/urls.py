from django.contrib.auth.decorators import login_required
from django.urls import path, include

from .views import SignUpView, IndexView, ProfileView, UserDetailView, EditView, MatchesView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile', login_required(ProfileView.as_view()), name='profile'),
    path('matches', login_required(MatchesView.as_view()), name='matches'),
    path('profile/edit', login_required(EditView.as_view()), name='edit'),
    path('<str:username>/', login_required(UserDetailView.as_view()), name='detail'),
    path('accounts/', include('django.contrib.auth.urls')),
]
