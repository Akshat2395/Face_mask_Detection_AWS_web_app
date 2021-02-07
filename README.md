# Face_mask_Detection_AWS_web_app

**NOTE** - This project was deployed on an AWS EC2 instance which is no longer available now.

**Please have a look at the documentation for more details about the project**

**The documentation provides a step-by-step guide to how you can create and run an AWS EC2 instance and access the web application. The report further discusses about the functionality and features of the web app.**


## Objective

The aim of this project is to develop a simple web application that uses AI to determine whether individuals that show up in a picture are wearing a mask.

This project provided an experience developing web application using Python and Flask, and deploying and running this application on Amazaon EC2. 


## Application Functionality
1. **Login panel** - 

Access to the application requires authentication by providing a username and password. Includes support for password recovery via email.

2. **User management** - 

As this is not a public application, only the administrator is able to create additional user accounts. The only way to create new accounts is for the
administrator to login and create the account. User accounts have access to all features in the website, with the exception that they are not able to create or
delete user accounts. All users have the ability to change their password.

3. **Mask detections** -

Authenticated users are able to run mask detection on images they specify. A user uploads an image by selecting it from their local file system, or by typing a URL for a location on the web from which the image can be downloaded. After an image is supplied, the application displays the number of faces that are detected, the number that are wearing masks, and shows a new version of the image with red rectangles drawn around the faces of people who are not wearing masks and green rectangles drawn on the faces of those that are.

4. **Upload history** - 

Authenticated users are able to browse lists of previously uploaded images. The history is split into 4 lists: images with no faces detected, images where all faces are wearing masts, images where all faces are not wearing a mask, and images where only some faces are wearing masks.


## App Features

* All user data is stored in a relational database.

* All users have a unique username and the password set by the user has to go through a requirement check in order to access the application.

* The password is first being hashed, then stored in the database with the respective salt value.

* All photos uploaded to the app are stored in the local file system (i.e., on the virtual hard drive of the EC2 instance). A user might upload different photos having similar     names. In this case, the application treats them as different photos and stores just the location and name of the photo in the relational database.

* All inputs are validated with reasonable assumptions (for example, do not let the user upload unreasonably big files). Also, the app does not rely only on browser-side validation but does the validation on the server side too.

* Appropriate error and success messages are displayed to the user during user interaction with the web application.

* The application supports different users simultaneously logged in into the applications using different computers.
