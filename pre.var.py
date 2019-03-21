
import goo
import digitxt
import waitInput
import tool


def handCheck():
    for l in goo.linkOrText(what="text"):
        #print("\n", type(l), "\n")
        print("\n",  "\n")

        #print(l[:500])
        tool.show2ndP(l)

        d = digitxt.digitizeText(l)
        print ("--- -- - score : ", d, d * 1000 * 10)

        i = waitInput.xMeansExit()


import txt
v = digitxt.vectorizer

if __name__ == "__main__":
    print("\n pre.var.py \n")

    handCheck()
