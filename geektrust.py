import sys
from kingdom import King

def main():
    input_file = sys.argv[1]
    with open(input_file) as secret_message:
        secret_message_list = secret_message.readlines()

    Shan = King("SPACE", secret_message_list)
    support = Shan.analyze_support()
    print(support)

if __name__ == "__main__":
    main()