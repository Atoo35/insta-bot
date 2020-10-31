from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait 

chromedriver_path = 'C:\\Users\\Atharva\\Desktop\\Insta Bot\\chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('YOUR ID')
password = webdriver.find_element_by_name('password')
password.send_keys('YOUR PASSWORD')

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(3)

# notnow = webdriver.find_element_by_css_selector('body > div:nth-child(3) > div > div > div:nth-child(3) > button:nth-child(2)')
# notnow.click() #comment these last 2 lines out, if you don't get a pop up asking about notifications



webdriver.find_elements_by_xpath("//button[contains(text(), 'Not Now')]")[0].click()

hashtag_list = ['amazingearth','longexposure','nightshot','nightpics','milkyway','milkywaygalaxy'
				,'wonderfulearth','bluesky','photography','mobilephotography','sunset','beach','clouds','nature']

# prev_user_list = [] 
# - if it's the first time you run it, use this line and comment the two below
prev_user_list = pd.read_csv('users_followed_list.csv', delimiter=',').iloc[:,1:2] # useful to build a user log
prev_user_list = list(prev_user_list['0'])

new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(5)
    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    
    first_thumbnail.click()
    sleep(randint(1,2))    

    try:        
        for x in range(1,10):
            username = webdriver.find_element_by_xpath("//a[@class='FPmhX notranslate nJAzx']").text
            print(username)
            if username not in prev_user_list:
                # If we already follow, do not unfollow
                
                if webdriver.find_element_by_xpath("//button[@class='sqdOP  L3NKy _4pI4F  y3zKF     ']").text == 'Follow':
                    
                    webdriver.find_element_by_xpath("//button[@class='oW_lN sqdOP yWX7d    y3zKF     ']").click()
                    
                    new_followed.append(username)
                    followed += 1

                    # Liking the picture
                    button_like = webdriver.find_element_by_xpath("//button[@class='dCJp8 afkep']")
                    
                    button_like.click()
                    likes += 1
                    sleep(randint(18,25))

                    # Comments and tracker
                    comm_prob = randint(1,10)
                    print('{}_{}: {}'.format(hashtag, x,comm_prob))
                    if comm_prob > 5:
                        comments += 1
                        webdriver.find_element_by_xpath("//span[@class='glyphsSpriteComment__outline__24__grey_9 u-__7']").click()
                        comment_box = webdriver.find_element_by_xpath("//textarea[@class='Ypffh']")

                        if (comm_prob < 7):
                            comment_box.send_keys('Really cool! Do follow @atharva_35')
                            print("commented on: ",username)
                            # sleep(1)
                        elif (comm_prob >= 6) and (comm_prob < 9):
                            comment_box.send_keys('Nice work :) Do follow @atharva_35')
                            print("commented on: ",username)
                            # sleep(1)
                        elif comm_prob == 9:
                            comment_box.send_keys('Nice gallery!! Do follow @atharva_35')
                            print("commented on: ",username)
                            # sleep(1)
                        elif comm_prob == 10:
                            comment_box.send_keys('So cool! :) Do follow @atharva_35')
                            print("commented on: ",username)
                            # sleep(1)
                        # Enter to post comment
                        # webdriver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']").click()
                        # comment_box.send_keys(Keys.ENTER)
                        comment_box.submit()
                        sleep(randint(22,28))

                # Next picture
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(25,29))
            else:
                webdriver.find_element_by_link_text('Next').click()
                sleep(randint(20,26))
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        continue

for n in range(0,len(new_followed)):
    prev_user_list.append(new_followed[n])
    
updated_user_df = pd.DataFrame(prev_user_list)
updated_user_df.to_csv('users_followed_list.csv')
print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))
