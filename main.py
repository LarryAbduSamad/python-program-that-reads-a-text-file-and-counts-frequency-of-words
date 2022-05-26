


def read_file_content(filename):
    with open(filename) as f:
        content = f.read()
    
    return content

print(read_file_content("story.txt"))


from collections import Counter

def count_words(filename):
        with open(filename) as f:
            text = f.read()
        
        return Counter(text.split())

print(count_words("story.txt"))
