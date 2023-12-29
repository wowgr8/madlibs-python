with open("story.txt", "r") as f: 
  story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

# Loop through characters in the 'story' string and enumerate provides both position (i) and character (char) in the position
for i, char in enumerate(story):
  # Check if the character is the start of the target word
  if char == target_start:
    start_of_word = i

  # Check if the character is the end of the target word and there's a valid start position
  if char == target_end and start_of_word != -1:
    # Extract the word from start position to the current position (inclusive)
    word = story[start_of_word: i + 1]
    # Append the extracted word to the 'words' list
    words.add(word)
    # Reset the start position for the next word
    start_of_word = -1

answers = {}

for word in words:
  answer = input("Enter a word for " + word + ": ")
  answers[word] = answer

print(answers)