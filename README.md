# 📚 Scrape Wikipedia with Python

This project demonstrates how to scrape useful information from Wikipedia using Python. It uses the `wikipedia` library to extract article summaries, full content, images, references, and multilingual data.

---

## 🧠 What This Project Does
- Searches Wikipedia articles
- Suggests correct article names
- Fetches summaries in different languages
- Extracts full article content
- Retrieves images and references from Wikipedia

---

## 🛠️ Technologies Used
- Python 3
- wikipedia (Python package)

---

## 🚀 How to Run the Project
python main.py

---

## 🔍 Search Wikipedia
wiki.search("Python")
Returns all related article titles.

---

## ✨ Suggest Correct Keywords
wiki.suggest("Pyth")
Suggests correct article names.

---

## 📄 Get Article Summary
wiki.summary("Python")

---

## 🌍 Multilingual Support
wiki.set_lang("fr")
wiki.summary("Python")

---

## 📘 Full Article Scraping
- page = wiki.page("Python")
- page.title
- page.url
- page.content
- page.images
- page.links

---

## ♻️ Reusability
- Can be reused for any Wikipedia topic
- Easy to integrate into data analysis & NLP projects
- Useful for educational and research purposes

---

## 🤝 Contribution
Contributions are welcome!
- Fork the repository
- Create a new branch
- Commit your changes
- Open a Pull Request

---

## 🆘 Support
- If you face issues:
- Open a GitHub Issue
- Check official Wikipedia API documentation
- Ensure stable internet connection
