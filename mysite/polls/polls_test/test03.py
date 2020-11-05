from polls.models import User

user = User()
fields = user.get_deferred_fields()
print(fields)
