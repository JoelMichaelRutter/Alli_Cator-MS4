# **[Alli_cator](https://alli-cator-ms4.herokuapp.com/)**
Alli_cator is a full stack business-based web application. I built this application with my current full-time job in mind as I thought it would be beneficial for my portfolio to demonstrate that I could create a piece of software that would serve a tangible benefit in the workplace. 

My role is in the customer complaints function of a retailer and financial services company. The existing system we use to capture, manage, and keep a record of complaints isn’t user-friendly or streamlined – sometimes creating more work for the user (colleague), taking up more of their time than necessary. A problem with this system is that it doesn’t always order and filter database entries correctly, and even when it does function as it should – users still have to spend time searching through information and navigate through various screens to get the latest update on a complaint, reducing their efficiency and timeliness in responding to a customer and resolving their issue. 

To get around this, colleagues sometimes use more widely available applications such as Microsoft Excel spreadsheets to keep track of the complaints that they have allocated to them to manage. These are often unwieldly, not very user-friendly, and generally not intuitive. This also can cause consistency and quality issues due to colleagues using different systems, whereas one cohesive solution would be much better. Also, the stress caused by having to trawl through information when you have a dissatisfied customer on the phone is stressful whereas being able to see the latest update at the click of a button is very handy.

On that basis, I’ve built a full stack application to pair with the Complaints Management System that the business has already implemented which will allow users to easily create, read, update, and delete complaints with ease.

## Table of contents
* ### [Deployed Site](#deployed-website)
* ### [Demo](#site-demonstration)
* ### [UX](#user-experience)
* ### [Design](#design-features)
* ### [Features](#functional-features)
* ### [Technologies](#technologies-used)
* ### [Testing](#application-testing)
* ### [Deployment](#deploying-the-site)
* ### [Reflection](#project-reflection)
* ### [Further Development](#further-development-scope)
* ### [Credits](#project-credits)
* ### [Acknowledgement](#project-acknowledgements)
# <a id="deployed-website"></a>
# [**Deployed Website**](https://alli-cator-ms4.herokuapp.com/)  
By clicking the hyperlinked header above, you can access the final deployed site hosted on Heroku.
# <a id="site-demonstration"> **Site Demonstration**
## [Am I Responsive?](http://ami.responsivedesign.is/)
Below you can see an image of the final site in the Am I Responsive tool which shows the fantastic level of responsivity of the site to a number of viewports. A link to the tool is attached in the header above.  
![allicator-amiresponsive](readme-files/images/amiresponsive/am-i-responsive.png)
# <a id="user-experience"></a>**User Experience**
In this section, I will discuss the user experience considerations I implemented during the development process.
## **Strategy**
### **Business Goals**
In terms of business scope, this application provides many benefits:
* To provide the user with an intuitive easy to use system.
* To increase colleague productivity due to the removal of un-needed time on screens.
* Increase colleague satisfaction due to the implementation of an IT solution which works for them.
* Increase in consistency across all teams when it comes to complaint allocation management. 
* Increase consistency in terms of training due to a tailored solution being available for all teams.
### **User Stories**
Below are the user stories that needed to be fulfilled for the project to be successful from the perspective of the user:
* **User Story: Register** - As a **user** I should be able to **register for an Alli_cator account** so that I can access the functionality of the application.
* **User Story: Sign In** - As a **User**, I should be able to **sign in upon accessing the application** so that **I can see the complaints I have allocated to me**.
* **User Story: Add a complaint** - As a **User, once approved and authenticated,** I should be able to **add a complaint to the database** so that **I can review it going forward**.
* **User Story: Edit a complaint** - As a **User, **once authenticated**, I should be able to **update a complaint** so that **I can change its details as it progresses**.
* **User Story: Delete a complaint** - As a **User**, once authenticated, **I should be able to delete a complaint** from the database so that **I can remove it once I have dealt with it.**
* **User Story: Sign out** - As a **User**, whilst authenticated, **I should be able to sign out of the application so that I can ensure nothing happens to my complaints when I am not using the application.**  

Following the planning stage of the project, these user stories were added to a project Kanban board on the GitHub repository so that I could adopt an agile approach and develop each piece of significant functionality at a time.
Before going any further, I think it would be beneficial for the readers of this document to understand the application that I built this one to pair with. The application that the business uses to record, close (resolve), and keep a history of complaints is called the Complaints Management System or CMS. Not to be confused with Content Management System, I will refer to the system as CMS moving forward .
When a user signs into the CMS, an unfiltered list of all database entries are presented to the user. CMS sometimes filter in date order, but it is temperamental  . 

