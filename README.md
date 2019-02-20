# NYT Spelling Bee Word Generator

[Link to Spelling Bee](https://www.nytimes.com/puzzles/spelling-bee)

## Description

This is a simple Python script that
1. Prompts the user for the 7 letters in a Spelling Bee game,
2. Searches the Dwyl corpus of 479,000 English words for matches,
3. Prints the list of matching words, pangrams first.

## Data Sources

This solver uses the Dwyl corpus of >479,000 words as a reference, found on Github [here](https://github.com/dwyl/english-words).

An older version used the MIT 10K Wordlist, found [here](http://www.mit.edu/~ecprice/wordlist.10000).

## Potential Improvements

- This was coded before I learned functional programming; uses a potentially inefficient for loop. Will replace when I have time.
- The Spelling Bee uses a shorter, curated word list, preferring more common words. Will explore computational measures of how common a word is so that the solver can avoid printing words that are too obscure.
- Explore alternative forms of outputs other than printing to stdout. 
