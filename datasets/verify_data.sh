#! /bin/bash
DATASET_NAME="$1"
SHA1SUM_LIST_EXPECTED="$2"

SYNDICATEFS_DATASET_MOUNT_DIR=/opt/dataset/${DATASET_NAME}

# LIST FILES
echo "Listing files..."
SHA1SUM_LIST="$(ls -1 ${SYNDICATEFS_DATASET_MOUNT_DIR} | sha1sum | awk '{print $1}')"
echo $SHA1SUM_LIST
if [ "$SHA1SUM_LIST" != $SHA1SUM_LIST_EXPECTED ]; then
    echo "The file list is not same as expected!"
    echo "Expected: $SHA1SUM_LIST_EXPECTED"
    echo "Returned: $SHA1SUM_LIST"
    exit 1
fi

echo "Checking a dataset $DATASET_NAME... Done!"
