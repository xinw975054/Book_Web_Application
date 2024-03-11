import flask_jwt_extended

all_attributes = dir(flask_jwt_extended)

# Filter for functions only
functions = [attr for attr in all_attributes if callable(getattr(flask_jwt_extended, attr))]

# Print the list of functions
print("Functions in flask_jwt_extended:")
for func in functions:
    print(func)