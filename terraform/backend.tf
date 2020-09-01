terraform {
  backend "s3" {
    bucket         = "ncats-terraform-state-storage"
    dynamodb_table = "terraform-state-lock"
    encrypt        = true
    key            = "ansible-role-cyhy-reports/terraform.tfstate"
    region         = "us-east-1"
  }
}
