from urllib import response
import urllib.request,json
from .models import Quote

def get_quotes():
    random_quote_url= 'http://quotes.stormconsultancy.co.uk/random.json'
    
    with urllib.request.urlopen(random_quote_url) as url:
        get_quotes_data= url.read()
        response = json.loads(get_quotes_data)
        if response:
            quote_response= process_response(response)
    return quote_response
            
def process_response(response):
    id = response.get('id')
    author = response.get('author')
    random_quote= response.get('quote')
    permalink = response.get('permalink')
    quote_object= Quote(id,author,random_quote,permalink)
    return quote_object
    

