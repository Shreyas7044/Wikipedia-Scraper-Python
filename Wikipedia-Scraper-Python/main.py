import wikipedia as wiki

# Search suggestions
print("Search Results for 'Python':")
print(wiki.search("Python"))
print("-" * 50)

# Suggest feature
print("Suggestion for 'Pyth':")
print(wiki.suggest("Pyth"))
print("-" * 50)

# Summary in English
print("English Summary:")
print(wiki.summary("Python", sentences=5))
print("-" * 50)

# Summary in French
wiki.set_lang("fr")
print("French Summary:")
print(wiki.summary("Python", sentences=5))
print("-" * 50)

# Change language back to English
wiki.set_lang("en")

# Scrape full article details
page = wiki.page("Python")

print("Title:")
print(page.title)
print("-" * 50)

print("URL:")
print(page.url)
print("-" * 50)

print("Content (first 1000 characters):")
print(page.content[:1000])
print("-" * 50)

print("Images:")
print(page.images)
print("-" * 50)

print("References / Links:")
print(page.links)