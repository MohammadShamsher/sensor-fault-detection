# sensor-fault-detection
Air Pressure braking sensor fault
Objection 1 , Data Ingestion bringing data from source
framework: group of libraries combined for a task becomes framework. or collection of libraries or packages, note package and library are same.

From command line go into the project folder and then open terminal and do below

code .


Step 1:
conda create -p venv python=3.8 -y
conda activate venv


step 2: create setup.py, it is used so that packages that you have created can be used and imported correctly without an error


step 3: create folder named sensor and there create __init__.py file so now this folder becomes a python package

step4: Do code in stup.py findpackages will go and search for libarries in the root directory.
setup() is used to "configure our package for distribution," I meant that it's the mechanism through which you specify how your package should be distributed, installed, and used by others. It's essentially a way to package up your Python project so that it can be easily shared and installed by others.
So, importing the setup() function from setuptools allows you to define these distribution configurations in your setup.py file, making it easier for users to install and use your package.
then give command python setup.py install 

It will create folder egg-info , it conntains necessary details about packages and will be used by python
Metadata Storage: The .egg-info file stores metadata about the installed package. This metadata includes information such as the package name, version, author, license, 
for Example.
Uninstallation: The .egg-info file is used during package uninstallation. When you uninstall a package, the package manager reads the metadata stored in the .egg-info file to determine which files to remove and dependencies to uninstall.

Note in requirements.txt (-e .) is for if u dont want to run setup.py and you wnagt to do 

Step 4 : pip install -r requireemnst.txt

step 5: Craete subfolder in sensor named as pipeline and make it __init__.py



Every pipeline will have some components like training, validation, testing etc so we need another folder named as components and that will be then sequenced in pipeline

step 6: Create new folder named as componenets and make __init__.py


Now we need to ingets data from source so we need another folder anmed as data_access and make it __init__.py its reponsibility will be to connect with the database and fetch data and make a csv file. 

step 7: data_access and __init__.py

Note We do this modularity because if we do all this fetching training testing vcalidating predicting code in a single file then how multi developer will work on same project with different tasks, if i want a developer to just make connectivity configurations like connect me to mongodb and he dont know mL so its okay he will just go the data_access folder and will do his code.

Step 8: craete folder named as cloud_storage and make it __init__.py this will be used to upload model on s3, get model from there etc.

Step 9: create folder named as configuration and do it __init__.py because there atre so many configurations connecting with mongodb , connecting with AWS s3 etc.


Step 10: create folder named as constant and make it __init__.py . All projects require some constants like folder name model name etc., these are basically hard coded values.

Step 11: create logger.py and exception.py in sensor because every project has exceptions and loggs too.

Step 12: create entity dolder and make it __init__.py which will contain information regarding the strudcture , regarding the input output to and from the component.

Artifact is you can say something output that will be generated by the pipeline as an output or from ML perspective the ouput trained model created by the training processs. e.g pickle saving model.

Artifact is the ouput of each component. so artifact will be in entity folder.

step 13: create artifact_entity.py , ouput to every component.

Step 14: create config_entity.py, this will be reponsible for input to every component.

step 15: craete folder ml and make it __init__.py, this willl contain functions like feature engineering or you making your custom ml model etc, custom graph or accuracy matrixes etc.

step 16: go to mongodb atlas and creat edatabase cluster and then to database option click connect and copy that url and change username and password.

step 17: create mongo_db_connection.py file in configuartion folder. which will conatin code to connect you to mongodb.

step 18: craete folder database.py in constant folder which will contain databse name etc.

step 19: Write exception code in exception.py , note there are custom exceptions which is used when error raises so it give us error name, error line number , file name in which the error is raised.

Step 20: Write logging code 

step 21: create env_variable.py which will contain info about all the variables like Aws acces key, mogo db url key etc, region aws etc. you can sav eur keys like this is the system for just this opened session export AWS_ACCESS_KEY_ID=123456, if you want permanent then you have to write this in bashrc file.

step 22: craete s3_bucket.py which will contain info regarding tarined model and predict model variable names.

Step 23: create application.py in constant which will contain variables names regading the app port , the app host need for train and predict. so it will take your system current IP .

Step 24: now we will create a subfolder inside constant folder named as training_pipeline which will contain constants only regarding training of model.

step 25: create config folder the project folder outside sensor and inside it craete folder schema.yaml which will contain information regarding the structure

