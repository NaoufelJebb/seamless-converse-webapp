from app.config import app_configurations
from app import create_app

app = create_app(app_configurations["dev"])

if __name__ == "__main__":
    app.run()
