
alphabet = {}
final = {}
encoded={}
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']




for letter in letters:
  alphabet[letter]=str(letters.index(letter)+1)
encoded=alphabet
print(alphabet)

print('\n')
newNum=0
for key, value in encoded.items():
  num = int(value)
  if (num <= 5):
    newNum = num * 2
  elif (6 <= num <= 10):
      value = num % 3
      newNum = value * 5
  elif (11 <= num <= 15):
      value = num // 4
      newNum = value * 8
  elif (16 <= num <= 20):
      new_str = str(num)
      sepe = list(new_str)
      sepe = [int(numb) for numb in sepe]
      total = sum(sepe)
      newNum = total * 10
  elif (21 <= num <= 26):
      factors = []
      for i in range(1, num):
          if num % i == 0 and i != num:
              factors.append(i)
      maxi = max(factors)
      newNum = maxi * 12
  encoded[key]=newNum
  if(encoded[key]>26):

    encoded[key] = (encoded[key] - 1) % 26 + 1


print(encoded)
valed=0

for letter in letters:
  final[letter]=str(letters.index(letter)+1)

while True:
  inputz = input('Enter a letter: ')
  if(inputz=='stop'):
    break
  for key, value in encoded.items():
    if(inputz==key):
      valed=value
  for key,value in final.items():
    if(int(value)==valed):
      print(key)
