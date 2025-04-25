# **foxycon**

foxycon - This is a python library that aims to create a universal tool for analyzing statistical data from various social media objects and creating algorithms for searching and accumulating these objects

## **Basic usage**

## Using StatisticianSocNet

StatisticianSocNet class that is a universal way to collect data from social platforms

### StatisticianSocNet supports
* YouTube Channels  
* YouTube Shorts  
* YouTube Videos  
* Instagram Reels  

## Using ContentAnalyzer

ContentAnalyzer is a class that represents a universal way to classify links social platforms

### ContentAnalyzer supports
* YouTube Channels  
* YouTube Shorts  
* YouTube Videos  
* Instagram Pages  
* Instagram Reels  
* Telegram Post 
* Telegram Chat

```python
from foxycon import ContentAnalyzer

ca = ContentAnalyzer()

ca.get_data("https://www.youtube.com/watch?v=6fty5yB7bFo")
```
### **output**

```python

ResultAnalytics(url='https://youtube.com/watch?v=6fty5yB7bFo', 
                social_network='youtube', 
                content_type='video', 
                code='6fty5yB7bFo')

```
