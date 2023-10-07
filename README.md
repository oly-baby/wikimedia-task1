# wikimedia-task
WIKIMEDIA- ASSIST CAPACITY EXCHANGE DEVELOPMENT

Repository for WIKIMEDIA Assist Capacity Exchange Development Django Project for the Outreach Applicant Task.

## PROJECT DESCRIPTION:
The Wikimedia project's goal is to develop a Bug app designed for users to access and oversee bug reports across diverse software projects. This app offers a space for users to submit bug reports, monitor the progress of these issues, and engage in collaborative efforts with both users and developers to resolve them.

## FEATURES OF THIS PROJECT:

Submission Of Bugs: Users have the capability to submit bug reports by furnishing comprehensive details about the problem, including instructions to replicate it, anticipated outcomes, and the observed behavior.

Tracking Of Bugs:The application enables users to monitor the progress of their submitted bug reports, providing them with information about the current status, assigned individuals, and any comments or updates associated with the bug.


Managing Of Bugs: The application offers a robust platform for effectively handling bug reports, encompassing functionalities such as assigning bugs to specific developers, establishing priority levels, and categorizing bugs according to their severity or impact.

Details View Of Bugs: Users have the ability to access in-depth details about each bug report, encompassing its description, status,dates and any other discussions or updates.

## Installation
To get started with the Wikimedia project, follow these steps:

 cd wikimedia<br>
 python3 -m venv env<br>
 source env/bin/activate<br>
 pip install django<br>
 pip install -r requirements.txt<br>
 python manage.py makemigrations<br>
 python manage.py migrate<br>
 python manage.py createsuperuser<br>
 python manage.py runserver<br>


## Usage

To use the Wikimedia project, follow these steps:

The homepage list all the bugs and a possibility to register a bug link. From the homepage you can have access to the details of each bug. The sample url is http://127.0.0.1:8000/

Sign in with your superuser account created during the installation process to access the admin panel.http://127.0.0.1:8000/admin/

Explore the bug reports:http://127.0.0.1:8000/admin/bug/bug/

View Bug List: On the homepage, you can see a list of bug reports submitted by users. Click on a bug report to view its details.http://127.0.0.1:8000/

To create new bug: click create new bug, click on the "create Bug" button and fill in the required information, such as the bug description, report date,type ans status.http://127.0.0.1:8000/add_bug/

Track Bug Status: After submitting a bug report, you can track its status by visiting the bug homepage.http://127.0.0.1:8000/

Manage Bug Reports (Admin Panel):http://127.0.0.1:8000/admin/
