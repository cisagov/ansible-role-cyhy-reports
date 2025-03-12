# Create the test user
module "user" {
  source = "github.com/cisagov/molecule-iam-user-tf-module"

  providers = {
    aws                         = aws.users
    aws.images-provisionaccount = aws.images_provisionaccount
    aws.images-ssm              = aws.images_ssm
  }

  entity = "ansible-role-cyhy-reports"
  ssm_parameters = [
    "/cyhy/core/geoip/account_id",
    "/cyhy/core/geoip/license_key",
  ]
}
