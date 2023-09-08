from src.app.queries.user_queries import UserQueries
from src.app.services.user import UserService

def user_service() -> UserService:
    queries = UserQueries()
    return UserService(queries=queries)