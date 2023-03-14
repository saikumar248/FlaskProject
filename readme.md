In order to get started you need to install the dependencies using the pip command as shown below

pip install flask_pymongo

pip install bcrypt

pip install jsonfy

As you can see we are installing the above dependencies inside the flask project. Now we need to create the app.py file and copy paste the following code

As you can see we are importing the required libraries such as the flask and also the flask_pymongo library. And then we are making the new flask app. And also we are setting the secret key and also we are setting the config url of the mongo database. And here as you can see the mongodb uri contains the port number which is 27017 and also we have the mongodb database which is crud here. And then we are wrapping the flask app inside the PyMongo constructor. And then we are starting the flask app using the run() method.

Creating the Database in MongoDB

You can start the MongoDB Compass desktop software and then we can create a new database and Collections using MongoDB

Thats it for introduction
