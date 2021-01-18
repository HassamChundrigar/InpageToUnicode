#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[294]:


globalOptions = {
    "rbtnUrdu": True,           #/* Urdu? */
    "chkHehHamza": True,        #/* Correct heh with Hamza? */
    "chkRKashida": False,       #/* Remove Kashida Sign? */
    "chkQuotMarks": True,      #/* Reverse Quotation Marks? */
    "chkRDigits": True,         #/* Reverse Number / Digits? */
    "chkReverseSSign": True,    #/* Reverse Solidus (/) Sign? */
    "chkThousSeparator": True,  #/* Reverse Thousands Separator? */
    "chkBariYee": True,         #/* Correct Bari Ya? */
    "chkRDoubleSpace": True,    #/* Remove Double Space? */
    "chkRErabs": False,         #/* Remove All Erabs? */
    "chkYearSign": True         #/* Correct Year Sign? */
}


# In[295]:


with open('file.INP', 'rb') as f:
    data = f.read()


# In[296]:


def findStartPosition(data):
    for i, char in enumerate(data):
        if ((chr(char) == chr(1)) & (chr(data[i+4])== chr(13))):
            tempTest = ""
            for t in range(10):
                tempTest += str(data[i+t])
            if tempTest == "10001300000":
                return i+14


# In[297]:


def findEndPosition(data, start):
    for i in range(start, len(data)):
        if chr(data[i+6]) == chr(255):
            tempTest = ""
            for t in range(10):
                tempTest += str(data[i+t])
            if tempTest == "1300000255255255255":
                return i


# In[298]:


def convert2BitString(data, start, length):
    hexChar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    res = "";
    for i in range(start, start+length):
        b = data[i]
        res += "-" + hexChar[(b >> 4) & 0x0f] + hexChar[b & 0x0f]
    return res


# In[299]:


rbtnUrdu = globalOptions["rbtnUrdu"];
chkHehHamza = globalOptions["chkHehHamza"];
chkRKashida = globalOptions["chkRKashida"];
chkQuotMarks = globalOptions["chkQuotMarks"];
chkRDigits = globalOptions["chkRDigits"];
chkReverseSSign = globalOptions["chkReverseSSign"];
chkThousSeparator = globalOptions["chkThousSeparator"];
chkBariYee = globalOptions["chkBariYee"];
chkRDoubleSpace = globalOptions["chkRDoubleSpace"];
chkRErabs = globalOptions["chkRErabs"];
chkYearSign = globalOptions["chkYearSign"];
myEnter = chr(13)+chr(10)
myTab = chr(9)
regReverseEngWSpace = "[0-9]+[ ][0-9 ?]+[0-9]";
regEnter = "-0D-[^-]+-[^-]+-[^-]+-[^-]+[^-]";
regRemoveAhrab = "[ ًٌٍَُِّٰٖٗ]";
regUDigits = "[۰۱۲۳۴۵۶۷۸۹][۰۱۲۳۴۵۶۷۸۹/+×÷%,]+";
regADigits = "[٠١٢٣٤٥٦٧٨٩][٠١٢٣٤٥٦٧٨٩/+×÷%,]+";
regOnlyUDigits = "[۰۱۲۳۴۵۶۷۸۹][۰۱۲۳۴۵۶۷۸۹]+";
regOnlyADigits = "[٠١٢٣٤٥٦٧٨٩][٠١٢٣٤٥٦٧٨٩]+";
regUrduAlfabat = "([ابپتٹثجچحخدڈذرڑزژسشصضطظعغفقکكگلمنوئیےؤهۀةأـآيھإہۃں])";
regAhrab = "([ًٌٍَُِّٰٖٗ])"  #zair is inside
regNoonGuna = "(ں)" + regUrduAlfabat;
regHamza = "(ء)" + regUrduAlfabat;
regHamzaWAhrab = "(ء)" + regAhrab + regUrduAlfabat;


