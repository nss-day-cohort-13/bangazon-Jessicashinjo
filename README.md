# Birdyboard
## Command Line Message Board

In this app, users will create and read public and private messages via terminal input.

## Instructions

Create a series of prompts for a user interface that allows people to create an account and then create messages in a twitter/message board hybrid. You will be using serialization via pickle to store the users and the chirps to disk so that they persist between execution of the main application.

### Main Menu
```bash
#########################################
##           Birdyboard~~~~~           ##
#########################################
1. New User Account
2. Select User
3. Chirp
4. View Chirps
5. Exit
>
```


### New User
```bash
Enter full name
>

Enter screen name
>
```


### Select User
```bash
Which user is chirping?
1. Tweedleedee
2. BiffBoffin
...
>
```


### View Chirps

Display all chirps in a numbered list. Consider the use of `enumerate()`. Only display the first 20 characters of the chirp in this list. Consider the fact that the chirps must be displayed in the order in which they were created, so you will need an ordered collection.

The chirp message must be preceded by the screen name of the user who created it.

```bash
1. BiffBoffin: Hey, you up for ping...
2. Lara_keet: Any idea what Jeff wa...
3. BiffBoffin: Hah, you got wrecked...
...
9. Main Menu
>
```

Selecting an individual chirp takes you to that chirp's full text. If the user chose Chirp #1 from above, then the output would be as follows.

```bash
BiffBoffin: Hey, you up for ping pong later this afternoon? I'm feeling a bit rusty.

< Press enter to return to list of chirps >
```

### New Chirp

```bash
Enter chirp text
>
```

# Requirements

1. A full test suite with full coverage of all methods
2. User data will be serialized to a file (name of your choosing) and should contain the following information, at minimum:
  - A unique identifier
  - Screen name
  - Full name
3. Chirps will be serialized to a file (name of your choosing) and should contain the following information, at minimum
  - A unique identifier
  - Who authored the chirp
  - The text content of the chirp


# How to get started

1. Design first. Identify the objects involved in the application and decide what classes you will need.
1. The information is related to each other, so think about how you will connect the users and chirps together.
1. Write tests for creation of required objects, and verify their properties and behavior.
1. You can use `input()` and `print()` to show prompts and read user input.
1. You know how to use [`open()`, `readline()` and `write()`](https://docs.python.org/3.3/tutorial/inputoutput.html#reading-and-writing-files) to manipulate data in text files.
1. [Serialize](https://docs.python.org/3.3/library/pickle.html) the user and chirp data before storage & deserialize on read.

## UI Basics

> Define your classes and test their properties and behavior before writing UI code.

1. Show the main menu and read the user's choice with an `input()`.
1. Based on the user's choice, `print()` their choice, i.e. "You chose to make a new chirp."
1. Create the logic for each of the conditions to recieve further user input & display other menus.
1. Once all user input is received, perform the appropriate file action (reading from or writing to the chirps file), and direct the user back to the appropriate menu.
