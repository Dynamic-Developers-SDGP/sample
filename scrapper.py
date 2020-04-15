from src.InstagramScrapper import InstagramScrapper
from src.TwitterScrapper import TwitterScrapper

if __name__ == '__main__':
    print("Starting up Social Media Scrapper...")
    keyword = str(input("Enter your keyword to get search for: "))
    instagram_limit = int(input("Enter how many posts you need from Instagram: "))
    twitterApp_limit = int(input("Enter how many posts you need from Twitter: "))

    consumerKey = 'Y2x9rnSVirom9p4aP4j4GmWGy'
    consumerSecret = 'peCyxeqB68YvMrcdjXilHbzbWe3KXZKD4cE6NzHnjxTd2GCm9u'
    accessOfToken = '2186053585-zX6VlzWtTr9nNg72SXk9q0TWe6yV6VDyI0TCaxF'
    accessOfTokenSecret = 'T3NAV6vXeOzHXLwBRulUXyBxRQUP8cjdbepFkeFzQyMgh'

    scrapper = InstagramScrapper()
    scrapper.Scrape_Instagram(tag=keyword,
                              limit=instagram_limit,
                              browser='chrome')  # 'chrome' or 'firefox'

    twitter = TwitterScrapper()
    twitter.Scrape_Twitter(Consumer_Key=consumerKey,
                           Consumer_Secret=consumerSecret,
                           Access_Token=accessOfToken,
                           Access_Token_Secret=accessOfTokenSecret,
                           tag=keyword,
                           limit=twitterApp_limit,
                           lang='en')

    print("Stop Social Media Scrapping procedure...")
