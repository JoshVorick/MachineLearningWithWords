#Determine similarity of words
combo_constant = 1.0
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#open file to read/write the words from/in
my_word_file = open("Words.txt","r")
words = my_word_file.read().split(',')
my_word_file.close()
#words = ["drop", "water", "abcdefghijklmnopqrstuvwxyz", "qwertyuioplkjhgfdsazxcvbnm"]

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

#determines how similar two input words are
def calc_consecutive_letters(a,b):
  sim = 0.0
  for i in range(len(a)-1):
    for j in range(len(b)-1):
      if a[i] == b[j]:
        if a[i+1] == b[j+1]:
          sim += combo_constant
  return sim

def calc_letter_distance(a,b):
  return 0

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
      sim_array.append([calc_consecutive_letters(word, i)+calc_letter_distance(word, i), i])

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
  sim_array = []
  
  for i in words:
    if i != word:
      sim_array.append([calc_consecutive_letters(word, i)+calc_letter_distance(word, i), i])

  for i in range(len(sim_array)):
    if sim_array[i] == max(sim_array):
      print "Most similar word is: " + sim_array[i][1]
      print " "
      
  is_in_list = False
  for w in words:
    if word == w:
      is_in_list = True
      
  if is_in_list == False:
    words.append(word)

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

