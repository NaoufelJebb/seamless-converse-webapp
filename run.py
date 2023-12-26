from app.config import app_configurations
from app import create_app

app = create_app(app_configurations["dev"])


@app.route('/index')
def index():
    return '<h1>Happy New Year 2024 !</h1>'


if __name__ == "__main__":
    app.run()
