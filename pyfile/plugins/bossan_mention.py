from slackbot.bot import respond_to
from slackbot.bot import listen_to



@respond_to('疲れた')
@respond_to('つかれた')
def cheer(message):
    message.reply('おつかーれ！！')


@respond_to('おはよう')
@respond_to('おは')
@respond_to('oha')
def ohy(message):
    message.reply('(ｿ^▽^)ﾅ ｵﾊﾃｯｸ')
    print(message.body)


@respond_to('紗希ちゃん')
def saki(message):
    message.reply('紗希ちゃん')


@respond_to('天才')
@respond_to('最高！')
def tensai(message):
    message.reply('知ってる！')

@listen_to("何ができるの")
@listen_to("何ができる")
@listen_to("help")
@listen_to("なにができる")
def WTF(message):
    message.send('うーむ本の検索ができますよ・・・(￣Д￣)ﾉ')
    message.send('Book:（Book:の後はスペースを空けてください。）')
    message.send('例）Book: クビキリサイクル')









