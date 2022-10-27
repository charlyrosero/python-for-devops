import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """This is a wikipedia teacher"""

    my_wiki = wikipedia.summary(name, length)
    return str(my_wiki)


def findwiki(name="Liverpool"):
    """This is a wikipedia searcher"""

    result = wikipedia.search(name)
    return result


def phrase(name):
    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
