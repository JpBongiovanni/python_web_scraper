from selenium import webdriver
import os
import pandas as pd



url = "https://www.speedrun.com/smrpg"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")


browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
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