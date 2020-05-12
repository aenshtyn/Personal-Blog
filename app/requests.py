import urllib.request,json
from .models import Quote

base_url = None

def configure_request(app):

    base_url = app.config["QUOTES_URL"]

def get_quotes():

    get_quotes_url = base_url.format(random)

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes.data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes_results = None

        if get_quotes_response['results']:
            quotes_results_list = get_quotes_response['results']
            quotes_results = process_results(quote_results_list)

    return quote_results

def process_results(quote_list):

    quote_results = []

    for quote_item in quote_list:
        quote = quote_item.get('quote')
        author = quote_item.get('author')

        quote_results.append(quote_object)

    return quote_results
