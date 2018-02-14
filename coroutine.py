def tally():
	score =2
	increment = 0
	while True:
		increment = yield score
        
		if increment:
			score += increment
		else:
			increment = 0

white_fox = tally()
print(__name__)
print(next(white_fox))
print(next(white_fox))
print(white_fox.send(1))

print(next(white_fox))

