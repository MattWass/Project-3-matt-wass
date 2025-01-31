# Battleships

Battleships is a Python terminal game that runs in the Code Institute mock terminal on Heroku.

Players can attempt to sink all the computer's battleships and reign victorious over the seas. However if the computer sinks all the players battleships first it is game over.

Welcome to [https://project-3-matt-wass-9b18f1b1e57e.herokuapp.com/]

![alt text](image-2.png)

## Game Instructions

Battleships is an all time classic game, with various different iterations over the years.

This version starts with the player entering their name.

After the player has entered their name, they will be prompted to select four positions on the board. It has been noted in the introduction that the top left corner is row 0 column 0, to aid the player in the selection of their positions.

The player's ships will be marked with the '@' sign. The computer's battleships will not be visible to the player.

Any guesses are marked on the board with the 'X' sign. While any direct hits are indicated by the '*' sign.

The player and computer will take it in turns to attempt to sink all the battleships on the opposing side.

The winner is the defined by having sunk all the enemy ships.

## Features 

### Board Generation

The player may select their board positions as seen below

![alt text](image-3.png)


Once the first position has been selected, the player will then be prompted to select their remaining board posistions.

![alt text](image-4.png)


Now all the positions have been selected, we can see the game is ready to begin and the enter X and Y coordinates are ready to be guessed.

![alt text](image-5.png)


in the image below both sides missed 

![alt text](image-7.png)


in the image below the computer has hit 

![alt text](image-8.png)


The image below shows that you cannot enter the same coordinates twice and that you cannot enter invlaid coordinates that are outisde of the board sizing.

![alt text](image-9.png)


## Future Features

  - Have battleship sizing larger than 1x1
  - Increase board size and also number of ships on the board

## Testing

 - I have tested the project through the CI python linter, as seen below and the project came back all clear, with no errors found.
  - I have also tested the project in my local terminal as well as the Code Institute Heroku terminal

  ![alt text](image-1.png)

  - The project has been retested through the CI python linter before resubmission. This gave a result of all clear with no errors found as seen below.

  ![alt text](image-13.png)

  - The relevant testing and code has been added so that exception handling for empty or invalid values now displays appropriately, no longer crashing the app. Please see the image below.

  ![alt text](image-15.png)

  - Upon testing the game manually I managed to play the game in its entirety, coming to the conclusion of "player wins" as seen below.

  ![alt text](image-10.png)

  - After further update and troubleshooting of my project, additional testing has been done to receive the "play again? (y/n):" message as seen below. This addition is a much more user friendly way of restarting the game.

  ![alt text](image-11.png)

  Upon selecting "y" to restart the game, we can see that the game has gone back to the enter name section, ready for another game of battleships.

  ![alt text](image-12.png)

  - With further manual testing of my project, I reached a battleships conclusion of computer wins as seen below.

  ![alt text](image-14.png)

### Bugs

Solved Bugs

 - I had various issues getting the code to pass through the linter at first due  to blankspaces been present in my code. I solved this through the guidance displayed on the CI python linter.
 - My populate_board function was not displaying properly and kept appearing faulty due to me missing a ',' instead of a '.' in my code. Such a small error took me much longer than anticpated to notice.

 ### Remaing Bugs
  - There are now no remaining bugs

  ## Deployment 
  
  My project was deployed using Code Institutes mock terminal for Heroku.

    - Steps taken for deplyment:
      - Cloned repository
      - Created a Heroku app
      - Set releavant buildpacks Python and NodeJS in correct order
      - Linked Heroku app to repository
      - Clicked on Deploy

## Acknowledgements
- Code Institute for the deployment terminal
- Student Care, for all their support and guidance over what has been a very challenging time.
- My family for their unwavering support 
- I would like to thank Roman from the Tutoring team for advising me on the steps I needed to take for this resubmit. Helping me go through the finishing touches, Roman's guidance has been very much appreciated.

### Content

- Inspiration for my project was taken from the Love Sandwiches project as well as the ULTIMATE Battleships Project.