# In[300]:


startP = findStartPosition(data);
endP = findEndPosition(data, startP);
slength = endP - startP;


# In[301]:


newOutput = convert2BitString(data, startP, slength)


# In[302]:


newOutput = re.sub(regEnter, myEnter, newOutput)
newOutput = re.sub('-09', myTab, newOutput);
newOutput = re.sub('-04-AA', "ِ", newOutput); #ZEIR
newOutput = re.sub('-04-20', " ", newOutput);
newOutput = re.sub('-04-81-04-B3', "آ", newOutput);
newOutput = re.sub('-04-81-04-BF', "أ", newOutput);
newOutput = re.sub('-04-81', "ا", newOutput);
newOutput = re.sub('-04-82', "ب", newOutput);
newOutput = re.sub('-04-83', "پ", newOutput);
newOutput = re.sub('-04-84', "ت", newOutput);
newOutput = re.sub('-04-85', "ٹ", newOutput);
newOutput = re.sub('-04-86', "ث", newOutput);
newOutput = re.sub('-04-87', "ج", newOutput);
newOutput = re.sub('-04-88', "چ", newOutput);
newOutput = re.sub('-04-89', "ح", newOutput);
newOutput = re.sub('-04-8A', "خ", newOutput);
newOutput = re.sub('-04-8B', "د", newOutput);
newOutput = re.sub('-04-8C', "ڈ", newOutput);
newOutput = re.sub('-04-8D', "ذ", newOutput);
newOutput = re.sub('-04-8E', "ر", newOutput);
newOutput = re.sub('-04-8F', "ڑ", newOutput);
newOutput = re.sub('-04-90', "ز", newOutput);
newOutput = re.sub('-04-91', "ژ", newOutput);
newOutput = re.sub('-04-92', "س", newOutput);
newOutput = re.sub('-04-93', "ش", newOutput);
newOutput = re.sub('-04-94', "ص", newOutput);
newOutput = re.sub('-04-95', "ض", newOutput);
newOutput = re.sub('-04-96', "ط", newOutput);
newOutput = re.sub('-04-97', "ظ", newOutput);
newOutput = re.sub('-04-98', "ع", newOutput);
newOutput = re.sub('-04-99', "غ", newOutput);
newOutput = re.sub('-04-9A', "ف", newOutput);
newOutput = re.sub('-04-9B', "ق", newOutput);


# In[303]:


if rbtnUrdu:
    newOutput = re.sub('-04-9C', "ک", newOutput);
else:
    newOutput = re.sub('-04-9C', "ك", newOutput);


# In[304]:


newOutput = re.sub('-04-9D', "گ", newOutput);
newOutput = re.sub('-04-9E', "ل", newOutput);
newOutput = re.sub('-04-9F', "م", newOutput);
newOutput = re.sub('-04-A0', "ن", newOutput);
newOutput = re.sub('-04-A1', "ں", newOutput);


# In[305]:


if chkHehHamza:
    newOutput = re.sub('-04-A3-04-A2', "ؤ", newOutput);
    newOutput = re.sub('-04-BF-04-A2', "ؤ", newOutput);
else:
    newOutput = re.sub('-04-A3-04-A2', "ئو", newOutput);


# In[306]:


newOutput = re.sub('-04-A2-04-BF', "ؤ", newOutput);


# In[307]:


if rbtnUrdu:
    if chkHehHamza:
        newOutput = re.sub('-04-BF-04-A6', "ۂ", newOutput);
        newOutput = re.sub('-04-A3-04-A6', "ۂ", newOutput);
    newOutput = re.sub('-04-A6-04-BF', "ۂ", newOutput);
else:
    newOutput = re.sub('-04-A6-04-BF', "ۀ", newOutput);


# In[308]:


newOutput = re.sub('-04-A3-04-A6', "ئہ", newOutput);
newOutput = re.sub('-04-A2', "و", newOutput);
newOutput = re.sub('-04-A3', "ء", newOutput);
newOutput = re.sub('-04-A4-04-BF', "ئ", newOutput);


