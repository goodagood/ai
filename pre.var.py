
import goo
import digitxt
import waitInput

def handCheck():
    for l in goo.linkOrText(what="text"):
        #print("\n", type(l), "\n")
        print("\n",  "\n")

        print(l[:500])
        d = digitxt.digitizeText(l)
        print ("--- -- - score : ", d)

        i = waitInput.xMeansExit()


if __name__ == "__main__":
    print("\n pre.var.py \n")

    handCheck()
