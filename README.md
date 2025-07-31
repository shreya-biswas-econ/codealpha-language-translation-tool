# 🌐 Language Translation Tool

A simple web translation tool using Flask, JavaScript, and the MyMemory API. No API key needed. Built for learning and demo purposes.

> ✅ No authentication required  
> ✅ Built with Flask and JavaScript  
> ✅ Fully open-source and deployable

---

## 🚀 Features

- Translate text between over 20 languages
- Clean, responsive user interface
- Dropdowns for selecting source and target language
- Fast translations using MyMemory public API
- Easy to run locally (no API key or cloud setup needed)

---

## 🧱 Tech Stack

| Layer     | Technology            |
|-----------|------------------------|
| Backend   | Python (Flask)         |
| Frontend  | HTML, CSS, JavaScript  |
| API       | MyMemory Translation API |
| Optional  | Replit / Render for deployment |

---


## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shreya-biswas-econ/codealpha-language-translation-tool.git
cd language-translation-tool
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies

```bash
pip install -r requirements.txt
```
### 4. Run the flask app

```bash
python app.py
```
Open your browser and go to: http://127.0.0.1:5000

---

## 🌍 Supported Languages

You can use any language pairs supported by MyMemory.

Common examples:

- `en ↔ es` (English ↔ Spanish)
- `en ↔ fr` (English ↔ French)
- `en ↔ hi` (English ↔ Hindi)
- `en ↔ bn` (English ↔ Bengali)

---

## ✨ Future Improvements

- Add language auto-detection
- Add text-to-speech support
- Deploy online using Replit or Render
- Show language names instead of codes in the UI

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute.

---

## 🙌 Acknowledgments

- [MyMemory Translation API](https://mymemory.translated.net/)
- [Flask Web Framework](https://flask.palletsprojects.com/)
