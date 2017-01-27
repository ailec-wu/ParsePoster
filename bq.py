from bs4 import BeautifulSoup
import requests

def get_quote():
	response = requests.get("https://www.brainyquote.com/")
	page = BeautifulSoup(response.content, "html.parser")
	table = page.find("div", {"data-sai-includehighlight":"true"})
	return list(s.strip() for s in table.strings if s!='\n')

