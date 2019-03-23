
import requests


def fetchtxt(link):
    r = requests.get(result["link"])
    soup = bs4.BeautifulSoup(r.text)
    text = soup2txt.gettext(soup)
    result['text'] = text
    t.append(text)
    print(text[:100])


from nltk.tokenize import sent_tokenize

def show1stP(text):
    sent_list = sent_tokenize(text)
    print(sent_list[0])
    print("\n...\n")

def show2ndP(text):
    sent_list = sent_tokenize(text)
    if len(sent_list) > 1:
        print("\n...\n")
        print(sent_list[1])
        print("\n...\n")
    else:
        print(sent_list[0])


# c
def readFirstLineOfInputFile(filename):
    if not filename: return
    with open(filename) as f :
        r = f.read().strip()
        l = r.split("\n")[0]
        return l
    return None

import pydoc
import sh
def showLine(link):
    if not link: return
    dump = sh.w3m("-dump", link)
    dump = str(dump)

    pydoc.pager(dump)
    pass