# In[309]:


if rbtnUrdu: 
    newOutput = re.sub('-04-A4', "ی", newOutput);
else: 
    newOutput = re.sub('-04-A4', "ي", newOutput);

newOutput = re.sub('-04-A5', "ے", newOutput);
if rbtnUrdu: 
    newOutput = re.sub('-04-A6', "ہ", newOutput);
    newOutput = re.sub('-04-A7', "ھ", newOutput);
else: 
    newOutput = re.sub('-04-A6', "ه", newOutput);
    newOutput = re.sub('-04-A7', "ه", newOutput);

newOutput = re.sub('-04-A8', "ٍ", newOutput); #2 ZEIR NICHE
if chkRKashida: 
    newOutput = re.sub('-04-A9', "", newOutput); #169 TATWEEL
else: 
    newOutput = re.sub('-04-A9', "ـ", newOutput)
    


# In[310]:


newOutput = re.sub('-04-AA', "ِ", newOutput);# //ZEIR
newOutput = re.sub('-04-AB', "َ", newOutput);# //ZABAR
newOutput = re.sub('-04-AC', "ُ", newOutput);# //PAESH
newOutput = re.sub('-04-AD', "ّ", newOutput);# //0651 UNICODE VALUE
newOutput = re.sub('-04-AE', "ؑ", newOutput);# //ALAH ISLAM SH
newOutput = re.sub('-04-B0', "ٖ", newOutput);# //KHARI ZEIR


# In[311]:


if rbtnUrdu:
    newOutput = re.sub('-04-B1-04-B1', "ْ", newOutput);# //SAKIN
    newOutput = re.sub('-04-B1', "ْ", newOutput);# //SAKIN
else:
    newOutput = re.sub('-04-B1-04-B1', "ْ", newOutput);# //SAKIN
    newOutput = re.sub('-04-B1', "ْ", newOutput);# //SAKIN


# In[312]:


newOutput = re.sub('-04-B3', "ٓ", newOutput);# //MAD
newOutput = re.sub('-04-B4', "ْ", newOutput);# //SAKIN
newOutput = re.sub('-04-B5', "ٌ", newOutput);# //PAESH TYPE PHOOL
newOutput = re.sub('-04-B6', "ؤ", newOutput);#
newOutput = re.sub('-04-B7', "ئ", newOutput);#
newOutput = re.sub('-04-B8', "ي", newOutput);#


# In[313]:


if rbtnUrdu:
    newOutput = re.sub('-04-B9', "ۃ", newOutput);
else:
    newOutput = re.sub('-04-B9', "ة", newOutput);


# In[314]:


newOutput = re.sub('-04-BD', "ٰ", newOutput);# //KHARI ZABAR
newOutput = re.sub('-04-BE', "ٗ", newOutput);# //ULTA PAESH
newOutput = re.sub('-04-BF', "ٔ", newOutput);# //HAMZA OOPER

newOutput = re.sub('-04-C7', "ً", newOutput);# //2 ZABAR OOPAR
newOutput = re.sub('-04-C8', "آ", newOutput);#
newOutput = re.sub('-04-C9', "أ", newOutput);#
newOutput = re.sub('-04-CA', "إ", newOutput);#
newOutput = re.sub('-04-CB', "ﷲ", newOutput);# //ALLAH
newOutput = re.sub('-04-CF', "ؔ", newOutput);#  //207


# In[315]:


if rbtnUrdu:
    newOutput = re.sub('-04-D0', "۰", newOutput);
    newOutput = re.sub('-04-D1', "۱", newOutput);
    newOutput = re.sub('-04-D2', "۲", newOutput);
    newOutput = re.sub('-04-D3', "۳", newOutput);
    newOutput = re.sub('-04-D4', "۴", newOutput);
    newOutput = re.sub('-04-D5', "۵", newOutput);
    newOutput = re.sub('-04-D6', "۶", newOutput);
    newOutput = re.sub('-04-D7', "۷", newOutput);
    newOutput = re.sub('-04-D8', "۸", newOutput);
    newOutput = re.sub('-04-D9', "۹", newOutput);
