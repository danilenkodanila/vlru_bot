import schedule
import time
import user

# def job():
#     print("I'm working...")
#     return

# schedule.every().day.at("21:12").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(60) # wait one minute

for element in user.listLink:
		soup = BeautifulSoup(urlopen(element.replace("\n","").replace("\t","").replace("\t","")))
		data = soup.find_all("div", class_="story__info-comments-count")
		for div in data:
			links = div.findAll('a')
			for a in links:
				link.append("http://www.newsvl.ru" + a['href'])
				print(a['href'])

