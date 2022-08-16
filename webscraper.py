from selenium import webdriver
import os
import pandas as pd



url = "https://www.speedrun.com/smrpg"


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")


browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)
browser.get(url)

statistics = browser.find_element_by_xpath('//a[@href="/smrpg/gamestats"]')
statistics.click()

matches = browser.find_elements_by_class_name('row')



allText = []
splitText = []

statTitle = []
statValue = []

for match in matches:
    allText.append(match.text)


for text in allText:
    splitText.append(text.split("\n"))
    
sliceText = splitText[2:]   
# print(sliceText)

for index in sliceText:
    statTitle.append(index[0])
    statValue.append(index[1])
    
# print(statTitle)
# print(statValue)

df = pd.DataFrame({'Stat Title': statTitle, 'Stat Value': statValue})

# df.to_csv('speedrun_stats.csv', index=False')
df.to_json()



print(df)

browser.close()