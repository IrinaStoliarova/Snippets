from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm, UserRegistrationForm
from django.contrib import auth


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'form': form,
            'pagename': 'Добавление нового сниппета'
        }
        return render(request, 'pages/add_snippet.html', context)
    elif request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
        return redirect('snippets-list')


def snippet_delete(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    snippet.delete()
    return redirect('snippets-list')


# def snippet_update(request, snippet_id):
#     snippet = Snippet.objects.get(id=snippet_id)
#
#     return redirect('snippets-list')


def snippets_list(request):
    snippets = Snippet.objects.all()
    count_snippets = snippets.count()
    context = {
        'pagename': 'Просмотр сниппетов',
        "snippets": snippets,
        "count": count_snippets
    }
    return render(request, 'pages/view_snippets.html', context)


def snippet_detail(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    context = {
        'pagename': 'Информация о сниппете',
        "snippet": snippet
    }
    return render(request, 'pages/snippet_detail.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            # Return error message
            pass
    return redirect('home')


def logout_page(request):
    auth.logout(request)
    return redirect('home')


def registration(request):
    if request.method == "GET":
        form = UserRegistrationForm()
        context = {
            'form': form,
            'pagename': 'Регистрация нового пользователя'
        }
        return render(request, 'pages/registration.html', context)
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context = {
                'form': form,
                'pagename': 'Регистрация нового пользователя'
            }
            return render(request, 'pages/registration.html', context)
        return redirect('home')

