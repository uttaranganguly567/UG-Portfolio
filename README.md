# Uttaran Ganguly's Portfolio Website

A modern, dark-themed portfolio website built with **Streamlit**. Clean design, easy navigation, and fully customizable.

## 📁 Project Structure

```
Student/
├── app.py                 # Main application file (entry point)
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── portfolio_pages/
   ├── __init__.py       # Pages module
   ├── home.py           # Home page
   ├── projects.py       # Projects page
   ├── skills.py         # Skills page
   └── contact.py        # Contact page
```

## 🎨 Features

- **Dark Theme**: Clean, modern dark interface with cyan accents
- **Responsive Layout**: Works seamlessly on desktop and mobile
- **Sidebar Navigation**: Easy page switching
- **Modular Structure**: Each page is a separate module for easy maintenance
- **Modern Typography**: Professional fonts with smooth spacing
- **Interactive Elements**: Hover effects on cards and smooth transitions

## 📄 Pages

### 🏠 Home
- Welcome message with introduction
- Educational background
- Quick overview of what you do

### 🚀 Projects
- **Campus Core**: Campus management system
- **GoldFilmDB**: Movie database with microservices architecture
- Links to live projects

### 🛠️ Skills
- **Programming Languages**: Java, Python, C
- **Databases**: SQL
- **Data Science & ML**: Numpy, Pandas, Scikit Learn
- Grid layout for easy scanning

### 📬 Contact
- Email contact: uttaranganguly20@gmail.com
- GitHub: https://github.com/uttaranganguly567
- LinkedIn: https://www.linkedin.com/in/uttaran-ganguly/
- Contact form for direct messages

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Navigate to the project directory:**
   ```bash
   cd "project\directory\path"
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   ```
   
   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **The app will open in your default browser at:**
   ```
   http://localhost:8501
   ```

3. **To stop the server:** Press `Ctrl+C` in the terminal

### Enable Direct Message Email Delivery

The contact form can send messages directly to your inbox via SMTP. Configure the following environment variables before running `streamlit run app.py` (create a `.env` file or set them in your shell/user environment):

| Variable | Description |
| --- | --- |
| `PORTFOLIO_SMTP_HOST` | SMTP server hostname (e.g., `smtp.gmail.com`) |
| `PORTFOLIO_SMTP_PORT` | SMTP port, usually `587` for TLS |
| `PORTFOLIO_SMTP_USERNAME` | SMTP account username/login |
| `PORTFOLIO_SMTP_PASSWORD` | SMTP account password or app-specific password |
| `PORTFOLIO_SMTP_SENDER` *(optional)* | Email address used in the **From** header (defaults to the username) |
| `PORTFOLIO_CONTACT_RECIPIENT` | Destination email address for incoming messages |

Once these are set, the "Direct Message" form on the Contact page will email you every submission. If the variables are missing, the form stays visible but shows an info banner indicating email delivery is disabled.

## 🎨 Customization Guide

### Changing Colors
Edit the CSS in `app.py` (main file), look for the style section:
```python
--accent-color: #00d4ff;  # Change this hex code for accent color
--primary-color: #1f1f1f; # Change this for primary color
--text-color: #e0e0e0;    # Change this for text color
```

### Adding New Skills
In `portfolio_pages/skills.py`, add new skills to the `skills_data` dictionary:
```python
skills_data = {
    "New Category": ["Skill1", "Skill2", "Skill3"]
}
```

### Adding New Projects
In `portfolio_pages/projects.py`, duplicate the project card section and update with your new project details.

### Updating Contact Information
Edit the contact links in:
- `app.py` (sidebar info)
- `portfolio_pages/home.py` (home page links)
- `portfolio_pages/contact.py` (contact page)

### Changing Personal Information
Update your name and details in:
- `app.py` (page title and sidebar)
- `portfolio_pages/home.py` (introduction and education)

## 📦 Dependencies

- **streamlit**: Web application framework
- No other external dependencies required

## 🔧 Development Tips

1. **Hot Reload**: Streamlit automatically reloads when you save changes
2. **Debug Mode**: Add `print()` statements to debug; they appear in the terminal
3. **Local Testing**: Always test locally before deployment

## 🌐 Deployment Options

### Streamlit Cloud (Recommended)
1. Push your code to GitHub
2. Go to https://streamlit.io/cloud
3. Connect your GitHub repository
4. Click "Deploy"

### Other Platforms
- **Heroku** (with Procfile)
- **AWS** (with Lambda)
- **Azure** (with App Service)
- **PythonAnywhere** (simple hosting)

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Uttaran Ganguly**
- Email: uttaranganguly20@gmail.com
- GitHub: https://github.com/uttaranganguly567
- LinkedIn: https://www.linkedin.com/in/uttaran-ganguly/

---

**Last Updated:** November 25, 2025

For questions or suggestions, feel free to reach out!
