# **ParenthesisValidator**

## **Back to Hacking 2021 run by Major League Hacking**

November 19-21, 2021

## **Goal**

- Implement a web application that takes user input and returns the validity of having balanced parenthesis.
- Our App would be able to work for as many number of files as the user wants, in one go.
- Our App would check for the following parenthesis pairs : [], {}, and ()

### **Background**

Balanced parenthesis is a common programming problem that checks whether or not all open parenthesis have a closing parenthesis and are properly nested.
[GeeksforGeeks Balanced Parenthesis](https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/)

### **Algorithm**

The algorithm utilizes a stack data structure. This is a data structure that follows a First In Last Out principle. As we search through the input, upon every occurrence of an open parenthesis '(' we add it to the stack. When we encounter a closed parenthesis ')' we check that the top of the stack contains a '('. If so, we Pop it off the stack i.e remove it and continue. If we encounter another closed parenthesis ')' on the top of the stack we return False as the parenthesis are not nested properly. If we search the entire input and our stack is empty then we can return True.

<br>

Our Algorithm works in the following manner

<br>

```txt
******************************************************************************************************************
Example 1 :
String : []
Our Algo will implement the stack as :

First call :
Stack : |'['| pushed '[' into the stack

Second call :
Stack : |Empty| whenever we encounter any closing brace, we check if the top of the stack contains the matching opening brace or not, if this is the case then instead of pushing, we just pop the top most element of the stack.

Since the stack is empty, we return true (No parenthesis errors were found)
******************************************************************************************************************
Example 2 :
String : {}[]

First call :
Stack : |'{'| pushed '{' into the stack

Second call :
Stack : |Empty| popped '{' out of the stack because the matching closing brace was encountered

Third call :
Stack : |'['| pushed '[' into the stack

Fourth call :
Stack : |Empty| popped '[' out of the stack because the matching closing brace was encountered

Since the stack is empty, we return true (No parenthesis errors were found)
******************************************************************************************************************
Example 3 :
String : [()]

First call :
Stack : |'['| pushed '[' into the stack

Second call :
Stack : |'('| pushed '(' into the stack
        |'['|

Third call :
Stack : |'['| popped '(' out of the stack because the matching closing brace was encountered

Fourth call :
Stack : |Empty| popped '[' out of the stack because the matching closing brace was encountered

Since the stack is empty, we return true (No parenthesis errors were found)
******************************************************************************************************************
Example 4 :
String : foo(bar[i);

First call :
Stack : |Empty| we will only push the parenthesis into the stack

Second call :
Stack : |Empty|

Third call :
Stack : |Empty| we will only push the parenthesis into the stack

Fourth call :

```

## **Web Application**

Our web application is built utilizing the Flask web framework. The homepage will contain two options to pass different input types, either as a file of supported kind(See below) or as a string. Each option will direct you to another page where the process will take place. Upon completion, you will be redirected to the home page and prompted to repeat the process.

Flowchart Diagram:

![flowDiagram](https://user-images.githubusercontent.com/69116925/142677966-73f80633-da5e-411a-8007-4d5a59e0a1c1.png)


## **Four Flaskateers**

This is our first hackathon individually and as a group!  The three of us have different education backgrounds and come from different countries. The three of us have similar tech experience however but none of us have used Flask. 


## **Setting Up The Database Connection**

1. Open up terminal in working directory with virtual environment
2. run  `python`
3. run `from app import database`
4. run `database.create_all()`
5. Database has been establisted
6. run `exit()`
