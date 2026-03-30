Day 8 - 100 Days of Code: Project Day! Affirmations / Insults

Table of Contents
Day 8 Challenge
Common Errors
Solution (No Peeking!)

Youtube link 
https://www.youtube.com/watch?app=desktop&v=3SXW63IIs4I

Replit Link:
https://replit.com/@replit/day-8-100-days




















👉 Day 8 Challenge
Affirmations (or insults) Generator
Today's focus is using all the skills you have learned so far:
input and output
concatenation
if statements
nested if statements
Build a custom affirmations generator to give the user a customized affirmation each day of the week.
Make sure you ask the user for their name, the current day of the week, and a few of their favorite things. All of this information should be used to help you build your affirmations.
Hint: Think of these as variables.
The goal is to generate a unique message for each day of the week based on the user's answers.
Hint: use if and nested if statements
Use concatenation to generate the affirmation.
If affirmations are not your jam, then you could do a daily joke or insult. Please don't be mean. Keep it light and funny.
Final challenge: Can you create if statements that do not care about capital or lowercase letters of names.
Hint: Don't forget to restate the full question. name ==. The next chapter will explain this.























Common Error with If Statements
Here is a common error when joining if statements using logical conditions and or not.
In this example, I am trying to ignore the capitalization of the name for saying hi to Dave with or.
name = input("Name: ")
if name == "Dave" or "dave":
 print("Hi Dave")
The computer does not read the if statement in the same way a person does. The left side is saying "If the name is equal to Dave", but the computer reads the right side as saying "Does Dave exist?"
Here is how we fix this:
We need to restate the full question.
name = input("Name: ")
if name == "Dave" or name == "dave":
 print("Hi Dave")





