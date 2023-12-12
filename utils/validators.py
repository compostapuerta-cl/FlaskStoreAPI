from cerberus import Validator

def validate_user(name,email,role,active,password):

    user={
        "name": name,
        "email": email,
        "role": role,
        "active": active,
        "password": password
    }

    schema={
        "name": {
            "type": "string",
            "regex": "^[A-Z][a-z]+"
        },
        "email": {
            "type": "string",
            "regex": '^[a-zA-Z0-9_-]+@[a-zA-Z0-9-]+\.[a-z.]+$'
        },
        "role": {
            "type": "string",
            "allowed": ["ADMIN","USER"]
        },
        "active": {
            "type": "boolean"
        },
        "password": {
            "type": "string",
            "minlength": 6
        }
    }

    return validation(name,schema,user)

def validate_product(name,price,units):

    product={
        "name": name,
        "price": price,
        "units": units
    }

    schema={
        "name":{
            "type": "string",
            "maxlength": 40
        },
        "price":{
            "type": "float",
            "min": 0.1
        },
        "units":{
            "type": "integer",
            "min": 1
        }
    }

    return validation(name,schema,product)

def validate_user_info(name,age,job,city,gender):

    user_info={
        "age": age,
        "job": job,
        "city": city,
        "gender": gender
    }

    schema={
        "age": {
            "type": "integer",
            "min": 18,
            "max": 65
        },
        "job": {
            "type": "string",
            "regex": "^[A-Z][a-zA-Z/ ]+",
            "maxlength": 45
        },
        "city": {
            "type": "string",
            "regex": "^[A-Z][a-zA-Z ]+",
            "maxlength": 30
        },
        "gender": {
            "type": "string",
            "allowed": ["Male","Female","Non-binary","Other"]
        }
    }

    return validation(name,schema,user_info)

def validate_category(name):

    category={"name": name}
    schema={
        "name":{
            "type": "string",
            "regex": "^[A-Z][a-zA-Z ]+",
            "maxlength": 30
        }
    }

    return validation(name,schema,category)

def validate_email(email):

    email_dictionary={"email": email}
    schema={
        "email":{
            "type": "string",
            "regex": '^[a-zA-Z0-9_-]+@[a-zA-Z0-9-]+\.[a-z.]+$'  
        }
    }
    return validation(email,schema,email_dictionary)

def validation(identifier, schema, value):
    v=Validator(schema)
    if v.validate(value):
        return True
    else:
        print(f"{identifier} info errors: {v.errors}")
        return False