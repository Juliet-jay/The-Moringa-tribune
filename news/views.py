from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
    # return HttpResponse('Welcome to the Moringa Tribune')

def news_of_day(request):
    date = dt.date.today()
    return render (request, 'all-news/today-news.html',{"date": date})
    
# view function to present news from past days
def past_days_news(request, past_date):
    
    try:
        # converts data from the string Url 
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    
    except ValueError:
        #Raise 404 error when valueError is thrown 
        raise Http404()
        assert False
        
    if date == dt.date.today():
        
        return redirect(news_of_day)
    
    return render(request, 'all-news/past-news.html', {"date", date})
         
   
    
    

    
    
