from pytube import Search

search_query = input('Enter Search Query: ')

s = Search(search_query)


# get all search results
print(s.results)

#lenth of search results

print(len(s.results))

## completion of suggestion

print(s.completion_suggestions)
