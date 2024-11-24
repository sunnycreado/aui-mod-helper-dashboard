# AUI Mod Helper - Logs Dashboard

A professional dashboard interface for managing and monitoring moderation logs. Built with Flask and modern web technologies to provide a secure and efficient way to handle moderation data.

## Features

- **Secure Authentication**
  - Protected admin interface
  - Session management
  - Environment variable configuration

- **Database Operations**
  - Create/Delete tables with automatic backups
  - Truncate data while preserving structure
  - Download logs in Excel format
  - Automatic backup creation before destructive operations

- **Modern Interface**
  - Responsive design for all devices
  - Clean and intuitive UI
  - Real-time feedback with animated alerts
  - Confirmation dialogs for critical actions

## Tech Stack

- **Backend:** Python/Flask
- **Database:** PostgreSQL
- **Frontend:** HTML5, CSS3, JavaScript
- **Data Processing:** Pandas
- **Authentication:** Session-based with environment variables

## Installation

1. Clone the repository
    ```bash
    git clone https://github.com/sunnycreado/aui-mod-helper-dashboard.git
    cd aui-mod-helper-dashboard
    ```

2. Create and activate virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

4. Configure environment variables
    

5. Run the application
    ```bash
    python app.py
    ```


## Security

- Session-based authentication
- Environment variable configuration
- Automatic backup creation
- SQL injection prevention
- Secure password handling

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Author

**Sunny Creado**
- GitHub: [@sunnycreado](https://github.com/sunnycreado)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">Made with ❤️ for the AUI Moderation Community</p>