import argparse
import csv
import glob
import os
import sys
import textwrap
from random import shuffle
from shutil import copy2, move
from tempfile import NamedTemporaryFile


try:
    DATA_DIR = os.environ['FLASHCARDIO_DATA']
except:
    print('Cannot find environment variable "FLASHCARDIO_DATA". Please point this environment variable at the directory that contains your flashcard CSV files.')
    print(sys.exit(1))


def load_csv(filename):
    with open(filename, newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        print(rows)

        for i in rows:
            print(i)
        return rows


def add_file(filepath):
    try:
        copy2(filepath, DATA_DIR)
        filename = os.path.basename(filepath)
        print(f'Added file {filename} to {DATA_DIR}.')
    except:
        print('Failed to add file.')


def delete_file(filename):
    try:
        os.remove(os.path.join(DATA_DIR, filename))
        print(f'Deleted file {filename} from {DATA_DIR}.')
    except:
        print('Failed to delete file.')


def list_files():
    print(f'Files in FLASHCARDIO_DATA ({DATA_DIR}):')
    files = glob.glob(os.path.join(DATA_DIR, '*.csv'))
    for f in sorted(files):
        print(' ', f.split('/')[-1])


def save_file_and_exit(header, rows, filename):
    '''
    Saves rows to temp file.
    '''
    rows = [header] + rows
    tempfile = NamedTemporaryFile(delete=False)

    with open(tempfile.name, 'w') as temp_csv:
        writer = csv.writer(temp_csv, delimiter=',', quotechar='"')
        writer.writerows(rows)
        
        # Delete the original file.     
        os.remove(os.path.join(DATA_DIR, filename))
        # Save temp file under the original name.
        move(tempfile.name, os.path.join(DATA_DIR, filename))

    print('\n\nAll done!')
    sys.exit(0)


def get_input(question: str, options: list) -> str:
    '''
    Present user with options; returns their response.
    '''
    while True:
        response = input(question)

        if response.lower() not in options:
            print('Invalid response.')

        else:
            return response.lower()


def start(filename, review_all=False, swap=False, keep_order=False):

    filepath = os.path.join(DATA_DIR, filename)

    with open(filepath, newline='') as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        rows = list(rows)
        header, rows_list = rows[0], rows[1:]

        # Check if we're only reviewing active rows.
        if not review_all:
            rows_list = [i for i in rows_list if i[-1] == '1']

        # Check if we're keeping the order (don't randomize).
        if not keep_order:
            shuffle(rows_list)

        # Assign vars for column indices.
        ques, ans, active_status = 0, 1, 2
        if swap:
            ques, ans, active_status = 1, 0, 2

        current = 1
        total = len(rows_list)

        # Initial question.
        for row in rows_list:
            print('\n============================================================')
            print(f' {current}/{total}\n\n')
            print('   Q:', textwrap.fill(row[ques], width=54, subsequent_indent='     '))
            print('\n')            

            if review_all:
                status_str = 'ACTIVE' if row[active_status] == '1' else 'DEACTIVATED'
                print(f'Status: {status_str}\n')

                if status_str == 'ACTIVE':
                    question_1 = '(F)lip, (N)ext, (D)eactivate, (Q)uit: '
                    options_1 = ['f', 'n', 'd', 'q']
                else:
                    question_1 = '(F)lip, (N)ext, (A)ctivate, (Q)uit: '
                    options_1 = ['f', 'n', 'a', 'q']

            else:
                question_1 = '(F)lip, (N)ext, (D)eactivate, (Q)uit: '
                options_1 = ['f', 'n', 'd', 'q']
            
            response_1 = get_input(question_1, options_1)

            if response_1 == 'f':
                print('~~~~~~~~~~~~~~~~~~~~\n\n')
                print('   A:', textwrap.fill(row[ans], width=54, subsequent_indent='     '))
                print('\n')
                question_2 = '(N)ext, (Q)uit: '
                options_2 = ['n', 'q']
                response_2 = get_input(question_2, options_2)

                if response_2 == 'n':
                    current += 1
                    continue

                elif response_2 == 'q':
                    save_file_and_exit(header, rows_list, filename)

            elif response_1 == 'n':
                current += 1
                continue

            elif response_1 == 'a':
                current += 1
                row[active_status] = '1'

            elif response_1 == 'd':
                current += 1
                row[active_status] = '0'

            elif response_1 == 'q':
                save_file_and_exit(header, rows_list, filename)

        # TODO: write the rows back to the csv file in case the user deactivated a row.
        save_file_and_exit(header, rows_list, filename)
