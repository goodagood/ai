
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

categories = [
        'alt.atheism', 
        'talk.religion.misc'
        #'comp.graphics', 
        #'sci.space'
        ]

cat1 = [
        'talk.religion.misc',
        'sci.space']


# do this outside the function of digitizeText
newsgroups_train = fetch_20newsgroups(
        subset='train',
        categories=cat1)

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(newsgroups_train.data)

def digitizeText(text):
    #newsgroups_train = fetch_20newsgroups(
    #        subset='train',
    #        categories=cat1)

    #vectorizer = TfidfVectorizer()
    #vectors = vectorizer.fit_transform(newsgroups_train.data)

    #gof = vectorizer.transform(['good old fasion ai not god'])
    #mean = vectorizer.transform(['calculate the mean of this'])
    #print (gof.mean(), mean.mean())

    digital = vectorizer.transform([text])
    meanValue = digital.mean()
    return meanValue


if __name__ == "__main__":
    #newsgroups_train = fetch_20newsgroups(
    #        subset='train',
    #        categories=cat1)

    #vectorizer = TfidfVectorizer()
    #vectors = vectorizer.fit_transform(newsgroups_train.data)

    #gof = vectorizer.transform(['good old fasion ai not god'])
    #mean = vectorizer.transform(['calculate the mean of this'])
    #print (gof.mean(), mean.mean())

    pass
