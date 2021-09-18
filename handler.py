import requests

def main(event, context):

    x = requests.get('https://w3schools.com/python/demopage.htm')
    print(x.text)


if __name__ == "__main__":
    main('', '')
