from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet, name='snippet-add'),
    path('snippets/list', views.snippets_list, name='snippets-list'),
    path('snippets/<int:snippet_id>', views.snippet_detail, name='snippet-detail'),
    path('snippets/<int:snippet_id>/delete', views.snippet_delete, name='snippet-del'),
    # path('snippets/<int:snippet_id>/update', views.snippet_update, name='snippet-update'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('snippets/my/', views.snippets_my, name="snippets-my"),
    path('comment/comment_create/', views.comment_create, name="comment-create"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
