#!/bin/sh

logstash -f import_email_metadata_log.conf
logstash -f import_google_query_log.conf
logstash -f import_phone_metadata_log.conf
logstash -f import_phone_subscriber_info.conf
