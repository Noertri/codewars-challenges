---
tags: [codewars coding challenges]
title: Codewars coding challenges
created: '2024-01-31T04:55:15.216Z'
modified: '2024-05-23T05:38:58.646Z'
---

# Codewars coding challenges


- [x] List Filtering (7 kyu) --> complete!!!

  DESCRIPTION:
  In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

  Example:
  ```Python
  filter_list([1,2,'a','b']) == [1,2]
  filter_list([1,'a','b',0,15]) == [1,0,15]
  filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
  ```

- [x] Regex validate PIN code (7 kyu)

  DESCRIPTION:
  ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

  If the function is passed a valid PIN string, return true, else return false.

  Examples (Input --> Output)

  ```
  "1234"   -->  true
  "12345"  -->  false
  "a234"   -->  false
  ```

- [x] Create Phone Number (6 kyu)

  DESCRIPTION:
  Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

  Example

  ```Python
  create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
  ```

  The returned format must be correct in order to complete this challenge.

  Don't forget the space after the closing parentheses!

- [x] Factorial (7 kyu)
    
  DESCRIPTION:
  In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

  Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) or ValueError (Python) or return -1 (C).

  More details about factorial can be found here.

- [x] Alphabetical Addition (7 kyu)

  DESCRIPTION:
  Your task is to add up letters to one letter.

  The function will be given a variable amount of arguments, each one being a letter to add.

  Notes:
  * Letters will always be lowercase.
  * Letters can overflow (see second to last example of the description)
  * If no letters are given, the function should return 'z'

  Examples:

  ```Python
  add_letters('a', 'b', 'c') = 'f'
  add_letters('a', 'b') = 'c'
  add_letters('z') = 'z'
  add_letters('z', 'a') = 'a'
  add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
  add_letters() = 'z'
  ```

  Confused? Roll your mouse/tap over here

