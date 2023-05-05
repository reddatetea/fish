from selenium import  webdriver
from selenium.webdriver.common.keys import  Keys
import  time

def   spider(url,keywords):
    driver = webdriver.Chrome()
    driver.get(url)
    import_tag = driver.find_element_by_id('key')
    import_tag.send_keys(keywords)
    import_tag.send_keys (Keys.ENTER)
    driver.execute_script('document.documentElement.scrollTop=10000')
    get_goods(driver)
    time.sleep(5)
    #button = driver.find_element_by_partial_link_text('下一页')   #点击下一页
    #button.click()
    #get_goods(driver)

def     get_goods(driver) :
    goods  = driver.find_elements_by_class_name('gl-item')
    print(goods)
    for  good in goods :
        print(good)
        link = good.find_element_by_tag_name('a').get_attribute('href')
        name = good.find_element_by_css_selector('.p-name em').txt.replace('\n','')
        price = good.find_element_by_css_selector('.p-price i').txt
        commit = good.find_element_by_css_selector('.p-commit a').txt

        '''
        msg = 
                        商品%s
                        品名%s
                        价格%s
                        评论%s
                    
                  %(link,name,price,commit)
       '''
        print(link)
        print(name)
        print(price)
        print(commit)

if __name__ =='__main__' :
    url = 'https://www.jd.com/'
    keywords = '口红'

    spider(url,keywords)






