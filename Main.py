from howlongtobeatpy  import HowLongToBeat

#seach by name for HowLongToBeatEntry, combines into array of Objects
#0.2 refers to the degree to which results match query
results = HowLongToBeat(0.2).search("Portal 2")

#counter for keys
i = 0
for key in results:
    #print each game name from results array
    print(results[i].game_name)
    i+=1

#access entire json
print(results[0].json_content)


