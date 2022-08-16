from selenium import webdriver
import pandas as pd



url = "https://www.speedrun.com/smrpg"


browser = webdriver.Chrome("chromedriver")
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