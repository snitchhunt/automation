# Data Ingestion Scripts

## Usage

These are Logstash filter configuration files. Logstash can, using these configurations, read lines from input files, and spit them into ElasticSearch.

To use them:

 - install Logstash (`brew install logstash` on macOS)
 - update the .conf input file paths and output ElasticSearch URLs
 - for each dataset:
     + run logstash (e.g. `logstash -f phone_metadata_log.csv`) to upload the data to ElasticSearch.
     + create an _Index Pattern_ in Kibana (via the Management panel) for the dataset, e.g. `logstash-phone_metadata_*`
     + the logstash process won't exit. You'll know it's done when it stops printing to the console, and you can double check by selecting the Index Pattern in Kibana and checking that the number of hits found there matches the number of lines in the csv file.