![cms-screenshot](readme-files/images/readme/1-cms-screenshot.png)  
To locate a complaint, the user would need to use the filter. Granted there are many fields to filter the entries on but the problem remains that the ordering of the complaints does not come in any order and the key human identifiers for the customer are not kept on the top level of the system (customer name) so you could go into one complaint when you haven’t filtered the list and it could be the wrong one.
To access more detail about the complaint, the user then must click the view button.
If they want to access the latest update, they would then have to click the notes button and scroll through a list of notes to see where it is up to. This is less than ideal when an unhappy customer is on the phone or just when a user needs to be up to speed on a complaint quickly.


# **Structure Plane**  
I started my project by thinking about my user and the business function the user needs to satisfy. The main principles behind the development of the application were:
1. Ease of use – The application is easy to use and should be intuitive so that someone with little technical ability or exposure can pick it up straight away.
2. Reduce information overload – The user should no longer need to dig through screens and notes or use cells in a spreadsheet. The information should be at the fingertips and easy to read.
3. Consistency – This application will replace the various tools used by colleagues within the business so that there is a central platform.

While a system such as this is usually designed for use on a laptop or desktop monitor, I did approach the design of the application with a mobile first attitude . I also knew that I wanted to incorporate the libraries and frameworks that I’d learnt during this part of the course.

One of the key principles behind the application was the reduction of information overload. If you look at the example spreadsheet that one of my colleagues provided to me and imagine this with 30 of the rows full of data, it would be very overwhelming. 

Whilst a system such as this is usually designed strictly for use on a laptop or desktop monitor, I did approach the design of the application with a mobile first attitude. I also knew that I wanted to incorporate the libraries and frameworks that I’d learnt during this part of the course.
One of the key principles behind the application was the reduction of information overload. If you look at the example spreadsheet below that one of my colleagues provided to me and imagine this with 30 of the rows full of data, it would be very overwhelming. 
![spreadsheet-example](readme-files/images/readme/2-excel-screenshot.png)
The first thing I did was separate what data was key when it came to retrieving an update and through this process, I designed the data model for the application which is the driving force behind the application.
At the beginning of this project, I created a plan with Microsoft Powerpoint. The first part of this plan consisted of a mind map around the technologies that I might use to develop the application to which I added the main CRUD functionality with an agile approach. Please note: this was the planning stage and some of the technologies or functionality may not have been implemented in the final version.  

![allicator-plan-mindmap](readme-files/images/readme/3-alli-mind-map.png)

From here, I developed my data model. I started again with a table to decide the data structure and where this would be presented to the user. 
![plan-data-model](readme-files/images/readme/4-model-plan.png)  
I did consider having two data models but rationalised with myself that a second data model was not required due to one of the main user considerations being a reduction of information overload . As a result, the project only has one data model and that is the Complaint model. I will touch more on this and provide a breakdown of the code later in the document. 

# **Skeleton Plane**
Now I had an idea of which technologies and functionality I would be using, I proceeded to create some basic UI sketches before doing some more detailed wireframes. Each of the wireframes are set out below.
<img src="readme-files/images/readme/5-sketched-ui.png" alt="UI sketched drawing" width="400"/>  
### **Mobile Wireframes**
![mobile-wireframes](readme-files/images/readme/6-mobile-wireframe-ui.png)
### **Tablet Wireframes**
![tablet-wireframes](readme-files/images/readme/7-tablet-wireframe-ui.png)
### **Laptop & Larger Screen Wireframes**
![larger-screen-wireframes](readme-files/images/readme/8-largescreen-wireframe-ui.png)  
Whilst the development largely stuck to these wireframes, there were some very slight deviations in terms of layout and functionality during the development process as well as some additional functionality added.

# **Design Features**
## **Colour Choices**
Below I will outline my colour choices for the project and discuss some of the main colours and the impact that this has on the user:
<img src="readme-files/images/readme/9-colour-palette.png" alt="Colour palette for the application" width="1000"/>  

