# Hashmap Repeated Word

[code_challenge_31](https://canvas.instructure.com/courses/3826570/assignments/26339207?return_to=https%3A%2F%2Fcanvas.instructure.com%2Fcalendar%23view_name%3Dmonth%26view_start%3D2022-03-12)

- Write a function called repeated word that finds the first word to occur more than once in a string
- Arguments: string
- Return: string

## Stretch

- Modify your function to return a count of each of the words in the provided string
- Modify your function to return a list of the words most frequently used in the provided string

## Whiteboard Process

![whiteboard](hashmap_repeat_word.png)

## Approach & Efficiency

Strip the text into a list of words using a find.all regular expression method.
Then iterate through the list putting each word into a dictionary. If the word is already present, increment the word value. 
The first word to be counted twice should be returned as the first duplicated word.

## Solution

> pytest -v -m hr
