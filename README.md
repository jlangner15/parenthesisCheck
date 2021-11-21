# **ParenthesisValidator**

<br>

A Parenthesis Validator App is a must have app while working with programming languages. We never really know if the
file have all the Parenthesis Balanced or not. Only way is we can just pass those files or strings through our Web
App, and sit back and relax; it will do the job for you.

<br>

## **Back to Hacking 2021 run by Major League Hacking**

<br>

November 19-21, 2021

## **Three Flaskateers**

<br>

This is our first hackathon individually and as a group! The three of us have different educational backgrounds and come from different countries. All of us have similar tech experience however but none of us have used Flask before. It's a first for all of us.

<br>

## **Goal**

<br>

- Implement a web application that takes user input and returns the validity of having balanced parenthesis.
- Our App would be able to work for as many number of files and string inputs as the user wants just one at a time.
- Our App would check for the following parenthesis pairs : [], {}, and () while omitting other characters.

<br>

### **Background**

<br>

Balanced parenthesis is a common programming problem that checks whether or not all open parenthesis have a closing parenthesis and are properly nested.
[GeeksforGeeks Balanced Parenthesis](https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/)

<br>

## **Algorithm**

<br>

The algorithm utilizes a stack data structure that follows a First In Last Out principle. As we search through the input, upon every occurrence of an open parenthesis '(' we add it to the stack. When we encounter a closed parenthesis ')' we check that the top of the stack contains a '('. If so, we Pop it off the stack i.e remove it and continue. If we encounter another type of opening or an empty stack with a closing parenthesis then we return false as it isn't nested properly. If we search the entire string and our stack still has elements return False. If we search the entire input and our stack is empty then we can return True.

<br>

Our Algorithm works in the following visual manner:

<br>

### **For Strings**

<br>

```txt
We will be pushing a pair into our stack : pair <element, position>
********************************************************************************
Example 1 :
String : []
Our Algo will implement the stack as :

First call :
Stack : |'[', 1| pushed '[' into the stack

Second call :
Stack : |Empty| whenever we encounter any closing brace, we check if the top of the stack 
contains the matching opening brace or not, if this is the case then instead of pushing,
we just pop the top most element of the stack.

Since the stack is empty, we return true (No parenthesis errors were found)
********************************************************************************
Example 2 :
String : {}[]

First call :
Stack : |'{', 1| pushed '{' into the stack

Second call :
Stack : |Empty| popped '{' out of the stack because the matching closing brace was encountered

Third call :
Stack : |'[', 3| pushed '[' into the stack

Fourth call :
Stack : |Empty| popped '[' out of the stack because the matching closing brace was encountered

Since the stack is empty, we return true (No parenthesis errors were found)
********************************************************************************
Example 3 :
String : [()]

First call :
Stack : |'[', 1| pushed '[' into the stack

Second call :
Stack : |'(', 2| pushed '(' into the stack
        |'[', 1|

Third call :
Stack : |'[', 1| popped '(' out of the stack because the matching closing brace was encountered

Fourth call :
Stack : |Empty| popped '[' out of the stack because the matching closing brace was encountered

Since the stack is empty, we return true (No parenthesis errors were found)
********************************************************************************
Example 4 :
String : foo(bar[i);

First call :
Stack : |Empty| we will only push the parenthesis into the stack

Second call :
Stack : |Empty|

Third call :
Stack : |Empty| we will only push the parenthesis into the stack

Fourth call :
Stack : |'(', 4| pushed '(' into the stack

Fift call :
Stack : |'(', 4| we will only push the parenthesis into the stack

Sixth call :
Stack : |'(', 4| we will only push the parenthesis into the stack

Seventh call :
Stack : |'(', 4| we will only push the parenthesis into the stack

Eighth call :
Stack : |'[', 8| pushed '[' into the stack
        |'(', 4|

Ninth call :
Stack : |'[', 8| we will only push the parenthesis into the stack
        |'(', 4|

Tenth call :
Stack : |')', 10| The incoming element is : ')' which is not a matching brace 
Stack : |'[', 8| for our topmost element, hence we push element into the stack  
        |'(', 4| and break out of the loop, then we will simply return its index

Since the stack is not empty, we will check the topmost element of the stack, display its position and return false.
********************************************************************************
```

### **Future Idea: Take in multiple files to check at once**

<br>

Currently, the program is limited to a single file at a time. If we wanted to read multiple files we would have used a variable arguments method, so the user is not just limited to a single file, but the user can upload as many files as he/she wants. The updated algorithm will scan each file for errors and print the results. For files, our algorithm opens the files in read mode and then create a stack, and starts reading one character at a time from the input file until the EOF is encountered, and what it does is: it push uses the same string-based algorithm but on each character of the file, maintains the stack the same way, and print the results.


<br>

## **Web Application**

<br>

Our web application is built utilizing the Flask web framework. The homepage will contain two buttons for the option to pass different input types. One page will handle file input while the other will handle string input. Once input is received several python scripts are executed to read the input and determine the valdiity. The validity is ultimately displayed on the page with the filename or the input string.

<br>

Flowchart Diagram:

<br>

![flowDiagram](https://user-images.githubusercontent.com/69116925/142677966-73f80633-da5e-411a-8007-4d5a59e0a1c1.png)

<br>

## **Built with**
- Python
- Flask
- SQLAlchemly
- HTML
- CSS

## **Input Constraints**
- File: Must be less than 1MB
- String: Must be less than 1000 characters

## **Setting up virtual environment**
1. Open terminal or command prompt
2. run `pip install virtualenv`
3. Change directory to parenthesisCheck
4. run `py-3 -m venv <name of environment>` where <> is a name you choose
5. To activate on Mac OS / Linux run `source mypython/bin/activate`
6. To activate on Windows run `mypthon\Scripts\activate`
7. Virtual environment is now set up

## **Setting Up The Database Connection**

1. Open up terminal in working directory with virtual environment
2. run  `python`
3. run `from app import database`
4. run `database.create_all()`
5. Database has been establisted
6. run `exit()`

## **Running the application**
In Windows Terminal:
1. run `pip install Flask`
3. run `setx FLASK_APP "app.py"`
2. run `flask run`
