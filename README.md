Managing the user’s data(REST-API)

It has following functionalities:

    .list users (http://127.0.0.1:8000/api/users GET)
	
    .search user by First Name or Last Name (http://127.0.0.1:8000/api/users?name=James GET)
	
    .sort list by field(like = age,name,zip,etc.) (http://127.0.0.1:8000/api/users?sort=-age GET)
    
    .pagination of users list (127.0.0.1:8000/api/users?page=1&limit=10 GET)
	 There are 2 field in pagnation :- 1. page = 1(default value), last(write last to get to the last page)
	                                   2. limit = 5(default value)
	
    .create new user (http://127.0.0.1:8000/api/users - POST)
	
    .get detail of a user (http://127.0.0.1:8000/api/users/{id} - GET)
	
    .update details of a user (http://127.0.0.1:8000/api/users/{id} - PUT)
	
    .delete a user (http://127.0.0.1:8000/api/users/{id} - DELETE)
    
    
    This is a Webpage.
    Live :- https://simplestockpriceview.herokuapp.com/
