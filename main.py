def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
#    print(file_contents)
#    print(word_counter(file_contents))
#    print(char_counter(file_contents))
 
    unsorted_dict = char_counter(file_contents)
    chars_list = [{'char': char, 'count': count} for char, count in unsorted_dict.items()]
    chars_list.sort(reverse=True, key=sort_by_count)
    print(chars_list)
    formating(chars_list)
   

def word_counter(input_file):
    words = input_file.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def char_counter(input_file):
    my_dict = {}
    lowered_input_file = input_file.lower()
    for character in lowered_input_file: 
        if character not in my_dict: my_dict[character] = 1
        else: my_dict[character] += 1
    return my_dict

def sort_by_count(dict_item):
    return dict_item['count']

def formating(sorted_list):
    for item in sorted_list:
        if item['char'].isalpha(): print(f"The '{item['char']}' character was found {item['count']} times")
main()