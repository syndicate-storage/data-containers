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
SYNDICATE_CONFIG_DIR=~/.syndicate_anonymous/${DATASET_NAME}/syndicate.conf

SYNDICATE_CMD="syndicate -d -c ${SYNDICATE_CONFIG_DIR}"
SYNDICATEFS_CMD="syndicatefs -d3 -c ${SYNDICATE_CONFIG_DIR}"

# REGISTER SYNDICATE
echo "Registering Syndicate..."
${SYNDICATE_CMD} --trust_public_key setup ${USER} ${PRIVATE_MOUNT_DIR}/${USER}.pkey ${MS_HOST}
if [ $? -ne 0 ]; then
    echo "Registering Syndicate... Failed"
    exit 1
fi
${SYNDICATE_CMD} reload_user_cert ${USER}
${SYNDICATE_CMD} reload_volume_cert ${DATASET_VOLUME}
${SYNDICATE_CMD} reload_gateway_cert ${READER_UG_NAME}
echo "Registering Syndicate... Done!"


# MOUNT ANONYMOUS UG
echo "Mounting an anonymous UG..."
sudo mkdir -p ${SYNDICATEFS_DATASET_MOUNT_DIR}
sudo chown -R syndicate:syndicate ${SYNDICATEFS_DATASET_MOUNT_DIR}
sudo chmod -R 744 ${SYNDICATEFS_DATASET_MOUNT_DIR}

${SYNDICATEFS_CMD} -f -u ANONYMOUS -v ${DATASET_VOLUME} -g ${READER_UG_NAME} ${SYNDICATEFS_DATASET_MOUNT_DIR} &> /tmp/syndicate_${DATASET_NAME}.log&
waitfusemount.py syndicatefs ${SYNDICATEFS_DATASET_MOUNT_DIR} 30
if [ $? -ne 0 ]; then
    echo "Mounting an anonymous UG... Failed"
    echo "> This can be due to an insufficient permission to run FUSE"
    echo "> If you are in a docker container, rerun the container with following command line options: "
    echo "> docker run -ti --cap-add SYS_ADMIN --device /dev/fuse --privileged <docker-image>"
    exit 1
fi
echo "Mounting an anonymous UG... Done!"

/bin/bash
