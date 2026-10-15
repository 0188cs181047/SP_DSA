def count_word_chars(text):
  return {
    char.lower():
    text.lower().count(char.lower())
    for char in text
      if char.isalpha()
  }
print(count_word_chars("Hello World! 123"))