from howlongtobeatpy  import HowLongToBeat

#seach from ID for HowLongToBeatEntry
result = HowLongToBeat().search_from_id(7231)

#access attribute from json dictionary
print(result.json_content['game_name'])

#access attribute directly
print(result.game_name)

