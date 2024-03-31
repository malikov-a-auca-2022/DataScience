txt = 'it takes all the running you can do to keep in the same place and if you want to get somewhere else you must run at least twice as fast as that'
words = [e for e in txt.split(sep=' ')]
dict = {}
for x in words:
    if x not in dict:
        dict[x] = 1
    else:
        dict[x] += 1

print('Sorted by frequency:')
print('[', end='')
words_sorted_by_val = sorted(dict, key=dict.get, reverse=True)
for i in range(len(words_sorted_by_val)):
    curr = words_sorted_by_val[i]
    print(f"('{curr}', {dict[curr]})", end='')
    if i != len(words_sorted_by_val)-1:
        print(', ', end='')
print(']\n')

n = int(input('Enter a positive integer (n): '))
print(f'{words_sorted_by_val[n - 1]}: {dict[words_sorted_by_val[n - 1]]}\n')

dict_sorted_by_key = sorted(dict.items())
print('Sorted alphabetically:\n', dict_sorted_by_key, '\n')

my_name = 'adilet'

print(f"Words starting with the letter '{my_name[0]}':")
starts_with_mine = [pair[0] for pair in dict_sorted_by_key if pair[0][0] == my_name[0]]
print(starts_with_mine, '\n')

print(f"Words not containing letters of the first name '{my_name}':")
not_contain_my_name = []
for word in words:
    if word in not_contain_my_name:
        continue
    contains = False
    for letter in my_name:
        if letter in word:
            contains = True
            break
    if not contains:
        not_contain_my_name.append(word)
print(not_contain_my_name, '\n')

print('Least frequent words with vowels replaced by dashes:')
min_freq = list(dict.values())[-1]
min_freq_words = []
for word in words_sorted_by_val:
    if word in min_freq_words:
        continue
    if dict[word] == min_freq:
        min_freq_words.append(word)
min_freq_words_no_vowels = []
for word in min_freq_words:
    new_word = ''
    for letter in word:
        if letter in 'aeoiu':
            new_word += '-'
        else:
            new_word += letter
    min_freq_words_no_vowels.append(new_word)
print(min_freq_words_no_vowels)