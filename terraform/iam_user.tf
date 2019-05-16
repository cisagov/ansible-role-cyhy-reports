# The user being created
resource "aws_iam_user" "user" {
  name = "test-ansible-role-cyhy-reports"
  tags = "${var.tags}"
}

# The IAM access key for the user
resource "aws_iam_access_key" "key" {
  user = "${aws_iam_user.user.name}"
}

# The SSM parameters of interest
data "aws_ssm_parameter" "parameter" {
  count = "${length(var.ssm_parameters)}"

  name = "${var.ssm_parameters[count.index]}"
}

# IAM policy documents that allow reading the SSM parameters.  This
# will be applied to the IAM user we are creating.
data "aws_iam_policy_document" "ssm_parameter_doc" {
  count = "${length(var.ssm_parameters)}"

  statement {
    effect = "Allow"

    actions = [
      "ssm:GetParameters",
    ]

    resources = [
      "${data.aws_ssm_parameter.parameter.*.arn[count.index]}",
    ]
  }
}

# The SSM policies for our IAM user that lets the user read the SSM
# parameters.
resource "aws_iam_user_policy" "ssm_policy" {
  count = "${length(var.ssm_parameters)}"

  user   = "${aws_iam_user.user.id}"
  policy = "${data.aws_iam_policy_document.ssm_parameter_doc.*.json[count.index]}"
}
