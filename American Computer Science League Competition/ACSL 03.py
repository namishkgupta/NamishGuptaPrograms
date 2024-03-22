def splitParagraph(paragraph):
   sentences = paragraph.split('.')
   cleanedSentences = {}
   sentenceCount=1
   for sentence in sentences:
       if sentence.strip():
           cleanedSentences[sentenceCount] = sentence.strip()
           sentenceCount+=1

   words={}
   for index, sentence in cleanedSentences.items():
       wordList = sentence.split()
       words[index] = wordList

   characters = {}
   for index, wordList in words.items():
       characterList = []
       for word in wordList:
           characterList.extend([list(word)])
       characters[index] = characterList

   return cleanedSentences, words, characters







def decodeMessage(text, message):
   # Write your code here
  global firstNum
  global secondNum
  global thirdNum
  sentences, words, characters = splitParagraph(text)
  seperatedMessage = message.split(' ')
  for item in seperatedMessage:
    numbers = item.split('.')
    firstNum = int(numbers[0])
    secondNum = int(numbers[1])
    thirdNum = int(numbers[2])
    try:
      print(characters[firstNum][(secondNum-1)][(thirdNum-1)],end='')
    except IndexError:
      print(' ',end='')
    except KeyError:
      print(' ',end='')


decodeMessage("To be or not to be that is the question is a quote by William Shakespeare.  2B or not 2B is also a Boolean expression.  Write it both ways.", '2.1.2 1.3.1 1.4.2 2.8.4 1.13.5 2.7.1 2.3.1 1.17.2 1.15.5 1.10.4 4.1.1 1.15.6 2.8.4 3.4.1 1.7.3 3.4.3 1.16.6 3.3.5 1.1.1 1.3.2 1.13.2 1.10.3')
