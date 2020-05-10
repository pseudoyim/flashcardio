# flashcardio
A CLI flashcard app that jogs your memory.

## Installation

(Coming soon.)

## Usage
```
usage: flashcardio

A CLI flashcard app that jogs your memory.

positional arguments:
  {add,delete,list,start}

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
```

### `add`
```
usage: flashcardio add [-h] filepath

Add a file to your data dir ($FLASHCARDIO_DATA).

positional arguments:
  filepath    Path to file to add to data dir ($FLASHCARDIO_DATA).

optional arguments:
  -h, --help  show this help message and exit
```

### `delete`
```
usage: flashcardio delete [-h] filename

Delete a file from your data dir ($FLASHCARDIO_DATA).

positional arguments:
  filename    Filename to delete from data dir ($FLASHCARDIO_DATA).

optional arguments:
  -h, --help  show this help message and exit
```

### `list`
```
usage: flashcardio list [-h]

List all files in data dir ($FLASHCARDIO_DATA).

optional arguments:
  -h, --help  show this help message and exit
```

### `start`
```
usage: flashcardio start [-h] [--review-all] [--swap] filename

Add a file to your data dir ($FLASHCARDIO_DATA).

positional arguments:
  filename      Filename to review.

optional arguments:
  -h, --help    show this help message and exit
  --review-all  Review all rows, regardless of their "active" status.
  --swap        Swap column A and B (i.e. question and answer).
```