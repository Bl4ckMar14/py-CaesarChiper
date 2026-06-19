import time
from Library.simbol import simboljadi, asciiArt ,simboll1 ,simboll2 ,simbolSuces
from colorama import Fore, Style


print(asciiArt)
time.sleep(1)

def classic(uperLower,shift,huruf):
   hurufA = ord(uperLower)
   hurufinput = ord(huruf)
   sft = shift

   posisi = hurufinput - hurufA
   geser = posisi + sft
   mod = geser %26
   pra = mod + hurufA
   end = chr(pra)
   return end

def classicCaesar():
    mode = input(f"{simboljadi}Encrypt[e] or Decrypt[d] :")

    if mode == "e":
       plaintext = input(f"{simboljadi}Enter Plaintext:")
       shift = int(input(f"{simboljadi}Enter shift 1-26:"))
       time.sleep(2)
       print(f"{simbolSuces}Encrypted Succesfull :" , end="")
       time.sleep(1.8)
       for i in plaintext:
          if i.isupper()  :
             jadi = classic("A",shift,i)
          elif i.islower():
             jadi = classic("a",shift,i)
          else :
             jadi = i
          print(jadi,end="")
    elif mode == "d":
       enctext = input(f"{simboljadi}Enter Encrypted text:")
       shift = int(input(f"{simboljadi}Enter Shift 1-26:"))
       time.sleep(2)
       sftdec = shift * -1
       print(f"{simbolSuces}Decrypt Succesfull:" ,end="")
       time.sleep(1.8)
       for i in enctext :
          if i.isupper():
             jadi = classic("A",sftdec,i)
          elif i.islower():
             jadi = classic("a",sftdec,i)
          else :
             jadi = i
          print(jadi,end="")
    else :
       print(f"\n{simbolSuces}Program Stopped ;)")


def bruteForce(shifted, plaintext):
   max = 24
   sft = 0
   if shifted >= 0 :
    print(f"\n{simboljadi}Encrypted !")
   if shifted <= 0 :
    print(f"\n\n{simboljadi}Decrypted !")
      
   while max >= sft :
      sft += 1
      shft = sft * shifted
      print(f"\n{simbolSuces}Shift.{sft}: " , end="" )
      for i in plaintext:
         if i.isupper()  :
            jadi = classic("A",shft,i)
         elif i.islower():
            jadi = classic("a",shft,i)
         else :
            jadi = i
         print(jadi,end="")

def bruteForceED():
   plaintext = input(f"{simboljadi}Enter Plaintext:")
   time.sleep(1)
   bruteForce(1,plaintext)
   bruteForce(-1,plaintext)

       
print(f"{simboljadi}Welcome to Caesar Chiper ")
time.sleep(1)

def mudi():
   print(f"\n{simboljadi}Select Mode\n")
   time.sleep(0.3)
   print(f"{simboll1}Normal Mode")
   time.sleep(0.2)
   print(f"{simboll2}Brute Force Mode\n")
   time.sleep(0.2)

def main():
   mudi()
   mode = str(input(f"{simboljadi}1/2 :" ))
   time.sleep(0.1)
   if mode == "1":
      classicCaesar()
      input1 = str(input(f"\n\n{simboll1}Back to menu\n{simboll2}Exit\n{simboljadi}1/2 :"))
      if input1 == "1" :
         main()
      elif input1 == "2":
         print(f"\n{simbolSuces}Program stopped !")
         exit()
      else :
         print(f"\n{simbolSuces}Program Stopped !")
         exit()
   elif mode == "2":
      bruteForceED()
      input1 = str(input(f"\n\n{simboll1}Back to menu\n{simboll2}Exit\n{simboljadi}1/2 :"))
      if input1 == "1" :
         main()
      elif input1 == "2":
         print(f"\n{simbolSuces}Program Stopped !")
         exit()
      else :
         print(f"\n{simbolSuces}Program Stopped !")
         exit()
   else:
      exit()

 
if __name__ == "__main__" :
   main()