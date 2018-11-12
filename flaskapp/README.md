# Flask App
Flask version of Warren NMT, API-compatible.

## Requirements (suggest to use pip to install, or run requirements.sh)
* flask>=1.0.2
* jieba>=0.39
* opencc-python-reimplemented>=0.1.4
* mysql-connector-python>=8.0.12
* virtualenv>=15.0.1
 
## How to host the web translation engine on GCP / AWS EC2
1. Clone the repository  
`git clone https://github.com/topadmit/warren/`  
  
2. Change directory to the web translation and create a virtual environment named `venv` (you can change the name as you wish)  
`cd path/to/warren`  
`virtualenv venv`  
  
3. Run the virtual environment  
`source venv/bin/activate`  

4. Install requirements
Suggestion: Run the shell script in the main folder  
`cd path/to/warren`  
`chmod +x ./requirements.sh`  
`sudo bash ./requirements.sh`  
  
5. Set up mySQL on Google Cloud 
`sudo apt-get update`  
`sudo apt-get -y install mysql-server`  
`sudo mysql_secure_installation` (Follow the steps in the console)  
  
6. Set up the local database and tables  (Important: Check database name and credentials and modify `queries.py` or `options.cnf` with the correct details. Replace `username` and `password` with the credentials you want.)  
`sudo mysql -u root -p`  
`mysql> GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' IDENTIFIED BY 'password';`  
`mysql> CREATE DATABASE warren;`  
`mysql> CREATE TABLE suggestion(id INT AUTO_INCREMENT, en text, zh_hant text, rating tinyint(4), en_modified text, PRIMARY KEY (id));`
