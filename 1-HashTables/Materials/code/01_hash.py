def convertToIndex(studentName):
    firstLetter = studentName[0].lower()
    index = ord(firstLetter) - 97
    return index


def insertStudent(scores, studentName, studentScore):
    index = convertToIndex(studentName)
    scores[index] = [studentName, studentScore]

def getScore(scores, studentName):
    index = convertToIndex(studentName)
    return scores[index]

scores = [None] * 26
insertStudent(scores, "Adam", 98)
insertStudent(scores, "Derek", 56)
insertStudent(scores, "Chris", 72)
insertStudent(scores, "Ethan", 79)

print(getScore(scores, "Ethan"))