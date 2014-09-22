famous_quote = input("Enter a famous quote: ")
formatted = """Upper case: {0}
Lower case: {1}
Capitalized: {2}
Title: {3}""".format(famous_quote.upper(), famous_quote.lower(), famous_quote.capitalize(), famous_quote.title())
print(formatted)
