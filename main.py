from secretsharing import PlaintextToHexSecretSharer
import pyqrcode
import png

def main():
    # Secret-share the message using Shamir's secret sharing scheme.
    shares = PlaintextToHexSecretSharer.split_secret("correct horse battery staple", 2, 3)
    print(shares)
    for share in shares: # Create png for each share
        img = pyqrcode.create(share)
        img.png(share[0]+'.png', scale = 8)

    # Recover
    # print(PlaintextToHexSecretSharer.recover_secret(shares[0:2]))

if __name__ == "__main__":
	main()