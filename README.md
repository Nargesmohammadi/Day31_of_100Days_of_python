# Flash-Card-App-Capstone

This is a simple flash card application that helps users learn French words with the help of flash cards. The application is built using Python's Tkinter library for the GUI and Pandas for reading and writing to CSV files.

## Usage

    Run the program: python main.py

The application will display a French word with its English translation on the front of the flash card. After 3 seconds, the flash card will automatically flip to show the English translation on the back of the card. To indicate whether you know the word or not, click the green checkmark button or the red x button respectively. If you click the green checkmark, the word will be removed from the current deck and saved to the "words_to_learn.csv" file. If you click the red x button, the current card will be skipped and another random card will be displayed.

## GUI Components
## Canvas

This component displays the flash card with the French word and its English translation.

### Green Checkmark Button

Clicking this button indicates that you know the word currently displayed on the flash card. The word will be removed from the current deck and saved to the "words_to_learn.csv" file.

### Red X Button

Clicking this button indicates that you do not know the word currently displayed on the flash card. The current card will be skipped and another random card will be displayed.

### Data Files
french_words.csv

This CSV file contains a list of French words and their corresponding English translations.

### words_to_learn.csv

This CSV file is created upon running the application for the first time. It initially contains a copy of the "french_words.csv" file. As you go through the flash cards, words that you know will be removed from this file.

## Dependencies

    Tkinter
    Pandas

