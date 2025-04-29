from app import app  # Import your Flask app instance
import os  # Import os to access environment variables

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    # Make sure Flask runs on 0.0.0.0 and uses the port from environment variable
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
