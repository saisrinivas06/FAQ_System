# FAQ Management System

A Django-based FAQ management system that allows users to view frequently asked questions in multiple languages (English, Hindi, Bengali). The system supports CRUD operations for FAQs and provides a REST API for integration with other applications.

---

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [API Usage](#api-usage)
4. [Running the Project](#running-the-project)
5. [Testing](#testing)
6. [Code Quality](#code-quality)
7. [Contributing](#contributing)
8. [License](#license)

---

## Features

- **Multilingual Support**: FAQs can be viewed in English, Hindi, and Bengali.
- **Admin Interface**: Easily manage FAQs through the Django admin panel.
- **REST API**: Fetch FAQs programmatically using the provided API.
- **Responsive UI**: A clean and modern user interface for viewing FAQs.
- **Unit Tests**: Comprehensive tests for models, views, and API endpoints.

---

## Installation

Follow these steps to set up the project locally.

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- PostgreSQL (or any other database supported by Django)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/faq-management.git
   cd faq-management
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**:
   - Update the `DATABASES` setting in `settings.py` to match your database configuration.
   - Run migrations:
     ```bash
     python manage.py migrate
     ```

5. **Create a Superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Load Sample Data (Optional)**:
   Use Django fixtures or the admin panel to add sample FAQs.

---

## API Usage

The FAQ Management System provides a REST API for fetching FAQs.

### Endpoints

- **List FAQs**: `GET /api/faqs/`
- **Retrieve a Single FAQ**: `GET /api/faqs/{id}/`

### Example Requests

1. **List All FAQs**:
   ```bash
   curl -X GET http://localhost:8000/api/faqs/
   ```

   **Response**:
   ```json
   [
       {
           "id": 1,
           "question": "What is Django?",
           "answer": "Django is a web framework for Python.",
           "question_hi": "डजांगो क्या है?",
           "answer_hi": "डजांगो पायथन के लिए एक वेब फ्रेमवर्क है।",
           "question_bn": "ডjango কি?",
           "answer_bn": "ডjango পাইথনের জন্য একটি ওয়েব ফ্রেমওয়ার্ক।"
       }
   ]
   ```

2. **Retrieve a Single FAQ**:
   ```bash
   curl -X GET http://localhost:8000/api/faqs/1/
   ```

   **Response**:
   ```json
   {
       "id": 1,
       "question": "What is Django?",
       "answer": "Django is a web framework for Python.",
       "question_hi": "डजांगो क्या है?",
       "answer_hi": "डजांगो पायथन के लिए एक वेब फ्रेमवर्क है।",
       "question_bn": "ডjango কি?",
       "answer_bn": "ডjango পাইথনের জন্য একটি ওয়েব ফ্রেমওয়ার্ক।"
   }
   ```

---

## Running the Project

1. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

2. **Access the Application**:
   - Open your browser and go to `http://localhost:8000/faqs/` to view the FAQ list.
   - Access the admin panel at `http://localhost:8000/admin/` to manage FAQs.

---

## Testing

The project includes unit tests for models, views, and API endpoints. To run the tests:

1. Install `pytest` and `pytest-django`:
   ```bash
   pip install pytest pytest-django
   ```

2. Run the tests:
   ```bash
   pytest
   ```

---

## Code Quality

The project follows PEP8 guidelines for Python and ESLint for JavaScript (if applicable).

### Python (flake8)
Run `flake8` to check for PEP8 compliance:
```bash
flake8 .
```

### JavaScript (ESLint)
Run ESLint to check JavaScript files:
```bash
npx eslint static/js/
```

---

## Contributing

We welcome contributions! Please follow these steps to contribute:

1. **Fork the Repository**:
   - Fork the project on GitHub.

2. **Create a Branch**:
   - Create a new branch for your feature or bugfix:
     ```bash
     git checkout -b feature/your-feature-name
     ```

3. **Make Changes**:
   - Write your code and ensure it follows PEP8/ESLint guidelines.
   - Add unit tests for new features or bugfixes.

4. **Commit Your Changes**:
   - Write clear and concise commit messages.
   - Push your changes to your forked repository:
     ```bash
     git push origin feature/your-feature-name
     ```

5. **Submit a Pull Request**:
   - Open a pull request against the `main` branch of the original repository.
   - Provide a detailed description of your changes.

---

## Docker Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/faq-management.git
   cd faq-management

2. Build and start the containers:
        docker-compose up --build
3. Run migrations:
        docker-compose exec web python manage.py migrate
4. Create a superuser:
        docker-compose exec web python manage.py createsuperuser
5. Access the application:

    Django app: http://localhost:8000/

    Admin panel: http://localhost:8000/admin/

    