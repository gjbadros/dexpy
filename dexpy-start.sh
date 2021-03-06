#!/bin/bash
/usr/bin/python2 dexpy.py \
        --DEXCOM-SHARE-SERVER $DEXCOM_SHARE_SERVER \
        --DEXCOM-SHARE-USERNAME $DEXCOM_SHARE_USERNAME \
        --DEXCOM-SHARE-PASSWORD $DEXCOM_SHARE_PASSWORD \
        --MQTT-SERVER $MQTT_SERVER \
        --MQTT-PORT $MQTT_PORT \
        --MQTT-SSL $MQTT_SSL \
        --MQTT-CLIENTID $MQTT_CLIENTID \
        --MQTT-TOPIC $MQTT_TOPIC \
        --INFLUXDB-SERVER $INFLUXDB_SERVER \
        --INFLUXDB-PORT $INFLUXDB_PORT \
        --INFLUXDB-SSL $INFLUXDB_SSL \
        --INFLUXDB-USERNAME $INFLUXDB_USERNAME \
        --INFLUXDB-PASSWORD $INFLUXDB_PASSWORD \
        --INFLUXDB-DATABASE $INFLUXDB_DATABASE \
        --NIGHTSCOUT-URL $NIGHTSCOUT_URL \
        --NIGHTSCOUT-SECRET $NIGHTSCOUT_SECRET \
        --NIGHTSCOUT-TOKEN $NIGHTSCOUT_TOKEN \
        --LOG-LEVEL $LOG_LEVEL
