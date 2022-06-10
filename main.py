
def read_file_content(filename):
    with open(filename) as file:
        content = file.read()
        print(content)
        return content
    
def count_words():
    text = read_file_content("story.txt")
    count = {}   
    text = text.split()
    for word in text:
        count[word] = text.count(word)
    return count

print(count_words())