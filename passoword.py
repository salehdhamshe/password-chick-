
def checking_password(password: str) -> dict:
   special_chars = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"
   lenght=len(password)>=9
   capital_letter=any(ch.isupper() for ch in password)
   small_letter=any(ch.islower() for ch in password) 
   sp_chars= any(ch in special_chars for ch in password)
   digits= any(ch.isdigit() for ch in password)
   return{ 
      "lenght_ok ?": lenght,
      "contain capital_letter  ?":capital_letter,
      "contain small_letter  ?":small_letter,
      "contain digit ? ":digits,
      "contain special cahr  ? ": sp_chars,
            }


password=input("insert your passowrd:  ")
answer=checking_password(password)
values=list(answer.values())
i=0  
score=0
while i<5 :
   if values[i]==True:
      score+=1

  
   i+=1


for key, value in answer.items():
    print(f"{key}: {value}")

print(f"status passowrd is: {'weak' if  score<3 else ('medium' if score==3 else 'strong') }")