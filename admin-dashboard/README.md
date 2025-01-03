# README.md

# Admin Dashboard

This project is an admin dashboard built with Flask, designed for managing blog posts and other administrative tasks. 

## Project Structure

```
admin-dashboard
├── app
│   ├── __init__.py          # Initializes the Flask application
│   ├── routes.py            # Defines the application routes
│   ├── templates
│   │   ├── base.html        # Base layout for the admin dashboard
│   │   └── index.html       # Main dashboard page
│   └── static
│       └── styles.css       # CSS styles for the dashboard
├── run.py                   # Entry point for running the application
├── config.py                # Configuration settings for the application
└── README.md                # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd admin-dashboard
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   python run.py
   ```

5. **Access the dashboard:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Use the sidebar to manage posts and navigate through different sections of the admin panel.
- Customize the styles in `app/static/styles.css` to fit your design preferences.

## License

This project is licensed under the MIT License.