# Get-Books
# Plugin Program

from slackbot.bot import listen_to
import requests
from requests.exceptions import RequestException


@listen_to('Book:')
def search_book(message):
    print(message.body)
    search_word = message.body['text'].split()


    print(search_word[1])


    # 楽天APIを使って、本のタイトルを検索するよ
    # PayloadはAPIに投げるGetリクエストの内容を定義するよ
    # 検索のトップに出てくるものを結果として出力するよ
    # 参照：https://webservice.rakuten.co.jp/api/booksbooksearch/

    payload = {'applicationId': '1051351458834896793', 'format': 'json', 'formatVersion': '2', 'title': search_word[1],
               'hits': '1', 'page': '1'}

    req = requests.get('https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?', params=payload).json()



    result = req['Items'][0]


    resulttitle = result['title'] + " " + result['subTitle']
    resultauthor = result['author']
    resultpublisher = result['publisherName']
    resultsale = result['salesDate']
    resultprise = result['itemPrice']
    resultItemurl = result['itemUrl']
    resultImagepath = result['largeImageUrl']

    print(result)

    message.send(resulttitle)
    message.send(resultauthor)
    message.send(resultpublisher)
    message.send(resultsale)
    # message.send(resultImagepath)
    message.send("楽天で見る" + resultItemurl)
