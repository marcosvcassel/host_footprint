# Host footprint project

This is a learning project created to help me on my python learning journey, mixing security and python programming. The intention of this tool, when finished is to provide a complete footprint of a given domain or IP that contains:
* Dns records
    * get the domain name from parameters
    * get the filepath to record the findings from a paramater or assume registers.txt as a default
    * get the query types from a parameter
* Dns Subdomains
    * execute a sub-domains brute force
    * execute a sub-domains recon based on known words
* Whois information
* Open network ports and service banners
* Shodan banners
* Web Frameworks fingerprint if a web app
* SSL certificates dump and pasrsing
* Known vulnerabilities related to everything found in the list above

## Future features:
* Generate PDF and xls reports with the findings
* Store all this in a database
* Allow a db search form a minimalist web UI

## Open questions
* Ignoring venv files has any impact in the project? 
* Should I use requirements.txt intead and global libs in my system?
* What are the best practices in version control when using venv?

