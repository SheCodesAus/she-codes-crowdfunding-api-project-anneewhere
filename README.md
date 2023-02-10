# Paw2Paw Crowdfunding Project
​
This is a crowdfunding page for pets that are in dire need of funding to replace, restore or fix damaged household items. Other pets can band together
to help replace items/furniture. This way, we decrease the amount of humans angry and lower the risk of getting rehomed. It's a win-win situation. 
​
## Features
- Ability to filter by owner, open date
- Ability to reset password
- Ability to maintain anonyminity when pledging

### User Accounts
​
- [X] Username: admin
- [X] Email Address: admin@admin.com
- [X] Password: admin
​
- [X] Username: testuser1
- [X] Email Address: testuser1@gmail.com
- [X] Password: testuser1
​
- [X] Username: Sherry
- [X] Email Address: sherry@gmail.com
- [X] Password: Sherry1234

### Project
​
- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Target Amount to Fundraise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
- [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge
  
### Implement suitable update delete
​
**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**
​
- Project
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy
- Pledge
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy
- User
  - [X] Create
  - [X] Retrieve
  - [ ] Update
  - [ ] Destroy
​
### Implement suitable permissions
​
**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**
​
- Project
  - [ ] Limit who can create
  - [ ] Limit who can retrieve
  - [X] Limit who can update
  - [X] Limit who can delete
- Pledge
  - [ ] Limit who can create
  - [ ] Limit who can retrieve
  - [X] Limit who can update
  - [X] Limit who can delete
- User
  - [ ] Limit who can retrieve
  - [X] Limit who can update
  - [ ] Limit who can delete
​
### Implement relevant status codes
​
- [X] Get returns 200
- [X] Create returns 201
- [X] Not found returns 404
​
### Handle failed requests gracefully 
​
- [X] 404 response returns JSON rather than text
​
### Use token authentication
​
- [X] implement /api-token-auth/
​
## Additional features
​
- [X] Filter
​
Projects can be filtered by the owner and whether it is open or not. Supporters can always be filtered as well. 
​
​
- [X] Ability to reset password
​
users can update their password by submitting their old and new password. 
​
​
- [X] Ability to maintain anonyminity when pledging
​
Supporters can pledge anonymously but still update their pledges. 
​
### External libraries used
​
- [X] django-filter
​
​
## Part A Submission
​
- [X] A link to the deployed project: lingering-cherry-4280.fly.dev
- [X] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [X] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [X] A screenshot of Insomnia, demonstrating a token being returned.
- [X] Your refined API specification and Database Schema.
​
### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
​
1. Create User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/users/ \
  --header 'Authorization: Token a91e4fb85481342109c5d0a8b7a85d597d2ac239' \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "testuser1",
	"first_name": "testuser1",
	"last_name": "testuser1",
	"email": "testuser1@gmail.com",
	"password": "testuser123"
}'
```
​
2. Sign in User
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/api-token-auth/ \
  --header 'Authorization: Bearer undefined' \
  --header 'Content-Type: application/json' \
  --data '{
	"username":"admin",
	"password":"admin"
}'
```
​
3. Create Project
​
```shell
curl --request POST \
  --url http://127.0.0.1:8000/projects/ \
  --header 'Authorization: Token a91e4fb85481342109c5d0a8b7a85d597d2ac239' \
  --header 'Content-Type: application/json' \
  --data '{
	"title": "Merit Ferrets",
	"description": "I need a ferret in my life. Please help fund one for me!",
	"goal": 70,
	"image": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Dollar_bill_and_small_change.jpg",
	"is_open": true,
	"date_created": "2023-01-29T06:21:39.771Z"
}'
```
