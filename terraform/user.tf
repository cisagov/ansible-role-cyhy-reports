# Create the test user
module "user" {
  source = "github.com/cisagov/molecule-iam-user-tf-module"

  providers = {
    aws                                    = aws
    aws.images-production-provisionaccount = aws
    aws.images-staging-provisionaccount    = aws
    aws.images-production-ssm              = aws
    aws.images-staging-ssm                 = aws
  }

  entity         = "ansible-role-cyhy-reports"
  ssm_parameters = ["/cyhy/core/geoip/license_key"]

  tags = var.tags
}
