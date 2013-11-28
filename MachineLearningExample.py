#Determine similarity of words
combo_constant = 1.0
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6']
phonetic_letter_values = {'b':'1','c':'2','d':'3','f':'1','g':'2','j':'2','k':'2','l':'4','m':'5','n':'5','p':'1','q':'2','r':'6','s':'2','t':'3','v':'1','x':'2','z':'2'}

#open file to read/write the words from/in
my_word_file = open("Words.txt","r")
words = my_word_file.read().split(',')
my_word_file.close()
#words = ["drop", "water", "melon", "molin", "bacon", "bamboo", "mkn"]

letter_vectors = []
for word in words:
  a = []
  for i in letters:
    num_in_word = 0
    for letter in word:
      if letter == i:
        num_in_word += 1
    a.append(num_in_word)
  letter_vectors.append(a)
  
phonetic_letters = []
for word in words:
  a = word[0]
  prev_letter = word[0]
  for i in range(len(word)):
    for j in phonetic_letter_values:
      if word[i] == j and word[i] != prev_letter:
        a += phonetic_letter_values[j]
        prev_letter = word[i]
  phonetic_letters.append(a)

phonetic_letter_vectors = []
for word in words:
  a = []
  for i in letters:
    num_in_word = 0
    for letter in word:
      if letter == i:
        num_in_word += 1
    a.append(num_in_word)
  phonetic_letter_vectors.append(a)

#determines how similar two input words are
def calc_consecutive_letters(a,b):
  sim = 0.0
  for i in range(len(a)-1):
    for j in range(len(b)-1):
      if a[i] == b[j]:
        if a[i+1] == b[j+1]:
          sim += 1
  return sim

def calc_letter_distance(a,b):
  squared_distance = 0
  for i in range(len(letters)):
    squared_distance += (a[i]-b[i]) ** 2
  return squared_distance ** (0.5)

#removes any non-letter elements from a string
def remove_spaces(a):
  b = ""
  for i in a:
    isnt_letter = False
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    for j in lowercase_letters:
      if i == j:
        b += i
        break
  return b

#determine most similar words of all words in dictionary
for word in words:
  sim_array = []
  
  for i in words:
    if i != word:
      sim_array.append([calc_consecutive_letters(word, i) - calc_letter_distance(letter_vectors[words.index(word)], letter_vectors[words.index(i)]), i])

  for i in range(len(sim_array)):
    if sim_array[i] == max(sim_array):
      print list([word, sim_array[i][1]])

#asks for a word, adds it to dictionary and returns the most similar
still_going = True
while still_going:
  a = raw_input("Give me a word: ")
  if a == "-1":
    still_going = False
    break
  else:
    word = remove_spaces(a.lower())
  is_in_list = False
  for w in words:
    if word == w:
      is_in_list = True
      
  if is_in_list == False:
    words.append(word)
    a = []
    for i in letters:
      num_in_word = 0
      for letter in word:
        if letter == i:
          num_in_word += 1
      a.append(num_in_word)
    letter_vectors.append(a)
    
    a = word[0]
    prev_letter = word[0]
    for i in range(len(word)):
      for j in phonetic_letter_values:
        if word[i] == j and word[i] != prev_letter:
          a += phonetic_letter_values[j]
          prev_letter = word[i]
    phonetic_letters.append(a)
    
    a = []
    for i in letters:
      num_in_word = 0
      for letter in word:
        if letter == i:
          num_in_word += 1
      a.append(num_in_word)
    phonetic_letter_vectors.append(a)
  
  sim_array = []
  for i in words:
    if i != word:
      sim_array.append([calc_consecutive_letters(word, i) - calc_letter_distance(letter_vectors[words.index(word)], letter_vectors[words.index(i)]), i])

  for i in range(len(sim_array)):
    if sim_array[i] == max(sim_array):
      print "Most similarly spelled word is: " + sim_array[i][1]
  
  sim_array = []
  for i in words:
    if i != word:
      sim_array.append([calc_consecutive_letters(phonetic_letters[words.index(word)], phonetic_letters[words.index(i)]) - calc_letter_distance(phonetic_letter_vectors[words.index(word)], phonetic_letter_vectors[words.index(i)]), i])

  for i in range(len(sim_array)):
    if sim_array[i] == max(sim_array):
      print "Most similar sounding word is: " + sim_array[i][1]

words.sort()

#write to file
my_word_file = open("Words.txt","w")
i = 0
for w in words:
  if i==0:
    my_word_file.write(w)
    i = 1
  else:
    my_word_file.write("," + w)
my_word_file.close()

my_word_file = open("BackupWords.txt","w")
i = 0
for w in words:
  if i==0:
    my_word_file.write(w)
    i = 1
  else:
    my_word_file.write("," + w)
my_word_file.close()
