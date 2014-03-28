def slope_style_score(scores):
	mini = min(scores)
	maxi = max(scores)
	scores.remove(mini)
	scores.remove(maxi)
	return round(sum(scores)/3,2)