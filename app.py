from flask import Flask, render_template, request, redirect, url_for, flash, send_file, session
from functools import wraps
import os
from dotenv import load_dotenv
import pandas as pd
from database_operations import create_reports_table, delete_reports_table, get_all_logs, truncate_table
from datetime import datetime
import io

load_dotenv()

if not os.path.exists('backups'):
    os.makedirs('backups')

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    if request.form['username'] == ADMIN_USERNAME and request.form['password'] == ADMIN_PASSWORD:
        session['logged_in'] = True
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))
    flash('Invalid username or password!', 'error')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/create_table', methods=['POST'])
@login_required
def handle_create_table():
    try:
        create_reports_table()
        flash('Table created successfully!', 'success')
    except Exception as e:
        flash(f'Error creating table: {e}', 'error')
    return redirect(url_for('dashboard'))

@app.route('/truncate_table', methods=['POST'])
@login_required
def handle_truncate_table():
    try:
        truncate_table()
        flash('Table truncated successfully!', 'success')
    except Exception as e:
        flash(f'Error truncating table: {e}', 'error')
    return redirect(url_for('dashboard'))

@app.route('/delete_table', methods=['POST'])
@login_required
def handle_delete_table():
    try:
        # First get backup
        df = get_all_logs()
        if not df.empty:
            # Ensure backups directory exists
            if not os.path.exists('backups'):
                os.makedirs('backups')
            # Save to Excel
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_filename = f'reports_backup_{timestamp}.xlsx'
            df.to_excel(f'backups/{backup_filename}', index=False)
        
        delete_reports_table()
        flash('Table deleted successfully! Backup created.', 'success')
    except Exception as e:
        flash(f'Error deleting table: {e}', 'error')
    return redirect(url_for('dashboard'))

@app.route('/download_logs')
@login_required
def download_logs():
    try:
        df = get_all_logs()
        if df.empty:
            flash('No data to download!', 'warning')
            return redirect(url_for('dashboard'))
        
        # Create Excel file in memory
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False)
        output.seek(0)
        
        return send_file(
            output,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            as_attachment=True,
            download_name=f'reports_{datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx'
        )
    except Exception as e:
        flash(f'Error downloading logs: {e}', 'error')
        return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)