import sys,time
with open('wordsLibrary.txt', 'r') as file:
    words = file.read().split('\t')
k = 0
fullDiction = []
for i in words:
    if k % 2 == 1:
        fullDiction.append(words[k])
    k+=1
compDict = []
for i in fullDiction:
    if len(i) == 4:
        compDict.append(i)
# print(len(compDict))
hashDict = {}
for i in compDict:
    hashDict[i] = 0

alphabet = 'abcdefghijklmnopqrstuvwxyz'

initialWord = input("Please input the initial word:")
terminalWord = input("Please input the terminal word:")
def checkFor(word):
    if word in hashDict:
        return True
    else:
        return False
if checkFor(initialWord) and checkFor(terminalWord):
    pass
else:
    print('invalid input word')
    sys.exit()
totalWords = len(compDict)

# 每一轮都替换四个字母为二十六个
# 删除无效字母
# 对剩余的继续操作直到发现第一个目标单词
# 增加步长判断，每次操作增加一步
# 上一个单词，花费的步数
t1 = time.time()
track = {}
track[initialWord] = "INITIAL"
steps = 1

breaking = False

while True:
    tempTrack = {}
    for word, info in track.items():
        for index in range(4): #遍历原字符串每个字母
            for replace in alphabet: #替换字母
                final = word[:index] + replace + word[index+1:]
                if checkFor(final): #先检查单词是否有效
                    if final in track: #不走回头路
                        continue
                    tempTrack[final] = word
                    totalWords -= 1
                    if final == terminalWord:
                        breaking = True
                if breaking == True:
                    break
            if breaking == True:
                break
        if breaking == True:
            break
    if breaking == True:
        for word, info in tempTrack.items():
            track[word] = info
        break
    for word, info in tempTrack.items():
        track[word] = info
tracing = [terminalWord]
# print(track)
while True:
    if tracing[0] == 'INITIAL':
        break
    tracing = [track[tracing[0]]] + tracing

print(tracing[1:])
print(time.time()-t1)