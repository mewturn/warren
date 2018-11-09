# Warren NMT Engine
Developed by Milton  
A Chinese-to-English machine translation engine, built upon OpenNMT: http://opennmt.net/  
This repository contains both the training preparation (e.g. data collection, data processing and machine learning) and the web interface used to display the output (coupled with the API).  
  
Web Translation Engine: flaskapp/
Data Processing and Machine Learning: training/

## Requirements (suggest to use pip to install, or run requirements.sh)
* Flask>=1.0.2
* jieba>=0.39
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
Either: Run the shell script in the main folder  
`cd path/to/warren`  
`chmod +x ./install.sh`
