from api_call import GetColors

loved_colors = GetColors.loved_colors()
assert loved_colors is not None, 'Bad response from API'
print(loved_colors.keys())