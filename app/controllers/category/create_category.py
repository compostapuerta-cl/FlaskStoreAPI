from app.models.category import Category

class CreateCategory:

    def __call__(self,request):

        if request.is_json:

            data=request.get_json()
            name=data["name"]
            new_category=Category(name=name)

            if new_category.save():
                return {"message": f"category {new_category.name} has been created successfully."}
            else:
                return {"message": f"category {new_category.name} could not be created"}
        else:
            return {"error": "The request payload is not in JSON format"}