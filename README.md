# AUI Mod Helper - Logs Dashboard

A professional dashboard interface for managing and monitoring moderation logs. Built with Flask and modern web technologies to provide a secure and efficient way to handle moderation data.

## Live Demo
[AUI Mod Helper Dashboard](https://aui-mod-helper-dashboard.vercel.app/)

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
- **Deployment:** Vercel

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

4. Configure environment variables in `.env` file:
    ```
    DATABASE_URL=your_database_api_from_neon_tech
    SECRET_KEY=your_secret_key
    ADMIN_USERNAME=your_admin_username
    ADMIN_PASSWORD=your_admin_password
    ```

    > **Database Setup:**
    > - Get your free PostgreSQL database from [Neon Tech](https://neon.tech/)
    > - Copy the connection string from your Neon dashboard
    > - Paste it as your DATABASE_URL in the .env file

5. Run the application
    ```bash
    python app.py
    ```

## Deployment

The application is deployed on Vercel. To deploy your own instance:

1. Fork this repository
2. Create a new project on [Vercel](https://vercel.com)
3. Connect your GitHub repository
4. Add your environment variables in the Vercel dashboard:
   - DATABASE_URL
   - SECRET_KEY
   - ADMIN_USERNAME
   - ADMIN_PASSWORD
5. Deploy!

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