#👉 What is wrong the code below?
#print("SECURE LOGIN")
#username = input("Username > ")
#if username == "mark":
#print("Welcome Mark!")
#else:
#print("Go away!")
#elif username == "suzanne":
#print("Hey there Suzanne!")


# The elif statement is in the wrong place. It must go in between the if and else statements.

print("SECURE LOGIN")
username = input("Username > ")
if username == "mark":
  print("Welcome Mark!")
elif username == "suzanne":
  print("Hey there Suzanne!")
else:
  print("Go away!")
