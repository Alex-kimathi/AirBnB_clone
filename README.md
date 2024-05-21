# 0x00. AirBnB clone - The console

## Descritption
The goal of the project is to deploy on your server a simple copy of the[AirBnB website.](https://www.airbnb.com/)
The task is to make a clone of the website and build it and finally have it hosted in a server.
At the end of the project, we will have a complete web application composed by:

 * A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
 * A website (the front-end) that shows the final product to everybody: static and dynamic
 * A database or files that store data (data = objects)
 * An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

### Tasks
1. A command prompt interpreter.
	This is the starting front end to interact with the appllication,
	Will be build using the cmd module.

|Tasks          | Files       | Description|
|:--------------|:------------|:-----------|
|0. README, AUTHORS | AUTHORS  |Have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository|
|1. Be pycodestyle compliant! |The pycodestyle checks  | All code is pep8 compliant
|2. Unittests|tests/|Test cases for the classes
|3. BaseModel|models/base_model.py, models/__init__.py, tests/|Creates class BaseModel that defines all common attributes/methods for other classes
|4. Create BaseModel from dictionary|models/base_model.py, tests/|Re-create an instance with this dictionary representation (<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>)
|5. Store first object|models/engine/file_storage.py, models/engine/__init__.py, models/__init__.py, models/base_model.py, tests/|Convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. i.e Serialization and Deserialization
|6. Console 0.0.1|console.py|The command interpreter for manupulating data
|7. Console 0.1|console.py| Uprate the command interpreter to perfom CRUD operations
|8. First User|models/user.py, models/engine/file_storage.py, console.py, tests/|Creates User that inherits from BaseModel
|9. More classes!|models/state.py, models/city.py, models/amenity.py, models/place.py, models/review.py, tests/| Adds more classes that inherit from BaseModel: State,city,amenity review
|10. Console 1.0|console.py, models/engine/file_storage.py, tests/|Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review. Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created


### Application usage

1. Clone the repo