# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-6-29
# Author Yo
# Email YoLoveLife@outlook.com

# OPS PUSH_MISSION
STATUS_PUSH_MISSION_LACK_OF_KEY_OR_JUMPER = -3
STATUS_PUSH_MISSION_UNREACHABLE = -2
STATUS_PUSH_MISSION_FAILED = -1
STATUS_PUSH_MISSION_WAIT_EXAM = 1
STATUS_PUSH_MISSION_WAIT_UPLOAD = 2
STATUS_PUSH_MISSION_WAIT_RUN = 3
STATUS_PUSH_MISSION_RUNNING = 4
STATUS_PUSH_MISSION_SUCCESS = 5
STATUS_PUSH_MISSION_IMPORT_VAR = 6
STATUS_PUSH_MISSION_IMPORT_TASKS = 7
STATUS_PUSH_MISSION_RERUN = 8

# SAFE WORK
STATUS_SAFEWORK_REJECT = -1
STATUS_SAFEWORK_WAIT_RUN = 1
STATUS_SAFEWORK_WAIT_DONE = 2
STATUS_SAFEWORK_DONE = 3

# HOST
STATUS_HOST_DENY_OR_REFUSE = -4
STATUS_HOST_NOT_SELECT = -3
STATUS_HOST_CLOSE = -2
# 此状态机器将不会参与到所有运维操作中
STATUS_HOST_PAUSE = -1
STATUS_HOST_CAN_BE_USE = 1
STATUS_HOST_DISK_SPACE_FULL = 2
STATUS_HOST_UPTIME_ERROR = 3
STATUS_HOST_DISK_INODE_FULL = 4

# GROUP
STATUS_GROUP_PAUSE = -2
STATUS_GROUP_UNREACHABLE = -1
STATUS_GROUP_CAN_BE_USE = 1

# JUMPER
STATUS_JUMPER_WRONG_KEY = -3
STATUS_JUMPER_NO_KEY = -2
STATUS_JUMPER_UNREACHABLE = -1
STATUS_JUMPER_CAN_BE_USE = 1

# EZSETUP STATUS
STATUS_EZSETUP_UNREACHABLE = -3
STATUS_EZSETUP_LACK_OF_KEY_OR_JUMPER = -2
STATUS_EZSETUP_ERROR = -1
STATUS_EZSETUP_INSTALLING = 1
STATUS_EZSETUP_DONE = 2

# CDN STATUS
STATUS_CDN_ERROR = -1
STATUS_CDN_RUN = 1
STATUS_CDN_DONE = 2


# CDN TYPE
TYPE_CDN_NONE = -1
TYPE_CDN_QN = 1
TYPE_CDN_WS = 2
TYPE_CDN_ALIYUN = 3

# EZSETUP TYPE
TYPE_EZSETUP_MYSQL = 1
TYPE_EZSETUP_REDIS = 2

# MONITOR TIME TYPE
TYPE_MONITOR_ONE_HOUR = 1
TYPE_MONITOR_SIX_HOUR = 2
TYPE_MONITOR_HALF_DAY = 3
TYPE_MONITOR_DAY = 4
TYPE_MONITOR_3_DAY = 5
TYPE_MONITOR_7_DAY = 6

# IP_POOL TYPE
TYPE_IP_POOL_ECS = 1
TYPE_IP_POOL_SLB = 2
TYPE_IP_POOL_DNAT = 3
TYPE_IP_POOL_SNAT = 4
TYPE_IP_POOL_WAF = 5
TYPE_IP_POOL_DDOS = 6


# DB INSTANCE
STATUS_DB_INSTANCE_CONNECT_REFUSE = -3
STATUS_DB_INSTANCE_PASSWORD_WRONG = -2
STATUS_DB_INSTANCE_UNREACHABLE = -1
STATUS_DB_INSTANCE_CAN_BE_USE = 1

# DB TYPE
TYPE_DB_INSTANCE_MASTER = 1
TYPE_DB_INSTANCE_SLAVE = 2
TYPE_DB_INSTANCE_MGR = 3

# SLOT TYPE
TYPE_SLOT_EXPIRE = 1
TYPE_SLOT_INSPECT = 2

# TIMELINE
TIMELINE_KEY_VALUE = {
    # HOST
    'Host_HOST_CREATE':10,
    'Host_HOST_UPDATE':11,
    'Host_HOST_DELETE':12,
    'Host_HOST_SORT':13,
    'Host_HOST_PASSWORD':14,
    # Group
    'Group_GROUP_CREATE':20,
    'Group_GROUP_UPDATE':21,
    'Group_GROUP_DELETE':22,
    'Group_GROUP_SORT':23,
    # User
    'ExtendUser_USER_CREATE': 30,
    'ExtendUser_USER_UPDATE': 31,
    'ExtendUser_USER_DELETE': 32,
    'ExtendUser_USER_QRCODE': 33,
    # PMNGROUP
    'Permission_PMNGROUP_CREATE': 40,
    'Permission_PMNGROUP_UPDATE': 41,
    'Permission_PMNGROUP_DELETE': 42,
    # KEY
    'Key_KEY_CREATE': 50,
    'Key_KEY_UPDATE': 51,
    'Key_KEY_DELETE': 52,
    # JUMPER
    'Jumper_JUMPER_CREATE': 60,
    'Jumper_JUMPER_UPDATE': 61,
    'Jumper_JUMPER_DELETE': 62,
    'Jumper_JUMPER_FLUSH': 63,
    # META
    'META_META_CREATE': 70,
    'META_META_UPDATE': 71,
    'META_META_DELETE': 72,
    # MISSION
    'Mission_MISSION_CREATE': 80,
    'Mission_MISSION_UPDATE': 81,
    'Mission_MISSION_DELETE': 82,
    'Quick_QUICK_CREATE': 83,
    # VAR
    'Var2Group_VAR_CREATE': 90,
    'Var2Group_VAR_UPDATE': 91,
    'Var2Group_VAR_DELETE': 92,
    # CODE WORK
    'Code_Work_CODEWORK_CREATE': 100,
    'Code_Work_CODEWORK_EXAM': 101,
    'Code_Work_CODEWORK_CHECK': 102,
    'Code_Work_CODEWORK_UPLOAD': 103,
    'Code_Work_CODEWORK_RUN': 104,
    'Code_Work_CODEWORK_DELETE': 105,
    'Code_Work_CODEWORK_RESULTS': 106,
    # FILE
    'FILE_UTILS_FILE_CREATE': 110,
    'FILE_UTILS_FILE_UPDATE': 111,
    'FILE_UTILS_FILE_DELETE': 112,
    # IMAGE
    'IMAGE_UTILS_IMAGE_CREATE': 112,
    'IMAGE_UTILS_IMAGE_DELETE': 113,
    # LOGIN
    'None_LOGIN': 120,
    # EZSETUP
    'SETUP_REDIS_CREATE': 130,
    'SETUP_NGINX_CREATE': 131,
    # YoCDN
    'CDN_CDN_CREATE': 140,
}

# TIMELINE_VALUE_KEY = {v: k for k, v in TIMELINE_KEY_VALUE.items()}