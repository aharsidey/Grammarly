from textblob import TextBlob

txt = TextBlob("I amm a goood BBoy.")
print(txt.correct())

b = TextBlob('Hello')
print(b.translate(from_lang='en', to='zh'))
