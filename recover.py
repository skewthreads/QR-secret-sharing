from pyseltongue import PlaintextToHexSecretSharer
import inquirer
import animation

def main():
    # Enter shares
    shares = [input('Enter your share: ')]
    while True:
        questions = [
            inquirer.List('share',
                        message='Enter next share',
                        choices=['OK', 'I don\'t have another one'],
                    ),
        ]
        answer = inquirer.prompt(questions)['share']
        if answer != 'OK':
            break
        shares.append(input('Enter your share: '))

    # Recover
    wait = animation.Wait('spinner', 'Generating randomness.. It may take a while.. ')
    wait.start()
    message = PlaintextToHexSecretSharer.recover_secret(shares)
    wait.stop()
    print('Original message:\n'+message)

if __name__ == '__main__':
	main()
