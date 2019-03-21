
import requests
import bs4

from os.path import expanduser
import sys
sys.path.append(expanduser('~'))
sys.path.append('.')


# keys in home folder
import keys

import search
import soup2txt

import txt


my_api_key = keys.google_api_key
my_cse_id  = keys.google_search_engine_id

def searchGoogle(startWords="try to find God"):
    results = search.google_search(startWords, my_api_key, my_cse_id, num=10)

    for result in results['items']:
        print(result["link"])
        link = result["link"]

        #text = fetchtxt(link)
        #result['text'] = text
        #print(text[:100])

    return results


from googleapiclient.discovery import build
def makeService():
  service = build("customsearch", "v1", developerKey=my_api_key)
  return service


def makeCse():
  service = makeService()
  cse = service.cse
  return cse

def simpleSearch(search_term):
    cse = makeCse()
    res = cse().list(q=search_term, cx=my_cse_id).execute()
    return res

import random
def randomSearch(search_term):
    """give 10 random search

    num= 10 not checked
    """
    cse = makeCse()
    startNumber = random.randint(1,100)

    # check if start work?
    res = cse().list(q=search_term, cx=my_cse_id, start=startNumber, num=10).execute()
    return res


def fetchtxt(link):
    try:
        r = requests.get(link)
    except:
        return "PYTHON REQUEST EXCEPTION 2019 0321"

    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    text = soup2txt.gettext(soup)
    #print(text[:100])
    return text


def linkOrText(startWords="try to find God", what="link"):

    #results = search.google_search(startWords, my_api_key, my_cse_id, num=10)
    results = randomSearch(startWords)

    for result in results['items']:
        link = result["link"]

        if what == "link":
            yield link
        else:
            text = fetchtxt(link)
            result['text'] = text
            #print(text[:100])
            yield text

        pass


links = '''
    https://www.everystudent.com/features/know-God.html
    https://www.youtube.com/watch?v=pgmiPXAwiLg
    https://www.huffingtonpost.com/steve-mcswain/how-to-find-god-the-five-_b_4660375.html
    https://www.ted.com/talks/anjali_kumar_my_failed_mission_to_find_god_and_what_i_found_instead?language=en
    https://www.beliefnet.com/faiths/galleries/8-signs-god-is-trying-to-get-your-attention.aspx
    https://en.wikipedia.org/wiki/3_Acts_of_God
    https://www.imdb.com/title/tt3455338/
    https://thelife.com/dont-know-how
    https://www.amazon.com/Just-Do-Something-Liberating-Approach/dp/0802458386
    https://www.desiringgod.org/articles/why-are-so-many-christians-unhappy
    '''

import digitxt
import tool


def pageCheck():
    for l in linkOrText(what="text"):
        #print("\n", type(l), "\n")
        print("\n",  "\n")
        if type(l) == str:
            try:
                #print(l[:500])
                tool.show1stP(l)

                d = digitxt.digitizeText(l)
                print ("\n--- -- - score : ", d)
            except:
                print("\n ooo \n ")
        else:
            print('got no string')



if __name__ == "__main__":
    print(' __name__ == "__main__"')
    #words()

    #searchGoogle()

    #fetchtxt("https://thelife.com/dont-know-how")


    for l in linkOrText(what="text"):
        print("\n", type(l), "\n")
        if type(l) == str:
            try:
                print(l[:300])
                d = digitxt.digitizeText(l)
                print ("--- -- - score : ", d)
            except:
                print("\n ooo \n ")
        else:
            print('got no string')


