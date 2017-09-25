# Data Ingestion Scripts

## Usage

These are Logstash filter configuration files. Logstash can, using these configurations, read lines from input files, and spit them into ElasticSearch.

To use them you'll need to update the .conf input file paths and output ElasticSearch URLs, then run `./import.sh` or `logstash -f <filename.conf>` if you want to ingest one dataset at a time.

See: https://www.elastic.co/guide/en/logstash/current/config-examples.html
