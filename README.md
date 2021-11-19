# parenthesisCheck

## Back to Hacking 2021 run by Major League Hacking
November 19-21, 2021

## Goal:
Implement a web application that takes user input and returns the validity of having balanced parenthesis.

### Background:
Balanced parenthesis is a common programming problem that checks whether or not all open parenthesis have a closing parenthesis and are properly nested.
[GeeksforGeeks Balanced Parenthesis](https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/)

### Algorithm:
The algorithm utilizes a stack data structure. This is a data structure that follows a First In Last Out principle. As we search through the input, upon every occurrence of an open parenthesis '(' we add it to the stack. When we encounter a closed parenthesis ')' we check that the top of the stack contains a '('. If so, we Pop it off the stack i.e remove it and continue. If we encounter another closed parenthesis ')' on the top of the stack we return False as the parenthesis are not nested properly. If we search the entire input and our stack is empty then we can return True.

## Web Application:
Our web application is built utilizing the Flask web framework. The homepage will contain two options to pass different input types, either as a file of supported kind(See below) or as a string. Each option will direct you to another page where the process will take place. Upon completion, you will be redirected to the home page and prompted to repeat the process.

`![Decision flowchart](https://github.com/jlangner15/parenthesisCheck/flowDiagram1.jpg)`

## Three Flaskateers:
This is our first hackathon individually and as a group!  The three of us have different education backgrounds and come from different countries. The three of us have similar tech experience however but none of us have used Flask. 
