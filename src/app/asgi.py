from src.app.app import BaseApi

api = BaseApi(title="My Application", version="V1.0.0")
app = api.get_app()
