# My Visa App

My Visa App is a web application designed to assist users in finding and comparing visa options for different countries. The application uses Flask as both the frontend and backend framework, with SQLite for local development and Azure SQL Database for production. The app is deployed on Azure App Service and uses GitHub for version control.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- User-friendly interface to search and compare visa options.
- Developed using Flask with Jinja2 templates.
- Local development using SQLite.
- Production database using Azure SQL Database.
- Deployed on Azure App Service.
- Version control with GitHub.

## Prerequisites

- Python 3.8 or higher
- Pip (Python package installer)
- Virtualenv
- Azure CLI
- Git

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <your-github-repo-url>
   cd my-visa-app
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate Virtual Environment**:
   - **PowerShell**:
     ```powershell
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
     .\venv\Scripts\Activate.ps1
     ```
   - **Command Prompt**:
     ```cmd
     venv\Scripts\activate.bat
     ```

4. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Configure the Database**:
   - For local development, SQLite is used. The configuration is set in `config.py`.

2. **Run the Flask Application**:
   ```bash
   python run.py
   ```

3. **Access the Application**:
   - Open your browser and navigate to `http://127.0.0.1:5000`.

## Contributing

1. **Fork the Repository**:
   - Click on the "Fork" button on the top right corner of the repository page on GitHub.

2. **Clone Your Fork**:
   ```bash
   git clone <your-fork-url>
   cd my-visa-app
   ```

3. **Create a Branch**:
   ```bash
   git checkout -b my-new-feature
   ```

4. **Make Changes and Commit**:
   ```bash
   git add .
   git commit -m "Add new feature"
   ```

5. **Push Changes to Your Fork**:
   ```bash
   git push origin my-new-feature
   ```

6. **Submit a Pull Request**:
   - Go to the original repository on GitHub and create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

By following this guide, you can set up a robust development and production environment for your Flask application using Azure services and GitHub. This setup ensures scalability, maintainability, and a smooth development experience.