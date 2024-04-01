# Instructions

1. Cloning the project: "git clone https://github.com/hiteshpatil237/backend-challenge.git"

2. Create virtual environment: "python -m venv venv" and activate it: 
   - For Mac: " source venv/bin/activate"
   - For Windows: "venv\Scripts\activate"

3. "cd application"
     
4. Execute migrations to populate database "python manage.py migrate"


## Running the Server

1. Two users have already been created:
   - Hitesh:
      - Username: "hitesh"
      - Password: "Passw0rd@"
   - Ahmed:
      - Username: "ahmed"
      - Password: "Passw0rd@"

2. Run the server using: `python manage.py runserver`

3. Login to the admin panel using any of the above credentials.
   - Go to "http://127.0.0.1:8000/"

4. API Endpoints:
   - Task:
      - [http://127.0.0.1:8000/api/task/](http://127.0.0.1:8000/api/task/) - Getting all the tasks pertaining to the logged in user.
      - [http://127.0.0.1:8000/api/task/1](http://127.0.0.1:8000/api/task) - Replace the number after /api/task - Updating, editing details of certain task

   - Label:
      - [http://127.0.0.1:8000/api/label/](http://127.0.0.1:8000/api/label/) - Getting all the label pertaining to the logged in user.
      - [http://127.0.0.1:8000/api/label/1](http://127.0.0.1:8000/api/label) - Replace the number after /api/label -  Updating, editing details of certain label

