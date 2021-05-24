import random
allNameList=[]
moreLinks=True
moreLinks='True'
while moreLinks=='True':
    nm=input('Enter your name: ')
    captGen=str(random.randint(0,9)**6)
    entrCapt=input('Enter Captcha=>'+captGen+': ')
    if entrCapt==captGen:
        print('Registered successully!!')  
        moreLinks=input('Do you want to continue?(True/False)')
        allNameList.append(nm)
    
    
