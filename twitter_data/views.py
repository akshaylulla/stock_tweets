from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

import request
import os

from iexfinance.stocks import Stock
from twitter_data.forms import TickerForm
from Twitter.main_tweet import get_twitter_data

os.environ["IEX_TOKEN"] = "enter_iex_token"
# Create your views here.

class HomeView(TemplateView):
    template_name = 'twitter_data/home.html'
    
    def get(self, request):
        form = TickerForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = TickerForm(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['ticker']
            form = TickerForm()
            current_stock = Stock(ticker)
            ticker_data = current_stock.get_quote()
            ticker_price = ticker_data["iexRealtimePrice"]
            if not isinstance(ticker_price, int):
                ticker_price = ticker_data["close"]
            ticker_name = ticker_data["companyName"]
            ticker_tweets = get_twitter_data(ticker)
            if not ticker_tweets:
                args = {'form' : form}
            else:
                args = {'form': form, 'ticker_name': ticker_name, 'ticker_price':ticker_price, 'ticker_tweets': ticker_tweets}
            print(ticker)
            return render(request, self.template_name, args)
