#!/usr/bin/env bash
#
# Managed by cisagov/ansible-role-cyhy-reports.

set -o errexit
set -o nounset
set -o pipefail

CYHY_DATA_MOUNTPOINT="{{ cyhy_reports_data_mountpoint }}"
CYHY_DATA_MAX_USAGE="{{ cyhy_reports_data_max_usage }}"

# Verify that the disk usage of the device corresponding to the
# specified mountpoint is less than the specified percentage
#
# Arguments:
#   $1: The mountpoint (e.g., /mnt)
#   $2: The maximum acceptable usage percentage (e.g., 90)
#
# Returns:
#   0: If the actual disk usage percentage is less than or equal to
#   the specified maximum acceptable usage percentage
#   1: Otherwise
function check_disk_space {
  local mountpoint=$1
  local max_percent_usage=$2

  local device
  device=$(findmnt --mountpoint "${mountpoint}" --noheadings --output=SOURCE)

  percent_usage=$(df --output=source,pcent \
    | sed --quiet "s/^${device//\//\\/}[[:blank:]]*\([[:digit:]]\+\)%/\1/p")
  [[ percent_usage -le max_percent_usage ]]
  return $?
}

return_value=1
if check_disk_space "$CYHY_DATA_MOUNTPOINT" "$CYHY_DATA_MAX_USAGE"; then
  echo Genertating Cyber Hygiene reports...
  cd "$CYHY_DATA_MOUNTPOINT/.."
  sudo --user=cyhy ./create_snapshots_reports_scorecard.py --no-dock cyhy scan \
    2>&1 \
    | /usr/bin/logger --tag cyhy-reports
  return_value=$?
  cd "$OLDPWD"
else
  echo Insufficient disk space at "$CYHY_DATA_MOUNTPOINT" to run Cyber Hygiene reports.
fi

exit $return_value
