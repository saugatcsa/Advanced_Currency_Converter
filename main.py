# create dictionaries for usd and eur
# input 3 info from user
  # one has to be a float
# convert from dollars to euros (1/.83) = 1.20
# if else - easy part  if alredy in table
# Advanced part converting to the different table 
  #  convert from dollars to euros OR euros to dollars
  #  to be in the right talbe

usd_ex = {
  "EUR" : 00.83,
  "GBP" : 00.74,
  "INR" : 73.13,
  "XBT" : 00.01
}

eur_ex = {
  "AUD" : 01.61,
  "MXN" : 25.90,
  "USD" : 1.20
}

user = (float(input("Enter an amount to convert:")))
print(
'''
Select a Currency from the following options:
* USD
* EUR
* GBP
* INR
* XBT
* AUD
* MXN
'''
)
a = (input("Enter the currency you're converting from: "))
print(
'''
Select a Currency from the following options:
* USD
* EUR
* GBP
* INR
* XBT
* AUD
* MXN
'''
)
b = (input("Enter the currency you're converting to:"))

if a == "USD" and (b == "EUR" or b == "GBP" or b == "INR" or b == "XBT"):
  x = usd_ex[b] * user
elif a == "EUR" and (b == "AUD" or b == "MXN" or b == "USD"):
  x = eur_ex[b] * user

elif a == "EUR" and (b == "GBP" or b == "INR" or b == "XBT"):
  conv =  user * usd_ex["USD"]
  x = usd_ex[b] * conv
elif a == "USD" and (b == "AUD" or b == "MXN"):
  conv = user * usd_ex["EUR"]
  x = eur_ex[b] * conv

print (x)