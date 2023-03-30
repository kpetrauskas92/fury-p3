
# FURY
![Icon](assets/favicon/android-chrome-192x192.png)
## **Game Overview**

"FURY" tank battle game is a single player board game where the player's goal is to destroy all enemy tanks on the board within a limited number of turns. The player must choose a difficulty level (easy, medium, or hard) before starting the game. The game is played by guessing a row (letter) and column (number) on the enemy board to target a tank.

---
​
![Game Screen](assets/images/readme/game_screen.png)

#### [The deployed website is here on Heroku](https://fury-p3.herokuapp.com)​

## Table of contents:
1. [**Game Overview**](#game-overview)
1. [**Planning stage**](#planning-stage)
    * [***Planning Overview***](#planning-overview)
    * [***User Stories***](#user-stories)
    * [***Game Aims***](#game-aims)
    * [***Wireframes***](#wireframes)
    * [***Logic Flow***](#wireframes)
    * [***Color Scheme***](#color-scheme)
    * [***Design Choices***](#design-choices)
1. [**Game Features**](#game-features)
    * [***FEATURE1***](#feature1)
    * [***FEATURE2***](#feature2)
    * [***FEATURE3***](#feature3)
    * [***FEATURE4***](#feature4)
    * [***FEATURE5***](#feature5)
    * [***FEATURE6***](#feature6)
    * [***FEATURE7***](#feature7)
    * [***FEATURE8***](#feature8)
    * [***FEATURE9***](#feature9)
1. [**Testing**](#testing)
1. [**Deployment**](#deployment)
1. [**Technology and Applications**](#technology-and-applications)
1. [**Future-Enhancements**](#future-enhancements)
    * [***User Enhancements***](#user_enhacements)
    * [***Internal Enhancements***](#internal_enhacements)
1. [**Credits**](#credits)
    * [**Honorable mentions**](#honorable-mentions)
    * [**Content**](#content)
    * [**Media**](#media)

---


## **Planning Stage**

### **Planning Overview:**

The initial concept of the game was a Battleship-style game, where the player guesses the location of the enemy's ships. However, during the development, the concept was switched to a tank board game where the player tries to destroy the enemy tanks on a grid.

"FURY" was chosen from one of your favorite movies, which represents the theme of the game well.

  Core aims for the project:

* Maximize visual elements while utilizing a text-based terminal
* Deliver a seamless user experience
* Implement login and registration features
* Integrate a leaderboard feature for top players
* Establish a scoring system that takes difficulty levels into account
* Update scores according to player registration status
* Position tanks randomly on each game board
* Offer an enjoyable challenge with rewards


### **Target Audiences:**

* Python programmers interested in game logic
* Fans of the movie Fury and military-themed entertainment
* Casual players seeking strategic games for enjoyable pastime
* Competitive individuals striving to surpass high scores
* Individuals interested in honing their tactical skills in a single-player setting

### **User Stories:**

* As a player, I want a game featuring well-defined goals
* As a player, I want inputs that are easy to use and provide quick responses
* As a player, I want entertaining and engaging gameplay experience
* As a player, I want clear instructions on how to play the game
* As a player, I want to view my score and see the results of my gameplay


### **Game Aims:**

* The game should feature clear rules to help players navigate through the gameplay
* The game should offer a main menu and user menu for easy navigation and user control
* The game should be straightforward and easy to grasp for new players
* The game should feature a specified turn limit to add structure and strategy to the gameplay
* The game should automatically update the scores of registered players
* The game should give players informative and precise feedback to enhance the gaming experience.

---

### **Wireframes:**

The wireframes for the website were produced in [Balsamiq](https://balsamiq.com). The frames shown below are menus and game play on left and right side. The final site might be slightly different from the wireframes due to developments that occured during the creation process. 

![Wireframe 1](assets/images/readme/wireframe.png)

---

### **Logic Flow:**

I created a high-level logic flowchart in [Draw.io](https://draw.io)


![logic Flow](assets/images/readme/logic_flow.png)

---
​
### **Color Scheme:**

The limited color availability in the Python terminal I was working with had an impact on my decision-making process. However, I was fortunate enough to be able to choose the main colors required for the game despite this limitation.
I used colorama library with color constants to achieve the desired color scheme.

-  $\colorbox{green}{{\color{black}{GREEN}}}$ : Was utilized for the Fury Logo as well as some event messages in the game.

- $\colorbox{yellow}{{\color{black}{YELLOW}}}$ : was primarily used for displaying informational pieces such as rules and certain event messages in the game.

- $\colorbox{red}{{\color{black}{RED}}}$ : was utilized for displaying error messages or certain important information in the game.

- $\colorbox{magenta}{{\color{black}{MAGENTA}}}$ : was used to differentiate menu headings from other elements, providing a unique and distinct style.

- $\colorbox{cyan}{{\color{black}{CYAN}}}$ : was assigned to list numbers for choices and the terminal prompt cursor.

- $\colorbox{black}{{\color{white}{BRIGHT/BOLD}}}$ : Was applied to make the colors in the game more vibrant and visible.

- $\colorbox{gray}{{\color{white}{DIM}}}$ : was utilized for the inner section of the board in order to provide a contrast and ensure that events within this section were easily visible.


### **Design Choices**
​
When designing "FURY", I prioritized a clean and minimalistic user interface that would allow players to focus on the gameplay without distraction.

---
​
## **Main Features**

### ***INTRO LOGO***

I utilized ASCII art to create the FURY text for the logo and incorporated a pre-existing tank ASCII design to emphasize the theme of a tank warfare game.

- Incorporated introductory text to provide a glimpse into the game's theme and content.
- Included a "Ready to play" prompt, allowing users to decide whether they want to proceed with playing the game.
- Should the user opt not to continue, they will be presented with a "shutting down" message, along with instructions on how to restart the game.

<button><details><summary>Example Image</summary>
<img src="assets/images/readme/intro_logo.png">
</details></button>

---

### ***LOADING SCREEN***

Upon the user's decision to continue, the loading screen features a simplified version of the logo, enhancing the overall user experience.

- Sequential loading event messages are presented with a typewriter-style animation for added visual appeal.
- While the "game loaded" message is being prepared for display, the fury_data API is loaded silently in the background.
- Once the game has successfully loaded, the "Game loaded successfully" text appears and the screen is cleared to present the main menu.


<button><details><summary>Example Image</summary>
<img src="assets/images/readme/loading_screen.png">
</details></button>

---

### ***MAIN MENU***

The FURY menu is presented without a logo to enhance user experience, particularly when an error message for an invalid option is displayed. Headings are distinguished with a magenta color to stand out and create visual separation.

<button><details><summary>Main Menu Example</summary>
<img src="assets/images/readme/main_menu.png">
</details></button>

### Option 1. Play Game
- Allows users to play without the requirement of logging in or registering an account.
- Before presenting the difficulty selection screen, a prompt is displayed asking users if they would like to view the game rules.

<button><details><summary>Example</summary>
<img src="assets/images/readme/see_rules.png">
</details></button>

### Option 2. Login
- The user is directed to a login screen where they can input their credentials to resume their progress within the game.
- The fury_data API checks for existing data in the Google Sheets high score sheet. If the user is matched, they will be directed to the user-menu; otherwise, they will be returned to the main-menu with an error message displayed.

<button><details><summary>Example 1</summary>
<img src="assets/images/readme/login.png">
</details></button>

<button><details><summary>Example 2</summary>
<img src="assets/images/readme/main_menu.png">
</details></button>

---
### ***USER MENU***


---
### **FEATURE 4**


---
### **FEATURE 5**


---
### **FEATURE 6**


---
### **FEATURE 7**


---
### **FEATURE 8**


---
### **FEATURE 9**


### **Performance Summary**

SUMMARY TEXT

- text
- text
- text
- text
- text
- text
- text
- text

![logo](IMG)

---
## **Testing**

Testing documentation is [here](./TESTING.md)

## **Deployment**

- 
- 
- 
- 
-  

### **GitHub** 
  

---
​
## **Technology and Applications**
​
These are the technologies used for this project.

- Python 3.8.11
- Gitpod
- Github
- Heroku

----

## **Future-Enhancements**


### **User Enhancements**

* 
* 
* 

### **Internal Enhancements**

* 
* 
* 

## **Credits**
### **Honorable mentions**
​

​
### **Content:**
​
  
### **Media:**
​
* 