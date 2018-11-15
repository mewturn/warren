# Data Processing
Data Processing (Offline) version of Warren NMT, API-compatible.

## Requirements (suggest to use pip to install, or run requirements.sh)
* jieba>=0.39
* opencc-python-reimplemented>=0.1.4
 
## Alignment  
Contains file using the alignment process  
* `build_probability.py` : Builds transition probabilities to be used as reference for potential word sequence to be included into the jieba dictionary.
* `create_sql.py` : Create SQL query file with two parallel files (useful for exceptionally large corpus files)
* `segment.py` : Segments Chinese text using custom jieba dictionary
* `smush.py` : Reassembles sentences with a rule-based method
* `smushChinese.py` : Removes spaces between Chinese characters and converts from Simplified Chinese to Traditional Chinese (if needed)
* `split.py` : Split a bilingual text (English and Chinese in the same file) into one English file and one Chinese file (with limitations)  
  
## Downloaders
Contains grabbers and downloaders for different websites  
  
## Parsers
Contains parsers for different document types
  
## Processing  
Other processing scripts
* `askWarren.py` : Reads content of a file and obtains translations from Warren (need to run Warren on GCP server first)  
* `extractText-doc.py` : Extracts text from every DOC file in the directory
* `extractText.py` : Extracts text from every PDF file in the directory
* `google_translate.py` : Reads content of a file and obtains translation from Google (need to insert Google key here)
* `removeHTML.py` : Removes HTML content from a file (suggest to use bs4 instead)
* `removepunctuations.py` : Removes punctuation from a file
* `similarity.py` : Checks the Levenshtein distance between translations