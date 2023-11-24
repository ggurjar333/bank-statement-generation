# zywa-tech-round => Bank statement generation

As a developer, you are tasked with writing a set of services that will fulfill the following requirement: A user in our banking application will request a generation of a PDF file showing their transactions from date1 to date2.

The following are the base required services:
- A basic API that accepts a period of time (two dates) and the user's email address ID.
- A database service that collects the relevant transactions
- A PDF generation service that takes in the above data and generates a PDF of the transaction list
- An email service that sends the above PDF to the user's email address as an attachment

You can assume the following:
- The database can just be a CSV file. So the database call can just be reading the file and filtering for the relevant info. Assume the CSV to contain the following columns: `user_email`, `date_of_transaction`, `amount`
- The PDF generated can just have one table or just lines of text, with each line a valid transaction for the requested period.
- You can use any web API framework to expose the trigger API (date + email POST data) and it can be not authenticated (we do not care about authentication for this task)
- Each service can be written in any language of choice. Or even in a single server, but:
- None of the above services must interact directly with each other. They must only do their function and must not interfere with the process of the other services.
You can do so as a zip file containing the code, and a README.md outlining the solution to the question, why certain languages/frameworks were used, or other supporting information.

Bonus
- How would you go about adding authorization and authentication to this process? You can add a section in the README.md with your answer.
