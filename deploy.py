#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cdn.v20180606 import cdn_client, models

if __name__ == '__main__':
    os.system('npx hexo clean && npx hexo g')

    BLOG_SERVER_IP = os.getenv('BLOG_SERVER_IP')
    BLOG_SERVER_PORT = os.getenv('BLOG_SERVER_PORT')
    BLOG_SERVER_LOGIN_USER = os.getenv('BLOG_SERVER_LOGIN_USER')
    BLOG_SERVER_LOGIN_PASS = os.getenv('BLOG_SERVER_LOGIN_PASS')
    BLOG_UPLOAD_DIR = os.getenv('BLOG_UPLOAD_DIR')
    BLOG_SERVER_DIR = os.getenv('BLOG_SERVER_DIR')

    BLOG_DOMAIN = os.getenv('BLOG_DOMAIN')
    CDN_SECRET_ID = os.getenv('CDN_SECRET_ID')
    CDN_SECRET_KEY = os.getenv('CDN_SECRET_KEY')

    cmd = f'rsync -e \"ssh -i {BLOG_SERVER_LOGIN_PASS} -p {BLOG_SERVER_PORT}\" -avz --delete {BLOG_UPLOAD_DIR} {BLOG_SERVER_LOGIN_USER}@{BLOG_SERVER_IP}:{BLOG_SERVER_DIR}'
    os.system(cmd)

    try:
        cred = credential.Credential(CDN_SECRET_ID, CDN_SECRET_KEY)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cdn.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = cdn_client.CdnClient(cred, "", clientProfile)

        req = models.PurgePathCacheRequest()
        params = {"Paths": [BLOG_DOMAIN], "FlushType": "flush"}
        req.from_json_string(json.dumps(params))

        resp = client.PurgePathCache(req)
        print(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)
