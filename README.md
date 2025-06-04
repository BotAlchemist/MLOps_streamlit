# 🚀 MLOps with Streamlit + GitHub Actions CI/CD

This project demonstrates a complete hands-on setup for **CI/CD (Continuous Integration and Deployment)** using:

- 🐍 **Python + Streamlit** for the app
- ✅ **GitHub Actions** for CI (automated testing)
- ☁️ **Streamlit Cloud** for CD (automatic deployment)

---

## 📌 Features

### ✅ Streamlit App Features
- Welcome message and interactive button
- Text input greeting (`"Hello, <name>!"`)
- Square calculator (number input)
- Current date & time display
- Custom theme using `.streamlit/config.toml`

### ✅ CI (Continuous Integration)
- Every push or pull request triggers:
  - Python environment setup
  - Dependency installation
  - Automated unit tests
- GitHub Actions workflow: `.github/workflows/ci.yml`

### ✅ CD (Continuous Deployment)
- App is auto-deployed to **Streamlit Cloud** on every `main` branch update
- No manual deployment needed after merging pull requests

---

## 🧪 How CI Works (Simplified)

1. Developer creates a new **feature branch**
2. Adds/modifies code and pushes to GitHub
3. Opens a **Pull Request** to `main`
4. GitHub Actions runs:
   - ✅ `pip install` dependencies
   - ✅ `unittest` runs test cases
5. Only when tests pass → PR can be merged
6. ✅ **CI Successful!**

---

## 🚀 How CD Works (Simplified)

1. When PR is **merged to `main`**
2. **Streamlit Cloud** auto-detects the change
3. App is redeployed live — zero manual steps!

---

## 🧰 Tech Stack

| Tool           | Role                         |
|----------------|------------------------------|
| Streamlit      | UI Framework                 |
| GitHub Actions | CI: Run tests automatically  |
| Streamlit Cloud| CD: Deploy app automatically |
| Python         | Core programming language    |

---

## 🛠️ File Structure

MLOps_streamlit/
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── tests/
│ └── test_app.py # Basic test cases
├── .github/
│ └── workflows/
│ └── ci.yml # GitHub Actions CI config
└── .streamlit/
└── config.toml # Theme customization

---

## 🎨 Theme Preview

This app uses a custom **dark mode theme**:

```toml
[theme]
base="dark"
primaryColor="#00c4ff"
backgroundColor="#0e1117"
secondaryBackgroundColor="#262730"
textColor="#f5f5f5"
font="monospace"
