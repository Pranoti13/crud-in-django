#KDNinfoTech=>kdnInfOtEch
s = 'KDNinfoTech'
str1 = ""
l=len(s)
#vowels capital consonant small
for i in range(l):
    if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
        str = (s[i]).upper()
        str1+=str
    else:
        str1+=(s[i]).lower()
print(str1)