else:
    newOutput = re.sub('-04-D0', "٠", newOutput);
    newOutput = re.sub('-04-D1', "١", newOutput);
    newOutput = re.sub('-04-D2', "٢", newOutput);
    newOutput = re.sub('-04-D3', "٣", newOutput);
    newOutput = re.sub('-04-D4', "٤", newOutput);
    newOutput = re.sub('-04-D5', "٥", newOutput);
    newOutput = re.sub('-04-D6', "٦", newOutput);
    newOutput = re.sub('-04-D7', "٧", newOutput);
    newOutput = re.sub('-04-D8', "٨", newOutput);
    newOutput = re.sub('-04-D9', "٩", newOutput);


# In[316]:


newOutput = re.sub('-04-DA', "!", newOutput); #//218
newOutput = re.sub('-04-DB', "﴾", newOutput); #//SP B
newOutput = re.sub('-04-DC', "﴿", newOutput);#
newOutput = re.sub('-04-DE', "%", newOutput);#
newOutput = re.sub('-04-DF', "/", newOutput);#
newOutput = re.sub('-04-E0', "……", newOutput);# // ... DBL
newOutput = re.sub('-04-E1', ")", newOutput); #//N B
newOutput = re.sub('-04-E2', "(", newOutput); #//N B
newOutput = re.sub('-04-E4', "+", newOutput);#
newOutput = re.sub('-04-E6', "ؓ", newOutput); # //RAZI ALLAH SH
newOutput = re.sub('-04-E7', "ؒ", newOutput); # //RAHMATU ALLAH SH
newOutput = re.sub('-04-E8', "٭", newOutput);#
newOutput = re.sub('-04-E9', ":", newOutput); #//233
newOutput = re.sub('-04-EA', "؛", newOutput);
newOutput = re.sub('-04-EB', "×", newOutput);
newOutput = re.sub('-04-EC', "=", newOutput);
newOutput = re.sub('-04-ED', "،", newOutput);
newOutput = re.sub('-04-EE', "؟", newOutput);
newOutput = re.sub('-04-EF', "÷", newOutput);
newOutput = re.sub('-04-F1', "؍", newOutput);
newOutput = re.sub('-04-F2', "؂", newOutput);


# In[317]:


if rbtnUrdu:
    newOutput = re.sub('-04-F3', "۔", newOutput);
else:
    newOutput = re.sub('-04-F3', ".", newOutput);


# In[318]:


newOutput = re.sub('-04-F5', "-", newOutput);# //245  /
newOutput = re.sub('-04-F6', "ﷺ", newOutput);# //PBUH
newOutput = re.sub('-04-F7', "؁", newOutput);#  //247
newOutput = re.sub('-04-F8', "ؐ", newOutput);# //PBUH SHORT
newOutput = re.sub('-04-F9', ",", newOutput);#
newOutput = re.sub('-04-FA', "]", newOutput);#
newOutput = re.sub('-04-FB', "[", newOutput);#
newOutput = re.sub('-04-FC', ".", newOutput);#  //.


# In[319]:


if chkQuotMarks:
    newOutput = re.sub('-04-FE', "’", newOutput);#  //254
    newOutput = re.sub('-04-FD', "‘", newOutput);#  //253
else:
    newOutput = re.sub('-04-FD', "’", newOutput);#  //253
    newOutput = re.sub('-04-FE', "‘", newOutput);#  //254


# In[320]:


