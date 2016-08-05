from functools import wraps

from config import Config

def authorized(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        user_id = args[1].message.from_user.id
        if user_id in Config['authorized']:
            return func(*args, **kwargs)
    return decorated
