# Configure AWS
provider "aws" {
  region = "us-east-1"
}

module "iam_user" {
  source = "github.com/cisagov/molecule-packer-travisci-iam-user-tf-module"

  ssm_parameters = ["/github/oauth_token"]
  user_name      = "test-ansible-role-cyhy-reports"
  tags = {
    Team        = "NCATS OIS - Development"
    Application = "ansible-role-cyhy-reports testing"
  }
}