newOutput = re.sub('-04-3A', "", newOutput);
newOutput = re.sub('-04-3B', "", newOutput);
newOutput = re.sub('-09', myTab, newOutput);
newOutput = re.sub('-20', " ", newOutput);
newOutput = re.sub('-21', "!", newOutput);
newOutput = re.sub('-22', chr(34), newOutput);
newOutput = re.sub('-23', "#", newOutput);
newOutput = re.sub('-24', "$", newOutput);
newOutput = re.sub('-25', "%", newOutput);
newOutput = re.sub('-26', "&", newOutput);
newOutput = re.sub('-27', "'", newOutput);
newOutput = re.sub('-28', "(", newOutput);
newOutput = re.sub('-29', ")", newOutput);
newOutput = re.sub('-2A', "*", newOutput);
newOutput = re.sub('-2B', "+", newOutput);
newOutput = re.sub('-2C', ",", newOutput);
newOutput = re.sub('-2D', "-", newOutput);
newOutput = re.sub('-2E', ".", newOutput);
newOutput = re.sub('-2F', "/", newOutput);
newOutput = re.sub('-3A', ":", newOutput);
newOutput = re.sub('-3B', ";", newOutput);
newOutput = re.sub('-3C', "<", newOutput);
newOutput = re.sub('-3D', "=", newOutput);
newOutput = re.sub('-3E', ">", newOutput);
newOutput = re.sub('-3F', "?", newOutput);
newOutput = re.sub('-40', "@", newOutput);
newOutput = re.sub('-41', "A", newOutput);
newOutput = re.sub('-42', "B", newOutput);
newOutput = re.sub('-43', "C", newOutput);
newOutput = re.sub('-44', "D", newOutput);
newOutput = re.sub('-45', "E", newOutput);
newOutput = re.sub('-46', "F", newOutput);
newOutput = re.sub('-47', "G", newOutput);
newOutput = re.sub('-48', "H", newOutput);
newOutput = re.sub('-49', "I", newOutput);
newOutput = re.sub('-4A', "J", newOutput);
newOutput = re.sub('-4B', "K", newOutput);
newOutput = re.sub('-4C', "L", newOutput);
newOutput = re.sub('-4D', "M", newOutput);
newOutput = re.sub('-4E', "N", newOutput);
newOutput = re.sub('-4F', "O", newOutput);
newOutput = re.sub('-50', "P", newOutput);
newOutput = re.sub('-51', "Q", newOutput);
newOutput = re.sub('-52', "R", newOutput);
newOutput = re.sub('-53', "S", newOutput);
newOutput = re.sub('-54', "T", newOutput);
newOutput = re.sub('-55', "U", newOutput);
newOutput = re.sub('-56', "V", newOutput);
newOutput = re.sub('-57', "W", newOutput);
newOutput = re.sub('-58', "X", newOutput);
newOutput = re.sub('-59', "Y", newOutput);
newOutput = re.sub('-5A', "Z", newOutput);
newOutput = re.sub('-5B', "[", newOutput);
newOutput = re.sub('-5C', "/",newOutput);
newOutput = re.sub('-5D', "]", newOutput);
newOutput = re.sub('-5E', "^", newOutput);
newOutput = re.sub('-5F', "_", newOutput);
newOutput = re.sub('-60', "`", newOutput);
newOutput = re.sub('-61', "a", newOutput);
newOutput = re.sub('-62', "b", newOutput);
newOutput = re.sub('-63', "c", newOutput);
newOutput = re.sub('-64', "d", newOutput);
newOutput = re.sub('-65', "e", newOutput);
newOutput = re.sub('-66', "f", newOutput);
newOutput = re.sub('-67', "g", newOutput);
newOutput = re.sub('-68', "h", newOutput);
newOutput = re.sub('-69', "i", newOutput);
newOutput = re.sub('-6A', "j", newOutput);
newOutput = re.sub('-6B', "k", newOutput);
newOutput = re.sub('-6C', "l", newOutput);
newOutput = re.sub('-6D', "m", newOutput);
newOutput = re.sub('-6E', "n", newOutput);
newOutput = re.sub('-6F', "o", newOutput);
newOutput = re.sub('-70', "p", newOutput);
newOutput = re.sub('-71', "q", newOutput);
newOutput = re.sub('-72', "r", newOutput);
newOutput = re.sub('-73', "s", newOutput);
newOutput = re.sub('-74', "t", newOutput);
newOutput = re.sub('-75', "u", newOutput);
newOutput = re.sub('-76', "v", newOutput);
newOutput = re.sub('-77', "w", newOutput);
newOutput = re.sub('-78', "x", newOutput);
newOutput = re.sub('-79', "y", newOutput);
newOutput = re.sub('-7A', "z", newOutput);
newOutput = re.sub('-7B', "{", newOutput);
newOutput = re.sub('-7C', "|", newOutput);
newOutput = re.sub('-7D', "}", newOutput);
newOutput = re.sub('-7E', "~", newOutput);
newOutput = re.sub('-7F', "", newOutput);
newOutput = re.sub('-30', "0", newOutput);
newOutput = re.sub('-31', "1", newOutput);
newOutput = re.sub('-32', "2", newOutput);
newOutput = re.sub('-34', "4", newOutput);
newOutput = re.sub('-35', "5", newOutput);
newOutput = re.sub('-36', "6", newOutput);
newOutput = re.sub('-37', "7", newOutput);
newOutput = re.sub('-38', "8", newOutput);
newOutput = re.sub('-39', "9", newOutput);
newOutput = re.sub('-33', "3", newOutput);


