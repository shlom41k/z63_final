# my_auth.urls file

from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings

from .views import SignUpView, SignInView, AddProfileView, UserProfileView, UserPostsView, UserActiveCoursesView, UserCompletedCoursesView


urlpatterns = [
    # path("", IndexView.as_view(), name="index"),

    # Registration
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signin/", SignInView.as_view(), name="signin"),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout', ),

    # Profile
    path("add_profile/", AddProfileView.as_view(), name="add_profile"),
    path("profile/", UserProfileView.as_view(), name="user_profile"),
    path("profile/posts/", UserPostsView.as_view(), name="user_posts"),
    path("profile/active_courses/", UserActiveCoursesView.as_view(), name="user_courses"),
    path("profile/completed_courses/", UserCompletedCoursesView.as_view(), name="completed_courses"),

]


