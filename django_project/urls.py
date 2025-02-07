from django.contrib import admin  # ✅ Import admin module
from django.urls import path
from django.contrib import admin
from django.urls import path
from app.views import login_view, logout_view, home_view, signup_view  # Ensure all exist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
]

