# SunFresh - Final Project (Timothy Sullivan, Taylor Paielli)

This application enables ASU students to place orders and check wait times for their favorite dining locations on campus.
Our application designed by Timothy Sullivan and Taylor Paielli can be scaled up and actually utilized by the university of deemed valuable.

## Installation

Downloading the necessary zip file and running the .py file from either the terminal, command prompt, or desktop will start the application up.
Users may need to install kivy using pip or git to enable the application to function as intended.
[Kivy Documentation](https://kivy.org)

```bash
pip install kivy
```

```bash
pip install time
```


```shell
$ python3 SunFresh.py
```

### Log in credentials

Feel free to use any credentials you would like to test the applications functionality.

### Kivy File .kv Syntax

Most of the logic of our application is found within the .kv file. More can be found at this link to understand our styling and functionality. We had to teach ourselves the very complicated language that is the kv language.
[Kivy Syntax](https://kivy.org/doc/stable/guide/lang.html)

### Order a menu item

Navigate throughout the user interface and select desired food item. Order information will be saved to JSON file in dictionary format.

### Exit 

The log out option on the home screen will exit and close the application.

### Class

There is a class that takes a Screen object for every screen within the application. The screen manager then takes an instance of each class and adds it to a Kivy widget. Each class has a functino defined within it that correlates to what is saved within the JSON file. 

Instance variables:
1. order_dic: public dictionary
2. Screen: instance of Screen class
3. product: instance of Order class, public string
4. prod_num: instance of Order class, public string 
5. order_time: instance of Order class, public string


### KivyApp Class

The application itself acts as an instance of the App class, which allows the program to run on a multitude of machines ranging from android devices to laptops. Various attributes of the application are set in this class. 

### Auto Testing

Run the following command to test the .py file
```shell
$ pip install pytest
$ pytest -v
```

### Test Results

| Product       | Product_No | Date & Time              |
|---------------|------------|--------------------------|
| Supreme Nacho | 4          | Thurs. Dec 1. 12:30:21   |


### Future additions
We plan on having a functional back end at some point as to enable more dynamic elemetns across the application and user experience. 