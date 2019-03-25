
import os
import re


file_list = [
        '/tmp/rc.input',
        '~/tmp/rc.input',
        './rc.input'
        ]


def getInputFile(file_list):
    for fn in file_list:
        if fn:
            if os.path.exists(fn):
                return fn

    return None


def readFirstLineOfInputFile(filename):
    if not filename: return
    with open(filename) as f :
        r = f.read().strip()
        l = r.split("\n")[0]
        return l
    return None


class Monkey(object):
    def __init__(self, fileList=None):
        self._cached_stamp = 0
        self.fileName = None
        self.fileContent = None
        self.fileList = []
        self.lineList = []

        if fileList:
            self.fileList = fileList
            self.fileName = getInputFile(fileList)


    def changed(self):
        if not self.fileName:
            print('what file name you give me? mar.15 1400pm')
            print(self.fileName)
            return None

        stamp = os.stat(self.fileName).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            return True

        # File has changed, so do something...
            pass
        else:
            return False

    def readFile(self):
        if not self.fileName: return None

        with open(self.fileName, 'r') as f:
            self.fileContent = f.read()

        if self.fileContent:
            return self.fileContent
        else:
            return None


    def readLines(self):
        if self.changed: self.readFile()

        if self.fileContent:
            lines = self.fileContent.split("\n")
            self.lineList = list(
                    filter(lambda x: not re.match(r'^\s*$', x),
                    lines))
            return self.lineList
        else:
            return None


    def firstWords(self):
        """
        """
        lines = self.readLines()
        if lines and len(lines) > 0:
            return lines[0]

        return None


    def findStop(self):
        """find if there is a line with single word: stop
        """
        if self.changed: self.readLines()

        for l in self.lineList:
            if re.match(r'^\s*stop\s*$', l, re.IGNORECASE):
                return True

        return False




if __name__ == "__main__":
    monkey = Monkey(file_list)
    if monkey.changed():
        s = monkey.readFile()
        l = monkey.readLines()
        print(monkey.firstWords())
    else:
        print('monkey NOT changed')

