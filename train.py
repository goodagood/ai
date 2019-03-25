

from nltk.tokenize import sent_tokenize


def addup(srcList, newList):
    return srcList + newList


def readForTraining(fileName):
    txtList = []
    with open(fileName, 'r') as f:
        txt = f.read()
        sentences = sent_tokenize(txt)

        prefix = " "
        for s in sentences:
            if len(s.split()) > 100:
                txtList.append(prefix + s)
                prefix = " "
            else:
                prefix += s + " "
                pass
            pass

        return txtList

    # if return None, we can't add it up to list
    return []


if __name__ == "__main__":
    print(' train.py ')

    import os

    import config
    fpath = os.path.expanduser(config.religionTxt)
    lr = readForTraining(fpath)


    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer()
    #vectors = vectorizer.fit_transform(newsgroups_train.data)


