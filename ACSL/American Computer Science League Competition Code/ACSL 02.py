time = {1:9, 2:9.5, 3:10, 4:10.5, 5:11, 6:11.5, 7:12, 8:12.5, 9:13, 'A':13.5, 'B':14, 'C':14.5, 'D':15, 'E':15.5, 'F':16, 'G':16.5, 'H':17}


pay1=0
pay2=0
pay3=0
pay4=0
final = []
total=0
rStart=0
rEnd=0
runs = 0

while runs < 4:
  pay1=0
  pay2=0
  pay3=0
  pay4=0
  location = input('What was your location (1-29): ')
  start = input('What was your start time (1-H): ')
  end = input('What was your end time (1-H): ')


  if(int(location)==1 or int(location)==2 or int(location)==3 or int(location)==4 or int(location)==5 or int(location)==6 or int(location)==7 or int(location)==8 or int(location)==9):
    for key, value in time.items():
      if(str(start)==str(key)):
        rStart=value
      if(str(end)==str(key)):
        rEnd=value
    hours=float(rEnd)-float(rStart)
    pay1=hours*10
    final.append(pay1)
    print('$',pay1,'0',sep='')

  if(int(location)==10 or int(location)==11 or int(location)==12 or int(location)==13 or int(location)==14 or int(location)==15 or int(location)==16 or int(location)==17 or int(location)==18 or int(location)==19):
    for key, value in time.items():
      if(str(start)==str(key)):
        rStart=value
      if(str(end)==str(key)):
        rEnd=value
    hours=float(rEnd)-float(rStart)
    if(hours<=4):
      pay2=hours*8
    elif(hours>4):
      pay2=32+(12*(hours-4))
    final.append(pay2)
    print('$',pay2,'0',sep='')

  if(int(location)==20 or int(location)==21 or int(location)==22 or int(location)==23 or int(location)==24 or int(location)==25 or int(location)==26 or int(location)==27 or int(location)==28 or int(location)==29):
    for key, value in time.items():
      if(str(start)==str(key)):
        rStart=value
      if(str(end)==str(key)):
        rEnd=value
    hours=float(rEnd)-float(rStart)
    if(hours<=4):
      pay3=hours*12
    elif(hours>4):
      pay3=48+(24*(hours-4))
    final.append(pay3)
    print('$',pay3,'0',sep='')
  runs+=1
print('\nTotal Weekly Pay: ')
print('$',sum(final),'0',sep='')
