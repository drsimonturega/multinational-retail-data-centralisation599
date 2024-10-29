# multinational-retail-data-centralisation599

## A description of the project: what it does, the aim of the project, and what you learned
You work for a multinational company that sells various goods across the globe.

Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team.

In an effort to become more data-driven, your organisation would like to make its sales data accessible from one centralised location.

Your first goal will be to produce a system that stores the current company data in a database so that it's accessed from one centralised location and acts as a single source of truth for sales data.

You will then query the database to get up-to-date metrics for the business.

### Refactoring code
All retriived data frames were renamed to ```df_tran``` ready to be added to refactored data cleaning code. Data cleaning was refactored eliminate code duplication with a clean_na_in_data() function.

 ![Alt](/clean_na.png "clean_na_in_data()")

A ```if __name__ == "__main__":``` statement was added, to make the fuctions with in accessabe and tidy up code. Diagnostic print staments were removed. the use of self was minimised to varibles that are unique to each class instance and shared between functions.

## Installation instructions
DB set-up data was exctracted and cleaned.

A star-based schema was constructed.
## Usage instructions
add queries
## File structure of the project
jyper note books

SQL scripts
## License information

This is availible through a GNU General Public License, version 3.
