#!/bin/bash
#
# Perform the partition and format of disks except the OS disk
# Created by zifengw

# filesystem type to be formatted
FS_TYPE=ext4

# Partition and format disks by parted
partition_format_disks() {
  parted -s $1 mklabel gpt 1>/dev/null 2>&1
  parted -s $1 mkpart primary ${FS_TYPE} 0% 100% 1>/dev/null 2>&1
  if [[ $? = 0 ]]; then
    sleep $(($RANDOM%10))s
    echo $1 >> /tmp/partfinish
    P_FINISH_NUM=$(cat /tmp/partfinish | wc -l)
    echo -e "Parted $1 finished ,$P_FINISH_NUM disks Parted, Format disk $1... "
    mkfs.${FS_TYPE} -q -i 8192 -b 4096 ${1}1 1>/dev/null 2>&1
    if [[ $? = 0 ]]; then
      sleep $(($RANDOM%10))s
      echo $1 >> /tmp/formatfinish
      F_FINISH_NUM=$(cat /tmp/formatfinish | wc -l)
      echo -e "Format $1 finished ,$F_FINISH_NUM disks format "
      return 0
    else
      sleep $(($RANDOM%10))s
      echo $1 >> /tmp/formatfail
      F_FAIL_NUM=$(cat /tmp/formatfail | wc -l)
      echo -e "Format $1 failed ,$F_FAIL_NUM disks format failed "
      return 1
    fi
  else
    sleep $(($RANDOM%10))s
    echo $1 >> /tmp/partfail
    P_FAIL_NUM=$(cat /tmp/partfail | wc -l)
    echo -e "Parted $1 failed ,$P_FAIL_NUM disks parted failed "
    return 2
  fi
}

# main "$@"
SYS_DISK=$(df -hT 2> /dev/null | awk '$7 == "/" {print $1}' | awk -F [0-9] '{print $1}')
DISK_LIST=$(fdisk -l 2> /dev/null | grep dev | awk -F [:\ ] '$1 ~/Disk/ {print $2}' | sort)
DATA_DISKS=""
for i in $DISK_LIST; do
  if [[ $i == $SYS_DISK ]]; then
    DATA_DISKS=${DATA_DISKS}
  else
    DATA_DISKS="${DATA_DISKS} ${i}"
  fi
done

# Check if any data disk exists.
if [[ -z $DATA_DISKS ]]; then
  echo -e "Only system disk found, None data disks "
  exit 1
else
  sleep 1s
fi

# Check and confirm the SYS_DISK
echo -e "\n"
df -hT 2> /dev/null | grep $SYS_DISK | sort
echo -e "System disk is $SYS_DISK ,right?(Y/N) "
read INPUT
while [[ "${INPUT}a" != "Ya" && "${INPUT}a" != "ya" ]]; do
  if [[ "${INPUT}a" = "Na" || "${INPUT}a" = "na" ]]; then
    echo -e "please check your input again."
    exit 1
  else
    echo -e "please input (Y/N) "
    read INPUT
  fi
done

# Check and confirm DATA_DISKS
DATA_DISK_NUM=$(echo $DATA_DISKS | wc -w)
echo $DATA_DISKS
echo -e "All $DATA_DISK_NUM data disk is here, right?(Y/N) "
read INPUT
while [[ "${INPUT}a" != "Ya" && "${INPUT}a" != "ya" ]]; do
  if [[ "${INPUT}a" = "Na" || "${INPUT}a" = "na" ]]; then
    echo -e "please check your input again. "
    exit 1
  else
    echo -e "please input (Y/N) "
    read INPUT
  fi
done

# Confirm the disk to be formatted
echo -e "ALL the Data Disk will be Parted and Formated! Are you sure to do so? (Y/N) "
read INPUT 
while [[ "${INPUT}a" != "Ya" && "${INPUT}a" != "ya" ]]; do
  if [[ "${INPUT}a" = "Na" || "${INPUT}a" = "na" ]]; then
    echo -e "please check your input again."
    exit 1
  else
    echo -e "please input (Y/N) "
    read INPUT
  fi
done

# Formating Processing
rm -rf /tmp/partfinish /tmp/partfail /tmp/formatfinish /tmp/formatfail
touch /tmp/partfinish /tmp/partfail /tmp/formatfinish /tmp/formatfail
diskcount=0
for DISK in $DATA_DISKS; do
  if [[ $((${diskcount}%100)) -eq 0 ]]; then
    wait
    dd if=/dev/zero of=$DISK bs=4M count=1 1>/dev/null 2>&1
    partition_disks $DISK &
    ((diskcount++))
  else
    dd if=/dev/zero of=$DISK bs=4M count=1 1>/dev/null 2>&1
    partition_disks $DISK &
    ((diskcount++))
  fi
done
wait

