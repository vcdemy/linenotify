from settings import LINE_NOTIFY_TOKEN
from linenotify import Notify
from stock_price import get_quote

token = 'HPzTWkGnRvpcj4cClb7d5g38khy9ROH8jYtWqwRgJ7V'

stock_no = '2330'
quote = "{}目前股價為{}元！".format(stock_no, get_quote(stock_no))
print(quote)
Notify(LINE_NOTIFY_TOKEN, quote)
