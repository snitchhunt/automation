variable "region" {
  description = "The AWS region to create all the infrastructure in"
  default = "ap-southeast-2"
}

provider "aws" {
  region = "${var.region}"
}

resource "aws_s3_bucket" "b" {
  bucket = "tw-etang-snitchhunt-testbucket1"
  acl = "private"

  tags {
    Name = "My Test Bucket"
    Environment = "Dev"
  }
}
