# **Foxycon**

This project is conceived as a universal platform for parsing statistical data from various subjects, as well as for the formation of automated search methods for the accumulation of this data in personal databases.

---

## **Supported Parameters**

### 🛠️ **Link Analysis**
1. YouTube Channels  
2. YouTube Shorts  
3. YouTube Videos  
4. Instagram Pages  
5. Instagram Reels  
6. Google Meet  

---

### 📊 **Statistics Collection**
1. YouTube Channels  
2. YouTube Shorts  
3. YouTube Videos  
4. Instagram Reels  

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
ca.get_data("https://www.instagram.com/blyea_u/")
ca.get_data("https://www.instagram.com/reel/C9NSNb5ow03/?igsh=a29uNGk0eTdta3Fw")

```



