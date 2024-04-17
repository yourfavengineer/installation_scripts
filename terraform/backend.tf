terraform {
  backend "s3" {
    bucket = "terraform-project-bucket-007"
    key    = "terraform/backend"
    region = "us-east-1"
  }
}
