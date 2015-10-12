Please create a REST API server using Django and any other third-party packages (e.g. django-rest-framework).

You should create the following models

Fund
- `bank_account_number`: string representing the bank account associated with this fund
- `companies`: a list of companies associated with this fund
- `is_single_asset`: a boolean representing whether this fund has one or multiple companies
- `legal_name`: string representing the legal name of the fund
- `llc`: the Llc associated with this fund

Company
- `display_name`: the name of the company

Llc
- `created_at`: a DateTime object when the Llc was created
- `dissolved`: a boolean on whether the Llc has been dissolved
- `legal_name`: the legal name of the Llc

You should allow for the creation, retrieval, update, and deletion of all of the models
You should allow for an endpoint that displays all the funds a company is part of
You should allow for an endpoint that displays all the funds an Llc is a part of

Please limit yourself to 4 hours of work.  If you have extra time, you may also do any of the following

- create a frontend for the API server
- add permissions
- push the codebase to heroku and run it as a live site
- anything else

When you have finished, push your code to Github, and e-mail back the repository link.  We expect this to take you a week, but if you need more time, please reach out and let me know.
