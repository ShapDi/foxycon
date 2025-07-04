# **Foxycon**

This is a python library that aims to create a universal tool for analyzing statistical data from various social media objects and creating algorithms for searching and accumulating these objectsThis is a python library that aims to create a universal tool for analyzing statistical data from various social media objects and creating algorithms for searching and accumulating these objects
---

## **Supported Parameters**

### 🛠️ **Link Analysis**
1. YouTube Channels  
2. YouTube Shorts  
3. YouTube Videos  
4. Instagram Pages (Temporarily unsupported)
5. Instagram Reels (Temporarily unsupported)
6. Telegram Post (Public channels only)
7. Telegram Channels (Public channels only)


---

### 📊 **Statistics Collection**
1. YouTube Channels  
2. YouTube Shorts  
3. YouTube Videos  
4. Instagram Reels (Temporarily unsupported)
5. Telegram Post (Public channels only)
6. Telegram Channels (Public channels only)

---

### 🔍 **Search**
1. YouTube Videos  
*(Note: Additional details or examples can be added here)*

---

## Usage example

### analytics module

```python
from foxycon.analysis_services.сontent_analyzer import ContentAnalyzer

ca = ContentAnalyzer()


ca.get_data("https://youtu.be/dMPPMmUrYQM?si=_uGQVE6wtTXnVULv&t=32")
ca.get_data("https://youtu.be/GhXMLM7vUJI2")
```



