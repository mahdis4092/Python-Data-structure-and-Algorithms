def Anagram(s1,s2):
    str1=sorted(s1)
    str2=sorted(s2)
    if len(str1)!=len(str2):
        return False
    else:
        for i in range(len(str1)):
            if str1[i]!=str2[i]:
                return False

        return True



if __name__=='__main__':
    #s1 = ['l', 'h', 'u', 'v', 'o']
    #s2 = ['h', 's', 'o', 'v', 'u']
    #or
    s1='shuvo'
    s2='ovshp'
    print(Anagram(s1, s2))



