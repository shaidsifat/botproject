from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import psycopg2

from bot.models import Product

def search_products(request):
    search_query = 'gamingheadsets'
    url = 'https://www.amazon.com/s?k=' + search_query
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
  
    results = soup.find_all('div', {'data-component-type': 's-search-result'})
  
    conn = psycopg2.connect(host="localhost", database="bot", user="testuser", password="password")
    cursor = conn.cursor()

    for result in results:
        print(result)
        title = result.find('h2').text.strip()
        price = result.find('span', {'class': 'a-offscreen'}).text.strip()
        rating = result.find('span', {'class': 'a-icon-alt'}).text.strip()
        print(title)
        product = Product(title=title, price=price, rating=rating)
        print(product)
        product.save()

    cursor.close()
    conn.close()

    return HttpResponse('Search complete')

def update_products(request):
    products = Product.objects.all()

    for product in products:
        search_query = product.title
        url = 'https://www.amazon.com/s?k=' + search_query

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        result = soup.find('div', {'data-component-type': 's-search-result'})

        title = result.find('h2').text.strip()
        price = result.find('span', {'class': 'a-offscreen'}).text.strip()
        rating = result.find('span', {'class': 'a-icon-alt'}).text.strip()

        product.title = title
        product.price = price
        product.rating = rating
        product.save()

    return HttpResponse('Update complete')



def search1(request):
    search_query = 'gaming headsets wireless'
    url = f'https://www.amazon.com/s?k={search_query}'
    #url ='https://www.amazon.com/s?k=gaming+headsets+wireless'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get('https://www.amazon.com/', headers=headers)
    print(response)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)
    results = soup.find_all('div', {'data-component-type': 's-search-result'})
    print(results)
    conn = psycopg2.connect(host="localhost", database="bot", user="testuser", password="password")
    cursor = conn.cursor()
    for result in results:
       
        title = result.find('h2').text.strip()
        price = result.find('span', {'class': 'a-offscreen'}).text.strip()
        rating = result.find('span', {'class': 'a-icon-alt'}).text.strip()
        
        product = Product(title=title, price=price, rating=rating)
        product.save()
        print(product)
    cursor.close()
    conn.close()
    return HttpResponse('Search completed and results stored in database.')