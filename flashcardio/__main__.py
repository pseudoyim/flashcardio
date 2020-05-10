import argparse
import glob
import os
import sys
from .cardio import add_file, delete_file, list_files, start


DATA_DIR = os.environ['FLASHCARDIO_DATA']
# DATA_DIR = '/Users/PaulYim/Desktop/'
filenames = glob.glob(f'{DATA_DIR}/*.csv')


def main():
    p = argparse.ArgumentParser(
            description='A CLI flashcard app that jogs your memory.',
            usage='flashcardio'
            )
    p.add_argument(
            '-v', '--version',
            action='version',
            version='flashcardio 0.1.0'
            )

    subparsers = p.add_subparsers(dest='subcommand')

    # Subcommand: add
    desc_add = 'Add a file to your data dir ($FLASHCARDIO_DATA).'
    sub_add = subparsers.add_parser('add', description=desc_add)
    sub_add.add_argument(
        'filepath',
        help='Path to file to add to data dir ($FLASHCARDIO_DATA).')

    # Subcommand: delete
    desc_delete = 'Delete a file from your data dir ($FLASHCARDIO_DATA).'
    sub_delete = subparsers.add_parser('delete', description=desc_delete)
    sub_delete.add_argument(
        'filename',
        help='Filename to delete from data dir ($FLASHCARDIO_DATA).')

    # Subcommand: list
    desc_list = 'List all files in data dir ($FLASHCARDIO_DATA).'
    sub_list = subparsers.add_parser('list', description=desc_list)

    # Subcommand: start
    desc_start = 'Add a file to your data dir ($FLASHCARDIO_DATA).'
    sub_start = subparsers.add_parser('start', description=desc_start)
    sub_start.add_argument(
        'filename',
        help='Filename to review.')
    sub_start.add_argument(
        '--review-all',
        action='store_true',
        help='Review all rows, regardless of  their "active" status.')
    sub_start.add_argument(
        '--swap',
        help=f'Swap column A and B (i.e. question and answer).',
        action='store_true')

    args = p.parse_args()
    
    # SUBCOMMANDS
    if args.subcommand == 'add':
        add_file(filepath=args.filepath)

    elif args.subcommand == 'delete':
        delete_file(filename=args.filename)

    elif args.subcommand == 'list':
        list_files()

    elif args.subcommand == 'start':
        start(filename=args.filename,
              review_all=args.review_all,
              swap=args.swap)
    else:
        print('Error: Subcommand not recognized.')
        sys.exit(0)


if __name__ == '__main__':
    main()