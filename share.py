from secretsharing import PlaintextToHexSecretSharer
import pyqrcode
import png
import inquirer

def main():
    # Select number of shares
    questions = [
        inquirer.List('parties',
                    message='How many shares do you want?',
                    choices=['2', '3', '4', 'other'],
                ),
    ]
    answer = inquirer.prompt(questions)
    if answer['parties'] == 'other':
        parties = int(raw_input('Type a number: '))
        while parties < 2:
            parties = int(raw_input('Type a number greater than 1: '))
    else:
        parties = int(answer['parties'])
    threshold = parties

    # Select type of shares output
    questions = [
        inquirer.List('format',
                    message='Select the format of output images',
                    choices=['png', 'svg', 'terminal'],
                ),
    ]
    format = inquirer.prompt(questions)['format']

    # Select size of shares output
    if format != 'terminal':
        questions = [
            inquirer.List('scale',
                        message='Size of output images',
                        choices=['Small', 'Medium', 'Large'],
                    ),
        ]
        answers = inquirer.prompt(questions)
        if answers['scale'] == 'Small':
            scale = 2
        elif answers['scale'] == 'Medium':
            scale = 4
        elif answers['scale'] == 'Large':
            scale = 8

    secret = raw_input('Enter your message: ')

    # Secret-share the message using Shamir's secret sharing scheme.
    shares = PlaintextToHexSecretSharer.split_secret(secret, threshold, parties)
    print(shares)
    for share in shares: # Create png for each share
        img = pyqrcode.create(share)
        if format == 'png':
            img.png(share[0]+'.png', scale = scale)
        elif format == 'svg':
            img.svg(share[0]+'.svg', scale = scale)
        elif format == 'terminal':
            print(img.terminal())


if __name__ == '__main__':
	main()
