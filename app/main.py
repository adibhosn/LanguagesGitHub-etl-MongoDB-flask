from flask import Flask
from app.routes.languages import languages_blueprint
from app.routes.etl import etl_blueprint


app = Flask(__name__)
app.register_blueprint(languages_blueprint, url_prefix='/api')
app.register_blueprint(etl_blueprint, url_prefix='/api')

# Health check route
@app.route('/')
def health_check():
    return {"status": "OK", "message": "GitHub Analysis API is running"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)