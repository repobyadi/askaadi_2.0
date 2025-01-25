
# AI-Powered Chatbot for Supplier and Product Information

## Overview

This project is an AI-powered chatbot designed to provide users with natural language interaction to query supplier and product information. The chatbot integrates an open-source LLM for enhanced responses, uses LangGraph for workflows, and retrieves data from a PostgreSQL/MySQL database.

---

## Features

- Query product and supplier information using natural language.
- Fetch and summarize data using an LLM (e.g., GPT-3.5 or LLaMA 2).
- Responsive frontend built with React and Material UI.
- Backend powered by FastAPI and LangGraph.
- Database for storing product and supplier details.

---

## Folder Structure

```
chatbot_project/
├── backend/
│   ├── app/
│   │   ├── main.py        # FastAPI entry point
│   │   ├── database.py    # Database connection and models
│   │   ├── routes.py      # API routes
│   │   ├── langgraph.py   # LangGraph workflow for LLM
│   ├── requirements.txt   # Backend dependencies
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Chatbot.jsx # Chatbot UI component
│   │   ├── App.js          # Main React app entry
│   │   ├── index.js        # ReactDOM render
│   ├── package.json        # Frontend dependencies
├── schema.sql               # Database schema and sample data
```

---

## Setup Instructions

### 1. Database Setup

1. Install PostgreSQL or MySQL.
2. Run the `schema.sql` file to create the necessary tables and insert sample data:

   ```bash
   psql -U username -d dbname -f schema.sql
   ```

3. Update the database credentials in `database.py` under `DATABASE_URL`.

---

### 2. Backend Setup

1. Navigate to the `backend/` directory:

   ```bash
   cd backend
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:

   ```bash
   uvicorn app.main:app --reload
   ```

4. The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

### 3. Frontend Setup

1. Navigate to the `frontend/` directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the React development server:

   ```bash
   npm start
   ```

4. The app will be available at [http://localhost:3000](http://localhost:3000).

---

## Usage

1. Open the frontend in your browser.
2. Enter queries like:

   - "Show me all products under brand X."
   - "Which suppliers provide laptops?"
   - "Give me details of product ABC."

3. View the chatbot's structured and summarized responses.

---

## Technologies Used

- **Frontend:** React, Material UI, Axios
- **Backend:** FastAPI, LangGraph, SQLAlchemy
- **Database:** PostgreSQL/MySQL
- **LLM:** OpenAI GPT-3.5 (or any open-source model like LLaMA 2)

---

## Future Enhancements

- Add JWT-based authentication.
- Allow product comparisons.
- Implement chatbot memory to recall user preferences.
- Add an analytics dashboard for query tracking.

---

## Contributors

- Aditya Kumar

---

## License

This project is licensed under the MIT License.
