# Detection Project

A Django-based detection project with email notification capabilities.

## Features

- Django 4.2.19-based project
- Email notification system using SMTP
- Static files handling
- SQLite database
- User authentication and authorization

## Requirements

- Python 3.8.10
- Django 4.2.19
- Other dependencies listed in requirements.txt include:
  - click
  - keras
  - matplotlib
  - numpy
  - opencv-python
  - pandas
  - pillow
  - scikit-learn
  - tensorflow
  - xgboost

## Installation

1. Clone the repository
2. Create a virtual environment and activate it
3. Install dependencies
4. Configure environment variables
    - Create a `.env` file in the root directory
    - Add your email configuration (replace with your credentials):

## Configuration

The project uses the following key configurations:
- SQLite database
- Email backend using SMTP (Gmail)
- Static files serving
- Django admin interface

## Security Notes

- Debug mode is currently set to True (disabled in production)
- Make sure to set proper ALLOWED_HOSTS in production
- Use environment variables for sensitive information
- Change the SECRET_KEY before deploying to production

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License—see the LICENSE file for details.