# In[321]:


if (chkRDigits & chkReverseSSign & chkThousSeparator):
    if rbtnUrdu: 
        temp_re = re.compile(regUDigits)
    else:
        temp_re = re.compile(regADigits)
    
    matches = [match for match in temp_re.finditer(newOutput)]
    i=0
    text = ""
    for match in matches:
        text += newOutput[i:match.start()]
        if match.group(0)[-1] == '/':
            text += match.group(0)[::-1]+"/"
        else:
            text += match.group(0)[::-1]
        i=match.end()
    text += newOutput[i:len(newOutput)]
    newOutput = text

elif (chkRDigits & (not chkThousSeparator)):
    if rbtnUrdu:
        re = re.compile(regOnlyUDigits)
    else:
        re = re.compile(regOnlyADigits)
    matches = [match for match in temp_re.finditer(newOutput)]
    i=0
    text = ""
    for match in matches:
        text += newOutput[i:match.start()]
        text += match.group(0)[::-1]
        i=match.end()
    text += newOutput[i:len(newOutput)]
    newOutput = text


# In[322]:


newOutput = re.sub("(\/)(=)", r"\2\1", newOutput);
newOutput = re.sub(regNoonGuna, r"\1 \2", newOutput);
newOutput = re.sub("(ﺀ)(ﺀ)", r'ئ\2', newOutput);
newOutput = re.sub(regHamza, r'ئ\2', newOutput);
newOutput = re.sub(regHamzaWAhrab, r"ئ\2\3", newOutput);


# In[323]:


if (chkBariYee): 
    newOutput = re.sub("(ے)" + regUrduAlfabat, r"ی\2", newOutput);
    
if (rbtnUrdu): 
    newOutput = re.sub("(ي)" + regUrduAlfabat, r"\1 \2", newOutput);

if (chkRDoubleSpace):
    newOutput = re.sub('[ ]+[ ]', " ", newOutput);

if (chkRErabs): 
    newOutput = re.sub(regRemoveAhrab, "", newOutput);

if (chkYearSign): 
    newOutput = re.sub("(ھ)(؁)", r"\2\1", newOutput)
    newOutput = re.sub("(ء)(؁)", r"\2\1", newOutput);


# In[324]:


with open('unicode.txt', 'w', encoding='utf-8') as f:
    f.write(newOutput)


# In[ ]:




