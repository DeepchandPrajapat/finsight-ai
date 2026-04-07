# 💰 FinSight AI

**FinSight AI** is a full-stack expense tracking and budgeting application that helps users monitor their finances, visualize spending patterns, and gain AI-powered insights.

---

## 🌐 Live Demo

* 🔗 Frontend: https://finsight-ai-app.netlify.app/
* 🔗 Backend API: https://spendwise-ai-mn0e.onrender.com

> Deployed using **Netlify (frontend)**, **Render (backend)**, and **Neon PostgreSQL (database)**

---

## 🚀 Features

### 📊 Dashboard

* Total and monthly spending overview
* Interactive **doughnut chart** (category-wise breakdown)
* **Sparkline trend chart** (recent spending activity)
* Smooth animated financial metrics

### 💸 Expense Management

* Add and manage expenses
* Custom categories support
* Real-time updates

### 📅 Budget Tracking

* Monthly budget tracking
* Visual progress indicators
* Budget history overview

### 🤖 AI Insights

* Smart financial insights
* Spending pattern analysis
* Personalized recommendations

### 🎨 UI/UX

* Sticky navbar + toggleable sidebar
* Responsive and clean layout
* Smooth transitions and animations
* Modern design using Tailwind CSS

---

## 🛠️ Tech Stack

### Backend

* Python (Flask)
* SQLAlchemy (ORM)
* Flask-Migrate

### Frontend

* HTML, Tailwind CSS
* Vanilla JavaScript
* Chart.js

### Database

* Neon PostgreSQL

### Deployment

* Netlify (Frontend)
* Render (Backend)

---

## ☁️ Deployment Architecture

* Frontend hosted on **Netlify**
* Backend API hosted on **Render**
* Database powered by **Neon PostgreSQL**
* Environment variables managed via `.env`

---

## 📂 Project Structure

```
root/
│
├── app/
│   ├── routes/
│   │   ├── budgets.py
│   │   └── expenses.py
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   └── models.py
│
├── frontend/
│   ├── assets/
│   │   └── logo4.png
│   ├── script/
│   │   ├── dashboard.js
│   │   ├── add-expense.js
│   │   ├── expenses.js
    │   ├── utils.js
│   │   └── budget-history.js
│   ├── index.html
│   ├── add-expense.html
│   ├── expenses.html
│   └── budget-history.html
│
├── migrations/
├── venv/
├── .env
├── .gitignore
├── api_test.http
├── Procfile
├── requirements.txt
└── run.py
```

---

## ⚙️ Local Setup

### 1. Clone repository

```
git clone https://github.com/DeepchandPrajapat/finsight-ai.git
cd finsight-ai
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file:

```
FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
```

### 5. Run the application

```
python run.py
```

---

## 📈 Future Improvements

* User authentication (login/signup)
* Dark mode support
* Export data (PDF/CSV)
* Advanced analytics & predictions
* Improved mobile responsiveness

---

## 💡 Key Highlights

* Full-stack deployed application
* Clean and scalable architecture
* Interactive financial dashboard
* AI-powered insights integration
* Real-world deployment experience

---

## 🙌 Author

Built with a focus on learning, design, and real-world usability.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
