variable "region" {
  description = "The AWS region to create all the infrastructure in"
  default = "ap-southeast-2"
}

provider "aws" {
  region = "${var.region}"
}

#terraform {
#  backend "s3" {
    # Empty config here because each organisation will configure its own remote state
#  }
#}

resource "aws_elasticsearch_domain" "es" {
  domain_name           = "tf-pam-test"
  elasticsearch_version = "5.3"
  cluster_config {
    instance_type = "t2.small.elasticsearch"
  }

  advanced_options {
    "rest.action.multi.allow_explicit_index" = "true"
  }

  access_policies = <<CONFIG
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "es:*",
            "Principal": "*",
            "Effect": "Allow",
            "Condition": {
                "IpAddress": {"aws:SourceIp": ["66.193.100.22/32"]}
            }
        }
    ]
}
CONFIG
  ebs_options {
    ebs_enabled = true
    volume_size = 10
    volume_type = "gp2"
  }

  snapshot_options {
    automated_snapshot_start_hour = 23
  }

  tags {
    Domain = "tf-pam-test"
  }
}