* **#759252:** This is my main application colour. The name of the application is a play on the animal ‘alligator’, so I wanted a green colour to represent that. I found the colour after searching for an alligator green colour palette on Google. I didn’t want anything too murky or dark as I felt this would not appeal visually to the user, but I wanted to have a contrasting colour to that of the page body.
* **Whitesmoke (#F5F5F5):** I chose this as the colour for the body as on bright screens, the contrast between a darker colour, in this case the green of the navigation, and the default white background colour of the body is quite jarring. It isn’t far off white, but the duller tone makes the page more visually appealing and easy to view for the user whilst maintaining the contrast which gives clear indication of the sections of the page.
* **Lightgray (#D3D3D3):** I chose this as the background colour for my forms to ensure that the colour did not distract the user from the form content.
* **#E8BD6E:** I chose this colour as one of my main action accent colours. It has a pleasant visual contrast with the main green colour I used. 
* **#eb3939:** Whilst this red did not appear on my colour palette in relation to the main application colours, I knew that I wanted any delete functionality to be visually reinforced to the user with a striking colour. As such, I used the red colour rule in CSS and then used the colour picker within dev tools to locate a shade which was both visually striking and in-keeping with the pastel colours utilised by the rest of the application. 

In terms of tools, I used when it came to colours, I used:  
* **[ColourSpace](https://mycolor.space/)** to get complimentary colours for my main green colour.
* **[Opposite colour tool](https://www.colortools.net/color_complementary.html)** which allowed me to find the opposites of the colours I selected to use within hover pseudo selectors to provide visual feedback to users of their actions.

## **Imagery**	
In terms of imagery, there was little need for any imagery due to the data focused nature of the application. I did make an exception to this and included a little alligator logo which I downloaded as a PNG from [Flaticon](https://www.flaticon.com/premium-icon/crocodile_3120796?term=alligator&page=1&position=8&page=1&position=8&related_id=3120796&origin=search). These icons are free provided that the author is attributed, so thanks very much Freepik. I did use Flaticon to change the colour of the icon to white.

## **Iconography**	
In terms of iconography for the rest of the site, I used Font Awesome’s free library which is inserted via CDN in the base template head. You can find more information on how to sign up and use the service [here](https://fontawesome.com/).  
In terms of the specific icons, they can be located in the code within the classes of all "i" elements. 

## **Fonts**	
I chose my font to pair with Bootstraps standard font, I knew I wanted some sort of Mono font, so I auditioned using Google Fonts. I eventually settled on **Roboto Mono** as my custom font which is used throughout the project for headings buttons and text for visual accents. I used three font weights which I will detail in the screenshots below.  

![roboto-mono-400](readme-files/images/readme/10-font-400.png)

![roboto-mono-600](readme-files/images/readme/10-font-600.png)

![roboto-mono-700](readme-files/images/readme/10-font-700.png)

# **Functional Features, Code Breakdown and Explanation**
Within this section, I will firstly detail the data model, the functional features of the application and how they relate to the user stories. From there, I will provide a front and back-end code breakdown and explanation so that should you need to understand, use, or manipulate the code for this application, you can do so with ease. Where required, I will utilise screenshots to highlight the functionality of the application.

As this application is a data-driven CRUD application, I will start with the final data model and then move to the main CRUD functionality. Finally, I’ll explain the additional libraries utilised within the project.

**Please note:**  the main custom (non-library) CRUD functionality of the application is protected by authentication which will be discussed following the main CRUD breakdown. As a result, all code explained below is on the basis of successful sign up and sign in using the Django Allauth library.

## Final Data Model
As this application is data driven, everything stems from the data model. From there I will explain the views and the templates.

<img src="readme-files/images/readme/11-model-code.png" alt="Code for allicator final data model" width="600"/>  

1. On line 6, I import the User model so that I can use it within my custom model.
2. On line 15, I create the Complaint class which inherits the Django models.Model class.
3. Log_number - From line 16 to line 21, I declare the log_number column. This is a CharField, it must be unique, it must not be blank and has a max_length of 10 characters.
4. Customer_surname – On line 22, I declare the customer_surname column. It’s a Charfield, it has a max length of 40 characters and cannot be blank.
5. Complaint_category – From line 23 to 26, I declare the complaint_category column. It’s a Charfield, it has a max length of 100 characters and cannot be blank.
6. Date_logged – On line 28, I declare the date_logged column. This is a DateField.
7. Case_owner – On line 29, I declare the case_owner column. This is a ForeignKey field. It takes the User table as it’s first parameter and then the on_delete parameter which is set to models.CASCADE. This means that if a User is deleted from the User table, all their entries are deleted as well.
8. Boolean fields – From line 30 to 33, I declare four Boolean fields. You can see the names of said columns and these Boolean fields form the status of the complaint. 
9. Latest_update - Finally, in terms of columns, I declare the latest_update database column. This cannot be blank and has a max length of 250 characters. This is ample to leave a short update with a few bullet points as to where a complaint is up to.

On line 41, I declare a Meta class to confirm how the entries should be ordered in the database. In this case, I want the entries ordered by date_logged. Oldest to newest. If you wanted to reverse this order and have newest to oldest, you could just add a “-“ before the column name. Once the Model was created and connected to my database on Heroku, which is explained within the deployment section of the document, I ran two commands:

* **Python3 manage.py migrate**
* **Python3 manage.py makemigrations**

These commands create the database table based on the model I just described which then allows for data to be created, submitted and manipulated.
