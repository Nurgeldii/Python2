from site import findsite

scrapper = findsite()
list = scrapper.findArticle("bitcoin")
for i in list: print(i)
print(f"\n sites: {str(len(list))}")