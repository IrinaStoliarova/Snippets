from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page),
    path('snippets/add', views.add_snippet, name='snippet-add'),
    path('snippets/list', views.snippets_list, name='snippets-list'),
    path('snippets/<int:snippet_id>', views.snippet_detail, name='snippet-detail'),
    path('snippets/create', views.snippet_create, name='snippet-create'),
    path('snippets/<int:snippet_id>/delete', views.snippet_delete, name='snippet-del'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
