from src.app.db_models.user import User

class UserQueries:
    def __init__(self):
        self.model = User
        
    async def get_all_users(self):
        return await self.model.query.gino.all()