import zipfile
import time

folderpath=input("ENTER FILE PATH TO CRACK :- ")
zipf=zipfile.ZipFile(folderpath)

if not zipf:
    print("FILE IS NOT PASSWORD PROTECTED YOU CAN EASILY OPEN IT...")

else:
    starttime=time.time()
    result=0
    c=0

    characters =['0','1','2','3','4','5','6','7','8','9',
                 'a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','p','Q','R','S','T','U','V','W','X','Y','Z',
                 '!','@','#','$','%','=',':','?','.','/','|','~','>','*','(',')','<','}','{','^','[',']',' ','+','-','_','&',';','"','?','`',"'",'\\']
 
    print("BRUTE FORCE STARTED...")

    if(result == 0):
        print("Checking for four character password")
        #for loop to check each letter of password of 4 characters qas the characters increase we need to write more for lops as per digits in password 
        for i in characters :
            for j in characters :
                for k in characters :
                    for l in characters :
                        password =  str(i)+str(j)+str(k)+str(l)
                        c = c+1
                        print(password)
                        try:
                           with zipfile.ZipFile(folderpath ,'r' ) as zf:
                            zf.extractall(pwd=password.encode('utf-8'))
                            endtime = time.time()
                            result = 1
                            break
                        except:
                            pass
                    if(result == 1):
                        break
                if(result == 1):
                    break
            if(result == 1):
                break
    if(result == 0):
            print("Sorry, password not found. A total of "+str(c)+"+ possible combinations tried in "+str(duration)+" seconds. Password is not of 4 characters.")
    else:
        duration = endtime - starttime
        print('Congratulations!!! Password found after trying '+str(c)+' combinations in '+str(duration)+' seconds')
