from app import create_app
from app.routes import bp

app = create_app('config.Config')
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(port=8080)
