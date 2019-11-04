import pyperclip
from datetime import datetime


def main():
    now = datetime.strftime(datetime.now(), "%Y-%b-%d-%I%M%p")
    new_cboard = None
    current_clipboard_contents = ''

    with open('clipboard.txt', 'a', newline='') as f:
        f.write(f'\nCopy history initiated at {now}\n')
    while pyperclip.paste() != 'exit'.lower():
        if new_cboard != current_clipboard_contents:
            current_clipboard_contents = pyperclip.paste()
            new_cboard = pyperclip.paste()
            with open('clipboard.txt', 'a', newline='') as f:
                f.write(f'{current_clipboard_contents}\n\n')
        else:
            new_cboard = pyperclip.paste()


main()

if __name__ == '__main__':
    main()