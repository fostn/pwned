print("""
 ____  _    _  _  _  ____  ____     ___ 
(  _ \( \/\/ )( \( )( ___)(  _ \   (__ )
 )___/ )    (  )  (  )__)  )(_) )   (_/ 
(__)  (__/\__)(_)\_)(____)(____/    (_)                    

insta : @f09l | Twitter : @lwv5 | Telegram : @ifostn
""")
print("[This tool to check if you email been hacked]")

email = input("Enter the Email : ")
import requests
url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}?truncateResponse=false"
headers = {
	"User-Agent":"Spamlock/1.3.0 CFNetwork/1220.1 Darwin/20.3.0",
	"hibp-api-key":"19845a8c362a464b837f724beada9cf2"
}
r=requests.get(url,headers=headers)
if '"Name"' in r.text:	
	for new in r.json():
		print(str("Name : "+ new["Name"]))
		print(str("Hacked Date : "+new["BreachDate"]))
		print(str("Title : "+new["Title"]))
		print(str("Domain : "+new["Domain"]))
		print(str("Added Date : "+new["AddedDate"]))
		print(str("Modified Date : "+new["ModifiedDate"]))
		print("IsVerified :"+str(new["IsVerified"]))
		print("Is Fabricated : "+str(new["IsFabricated"]))
		print("Is Sensitive : "+str(new["IsSensitive"]))
		print("Is Retired : "+str(new["IsRetired"]))
		print("Is SpamList : "+str(new["IsSpamList"]))
		print("Is Malware : "+str(new["IsMalware"]))
		print("________________________")

elif email == "":
    print("Email required ! ")
else:
	print("Good news no data found !")
