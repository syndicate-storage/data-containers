#! /bin/bash
MS_HOST="$1"
USER="$2"
DATASET_VOLUME="$3"
READER_UG_NAME="$4"
DATASET_NAME="$5"

USER_ARR=(`echo ${USER} | tr '@' ' '`)
USER_NAME=${USER_ARR[0]}

PRIVATE_MOUNT_DIR=/opt/private
SYNDICATEFS_DATASET_MOUNT_DIR=/opt/dataset/${DATASET_NAME}

# REGISTER SYNDICATE
echo "Registering Syndicate..."
syndicate -d --trust_public_key setup ${USER} ${PRIVATE_MOUNT_DIR}/${USER}.pkey ${MS_HOST}
syndicate -d reload_user_cert ${USER}
syndicate -d reload_volume_cert ${DATASET_VOLUME}
syndicate -d reload_gateway_cert ${READER_UG_NAME}
echo "Registering Syndicate... Done!"


# MOUNT ANONYMOUS UG
echo "Mounting an anonymous UG..."
sudo mkdir -p ${SYNDICATEFS_DATASET_MOUNT_DIR}
sudo chown -R syndicate:syndicate ${SYNDICATEFS_DATASET_MOUNT_DIR}
sudo chmod -R 744 ${SYNDICATEFS_DATASET_MOUNT_DIR}

syndicatefs -f -u ANONYMOUS -v ${DATASET_VOLUME} -g ${READER_UG_NAME} -d3 ${SYNDICATEFS_DATASET_MOUNT_DIR} &> /tmp/syndicate_ug_read.log&
waitfusemount.py syndicatefs ${SYNDICATEFS_DATASET_MOUNT_DIR} 30
if [ $? -ne 0 ]; then
    echo "Mounting an anonymous UG... Failed"
    exit 1
fi
echo "Mounting an anonymous UG... Done!"

/bin/bash
