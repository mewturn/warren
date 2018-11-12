from bs4 import BeautifulSoup

with open('test.txt', 'r', encoding='utf-8') as file:
    with open('test_out.txt', 'w', encoding='utf-8') as output:
        for line in file:
            soup = BeautifulSoup(line)
            text = soup.get_text()
            output.write(text)