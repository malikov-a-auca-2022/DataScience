from random import randint

txt = open('movies.txt')
line = txt.readline()
txt.close()
movies = line.split(',')

rnd_ratings = int(input('Enter the number of random ratings for each movie: '))
ratings = {movie: [randint(0, 10) for _ in range(rnd_ratings)] for movie in movies}
print()

for movie in movies:
    rating = None
    while True:
        rating = int(input(f'Rate the movie "{movie}" (0 to 10): '))
        if rating >= 0 and rating <= 10:
            break
        else:
            print('Invalid rating. Please enter a number between 0 and 10.')
    ratings[movie].append(rating)
print()

print('All Ratings:')
for k, v in ratings.items():
    print(f'"{k}": {v}')
print()

print('Average Ratings:')
for k, v in ratings.items():
    print(f'"{k}": {sum(v) / len(v)}')