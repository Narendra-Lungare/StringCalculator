def replaceAlphabets(numbers):
   # function for replacing the  alphabets
   string_without_alphabets=""
   for ch in numbers:
      if(ch>='a' and ch<='z'):
         string_without_alphabets+=str(ord(ch)-ord('a')+1)
      else:
         string_without_alphabets+=ch
   return string_without_alphabets

def replaceNewlines(numbers):
   # function for replacing the newlines
   string_without_newlines=""
   i=0
   while(i<len(numbers)-1):
      if(numbers[i]=='\n'):
         string_without_newlines+=","
      else:
         string_without_newlines+=numbers[i:i+1]
      i+=1
   string_without_newlines+=numbers[-1]
   # print("string without new lines = ",string_without_newlines)
   return string_without_newlines


def getDelimitor(numbers):
   if(len(numbers)<6):
      return ""
   if(numbers[0:2]!="//"):
      return ""
   delimitor = ""
   for i in range(2,len(numbers)):
      if(numbers[i]=='\n'):
         break
      delimitor+=numbers[i:i+1]
   print("delimitor = ",delimitor)
   return delimitor

def replaceDelimitor(numbers,delimitor):
   delimitorFreestring=""
   for i in range(0,len(numbers)):
      isDelimitor=True
      for j in range(i,len(delimitor)):
         if(numbers[i+j]!=delimitor[j]):
            isDelimitor=False
            break
      if(isDelimitor):
         delimitorFreestring+=","
         i+=len(delimitor)-1
      else:
         delimitorFreestring+=numbers[i:i+1]
   # print("delimitor free string = ",delimitorFreestring)
   return delimitorFreestring

def checkforNegatives(numbers):
   neg_num=""
   i=0
   while(i < len(numbers)):
      if(numbers[i]=='-'):
         if(len(neg_num)>0):
            neg_num+=","
         for j in range(i,len(numbers)):
            if(numbers[j]!=","):
               neg_num+=numbers[j]
            else:
               i=j
               break
   if(len(neg_num)>0):
      raise NameError("Negatives not allowed => ",neg_num) 


def formatted_name(numbers):
   if(len(numbers)<=0):
      return 0

   # check for delimitor
   delimitor=getDelimitor(numbers)
   if(len(delimitor)>0):
      numbers=numbers[2+len(delimitor)+2:]
      numbers=replaceDelimitor(numbers,delimitor)

   # replace newlines with commas (used as default delimitor)
   numbers=replaceNewlines(numbers)

   # replace alphabets with their numeric value
   numbers=replaceAlphabets(numbers)


   numbers+=","
   ans=0
   cur=0
   for ch in numbers:
      if(ch==','):
         if(cur>1000):
            cur=0
         # adding the values to the ans
         ans+=cur
         cur=0
      else:
         cur*=10
         cur+=(ord(ch)-ord('0'))
   return ans