Managing the user’s data(REST-API)

It has following functionalities:

    list users (http://127.0.0.1:8000/api/users GET)
    search user by First Name or Last Name (http://127.0.0.1:8000/api/users?name=James GET)
    sort list by field (http://127.0.0.1:8000/api/users?sort=-age GET)
    pagination of users list (127.0.0.1:8000/api/users?page=1&limit=10 GET)
    create new user (http://127.0.0.1:8000/api/users - POST)
    get detail of a user (http://127.0.0.1:8000/api/users/{id} - GET)
    update details of a user (http://127.0.0.1:8000/api/users/{id} - PUT)
    delete a user (http://127.0.0.1:8000/api/users/{id} - DELETE)
    
    Application have the following endpoints:-
    
