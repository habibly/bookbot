

def main():
  book_path = "books/frankenstein.txt"
  book_text = get_book_text(book_path)
  words_count = get_words_count(book_text)
  char_dict = get_chars_dict(book_text)
  print_report(book_path, words_count, char_dict)
  
def get_book_text(book_path):
  with open(book_path) as f:
    file_contents = f.read()
    return file_contents

def get_words_count(text):
  return len(text.split())

def get_chars_dict(text):
  letters = {}
  lcase_string = text.lower()
  for char in lcase_string:
    if char not in letters:
      letters[char] = 1
    else:
      letters[char] += 1
  return letters

def sort_on(dict):
  return dict["count"]

def char_dict_to_sorted_list(char_dict):
  char_dict_sorted_list = []
  
  for item in char_dict:
    item_dict = {}
    item_dict["char"] = item
    item_dict["count"] = char_dict[item]
    char_dict_sorted_list.append(item_dict)
  
  char_dict_sorted_list.sort(reverse=True, key=sort_on)
  return char_dict_sorted_list

def print_report(book_path, words_count, char_dict):
  header = f"--- Begin report of {book_path} ---"
  total_words_found = f"{words_count} words found in the document\n"
  footer = "--- End report ---"
  char_sorted_list = char_dict_to_sorted_list(char_dict)
  
  print(header)
  print(total_words_found)

  for item in char_sorted_list:
    char, count = item["char"], item["count"]
    if char.isalpha():
      print(f"The '{char}' character was found {count} times")
  print(footer)

main()