# flashcardio
CLI flashcard app that jogs your memory.
Spend more time learning from flashcards and less time making them.

## Installation

(Coming soon.)

## Usage

flashcardio [OPTIONS]

LIST 		Lists available CSV files in your data dir (FLASHCARDIO_DATA).

ADD
<FILENAME>	Add CSV to your data dir.

DELETE
<FILENAME>	Delete CSV from your data dir.

START session options:
filename		
--review-all	Disregards "active" field and puts all rows in circulation.
--swap			Swap column A and B (i.e. question and answer).

TODO:
- View full list of cards.
- Let SPACE key be a proxy for 'flip' and 'next'; e.g. '(F)lip/[SPACE]'. (see 'ncurses' or 'keyboard' package on PyPI)