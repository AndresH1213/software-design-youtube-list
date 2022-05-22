from api.user import register_new_user, password_forgotten
from api.plan import upgrade_plan

"""There are two roles the subject and the observer the subject does things
    and changes things and notifies observers of any changes that happened.
    There's several variations of this pattern. Event management systems.
"""

#register a new user
register_new_user("Andres", "BestPasswordEva", "hi@testin.com")

#send a password reset message
password_forgotten("hi@testin.com")

# updgrade the plan
upgrade_plan("hi@testin.com")