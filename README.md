# **ParenthesisValidator**

<br>

## **Back to Hacking 2021 run by Major League Hacking**

<br>

November 19-21, 2021

<br>

## **Goal**

<br>

- Implement a web application that takes user input and returns the validity of having balanced parenthesis.
- Our App would be able to work for as many number of files as the user wants, in one go.
- Our App would check for the following parenthesis pairs : [], {}, and ()

<br>

### **Background**

<br>

Balanced parenthesis is a common programming problem that checks whether or not all open parenthesis have a closing parenthesis and are properly nested.
[GeeksforGeeks Balanced Parenthesis](https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/)

### **Algorithm**

<br>

The algorithm utilizes a stack data structure. This is a data structure that follows a First In Last Out principle. As we search through the input, upon every occurrence of an open parenthesis '(' we add it to the stack. When we encounter a closed parenthesis ')' we check that the top of the stack contains a '('. If so, we Pop it off the stack i.e remove it and continue. If we encounter another closed parenthesis ')' on the top of the stack we return False as the parenthesis are not nested properly. If we search the entire input and our stack is empty then we can return True.

<br>

Our Algorithm works in the following manner

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
Stack : |Empty| whenever we encounter any closing brace, we check if the top of the stack contains the matching
opening brace or not, if this is the case then instead of pushing, we just pop the top most element of the stack.

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
Stack : |')', 10| The incoming element is : ')' which is not a matching brace for our topmost element, hence we push s
Stack : |'[', 8| element into the stack and break out of the loop, then we will simply return its index 
        |'(', 4| 

Since the stack is not empty, we will check the topmost element of the stack, display its position and return false.
********************************************************************************
```

### **For Files**

<br>

We have used varibale arguements method, so the user is not just limited to a single file, but user can upload as many files as he/she wants, our algorithm will scan each file for errors and print the results. For files our algo opens the files in read mode and then create a stack, and starts reading one character at a time from the input file until the EOF is encountered, and what is does is : it push uses the same string based algo but on each character of the file, maintains the stack the same way, and print the results.

<br>

## **Web Application**

<br>

Our web application is built utilizing the Flask web framework. The homepage will contain two options to pass different input types, either as a file of supported kind(See below) or as a string. Each option will direct you to another page where the process will take place. Upon completion, you will be redirected to the home page and prompted to repeat the process.

<br>

Flowchart Diagram:

<br>

![flowDiagram](https://user-images.githubusercontent.com/69116925/142677966-73f80633-da5e-411a-8007-4d5a59e0a1c1.png)

<br>

## **Four Flaskateers**

<br>

This is our first hackathon individually and as a group!  The three of us have different education backgrounds and come from different countries. The three of us have similar tech experience however but none of us have used Flask. 

<br>

## **Setting Up The Database Connection**

1. Open up terminal in working directory with virtual environment
2. run  `python`
3. run `from app import database`
4. run `database.create_all()`
5. Database has been establisted
6. run `exit()`
