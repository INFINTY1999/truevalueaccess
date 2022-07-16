Managing the user’s data(REST-API)

It has following functionalities:

    .list users (https://truevalueaccess.herokuapp.com/api/users GET)
	
    .search user by First Name or Last Name (https://truevalueaccess.herokuapp.com/api/users?name=James GET)
	
    .sort list by field(like = age,name,zip,etc.) (https://truevalueaccess.herokuapp.com/api/users?sort=-age GET)
    
    .pagination of users list (https://truevalueaccess.herokuapp.com/api/users?page=1&limit=10 GET)
	 There are 2 field in pagnation :- 1. page = 1(default value), last(write last to get to the last page)
	                                   2. limit = 5(default value)
	
    .create new user (https://truevalueaccess.herokuapp.com/api/users - POST)
	
    .get detail of a user (https://truevalueaccess.herokuapp.com/api/users/{id} - GET)
	
    .update details of a user (https://truevalueaccess.herokuapp.com/api/users/{id} - PUT)
	
    .delete a user (https://truevalueaccess.herokuapp.com/api/users/{id} - DELETE)
    
    
    This is a Webpage.
    Live :- https://simplestockpriceview.herokuapp.com/
