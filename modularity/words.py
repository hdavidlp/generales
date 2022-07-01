from asyncio.windows_events import NULL
import sys
from urllib.request import urlopen
# dunder = __name__


def fetch_words(url):
    """ Fetch a list of words from URL

        Args:
            url: The URL of a UTF-8 text Document
        
        Returns:
            A list of strings cantaining the words from
            the document.
    """
    story = urlopen(url)
    story_words =[]
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


def args():
    url = 'http://sixty-north.com/c/t.txt'
    
    if sys.argv.__len__() > 1: 
        url = sys.argv[1]

    return url

if __name__ == '__main__':
    main(args())
    

#'http://sixty-north.com/c/t.txt'