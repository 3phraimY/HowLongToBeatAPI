from howlongtobeatpy  import HowLongToBeat

result = HowLongToBeat().search_from_id(7231)
print(result.json_content['game_name'])
print(result.game_name)
