price_of_whiskey = float(input())
beer = float(input())
wine = float(input())
rakija = float(input())
whiskey = float(input())

price_of_rakija = price_of_whiskey / 2
price_of_wine = wine * (price_of_rakija - (price_of_rakija * 0.4))
price_of_beer = beer * (price_of_rakija - (price_of_rakija * 0.8))
total_whiskey_price = whiskey * price_of_whiskey
total_rakija_price = rakija * price_of_rakija
total_price = price_of_beer + total_rakija_price + total_whiskey_price + price_of_wine

print(f'{total_price:.2f}')
