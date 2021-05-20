from django.shortcuts import render, HttpResponse, Http404, redirect
import datetime as dt
from .models import Article, Tags, Profile
from django.contrib.auth.decorators import login_required
from .forms import NewsArticleForm, UserForm, ProfileUpload
from django.contrib.auth import logout

@login_required
def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    return render(request, 'all-news/today.html',{'date': date,"news":news})


@login_required
def past_days_news(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)
    
    news = Article.days_news(date)
    return render(request, 'all-news/past.html', {"date":date,"news":news})

@login_required
def search(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})

@login_required(login_url='acounts/login/')
def article(request, article_id):
    try:
        article = Article.objects.get(id = article_id)

    except DoesnotExist:
        raise Http404()

    return render(request, 'all-news/article.html', {'article' : article})

@login_required(login_url='acounts/login/')
def new_article(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(commit=False)
            article.editor = current_user
            article.save()

        return redirect('todat_news')

    else:
        form = NewsArticleForm()

    return render(request, 'new_article.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    current_user = request.user
    profile = Profile.objects.all()

    return render(request, 'profile.html', {"current_user":current_user,"profile":profile})


@login_required
def update_profile(request):
    current_user = request.user
    title = 'Upload Profile'

    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.methos == 'POST':
            form = ProfileUpload(request.POST, request.FILES)

            if form.is_valid():
                requested_profile.profile_pic = form.cleaned_data['profile_pic']
                requested_profile.bio = form.cleaned_data['bio']
                requested_profile.username = form.cleaned_data['username']
                requested_profile.save()

                return redirect('profile')

        else:
            form = ProfileUpload()

    except:
        if request.method == 'POST':
            form = ProfileUpload(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(profile_pic = form.cleaned_data['profile_pic'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
                new_profile.save_profile()
                return redirect( 'profile' )
        else:
            form = ProfileUpload()
        
    return render(request, 'upload.html', {'current_user': current_user, "form": form, })