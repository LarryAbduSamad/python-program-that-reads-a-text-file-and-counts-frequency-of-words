
def read_file_content(filename):
    with open(filename) as file:
        content = file.read()
        print(content)
        return content
    

def count_words():
    text = read_file_content("story.txt")
    count = {}   
    text.split()
    return count

print(count_words())