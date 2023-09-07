from src.app.queries.users.user_queries import UserQueries
from src.app.services.users.user_service import UserService

def user_service() -> UserService:
    queries = UserQueries()
    return UserService(queries=queries)