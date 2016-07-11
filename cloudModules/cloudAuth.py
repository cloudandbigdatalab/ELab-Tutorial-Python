# -*- coding: utf-8 -*-
import configuration.globalVars as globalVars
import requests
import json


def auth():
    #url = 'http://129.114.110.198:5000/v2.0/tokens'
    url = globalVars.authURL
    
    body = {"auth" : 
               {"tenantName": "admin",
                "passwordCredentials": 
                   {"username": "admin",
                    "password": "password"}}}
                        
    json_body = json.dumps(body)

    r = requests.post(url, json_body)
    #print json.dumps(body, indent=4)
    #print json.dumps(r.json(), indent=4)
    globalVars.tenant_id += r.json()['access']['token']['tenant']['id']
    token_id = r.json()['access']['token']['id']
    return token_id

def createTenant(token_id):
    url =  'http://129.114.110.198:35357/v2.0/tenants'
	
    body = {"tenant": 
				{"name": "ACME corp 3",
				 "description": "A description ...",
				 "enabled": True}}

    my_headers = {"X-Auth-Token": token_id}
    json_body = json.dumps(body)

    r = requests.post(url, json_body, headers=my_headers)
    print json.dumps(r.json(), indent=4)
    #print r

def createRole(token_id):
    url =  'http://129.114.110.198:35357/v2.0/OS-KSADM/roles'
	
    body = {
			"role": {
			"id": "12332",
			"name": "Guest2",
			"description": "Guest Access2",
			"tenantId": "bc6d6ffacb284cf4ae8b7688974d2b53"}}

    my_headers = {"X-Auth-Token": token_id}
    json_body = json.dumps(body)

    r = requests.post(url, json_body, headers=my_headers)
    print json.dumps(r.json(), indent=4)

def createUser(token_id):
    url =  'http://129.114.110.198:35357/v2.0/users'
	
    body = {
    "user": {
        "name": "jqsmith2",
        "email": "john2.smith@example.org",
        "enabled": True,
		"tenantId": "bc6d6ffacb284cf4ae8b7688974d2b53",
        "OS-KSADM:password": "word"
    }
}

    my_headers = {"X-Auth-Token": token_id}
    json_body = json.dumps(body)

    r = requests.post(url, json_body, headers=my_headers)
    print json.dumps(r.json(), indent=4)
	
def grantRole(token_id):
    url ="http://129.114.110.198:35357/v2.0/tenants/bc6d6ffacb284cf4ae8b7688974d2b53/users/​1a80e968da744473909fd6785b21467d/roles/OS-KSADM/3390bb2982144e7999dbb3691d61884a"
    my_headers = {"X-Auth-Token": token_id}
    #json_body = json.dumps(body)

    r = requests.put(url,headers=my_headers)
    print json.dumps(r.json(), indent=4)
    #print url

def listUsers(token_id):
    url =  'http://129.114.110.198:35357/v2.0/users'
	
    my_headers = {"X-Auth-Token": token_id}
    #json_body = json.dumps(body)

    r = requests.get(url,headers=my_headers)
    print json.dumps(r.json(), indent=4)
    #print r

def listTenants(token_id):
    url =  'http://129.114.110.198:35357/v2.0/tenants'
	
    my_headers = {"X-Auth-Token": token_id}
    #json_body = json.dumps(body)

    r = requests.get(url,headers=my_headers)
    print json.dumps(r.json(), indent=4)
    #print r
	
def listRoles(token_id):
    url =  'http://129.114.110.198:35357/v2.0/OS-KSADM/roles'
	
    my_headers = {"X-Auth-Token": token_id}
    #json_body = json.dumps(body)

    r = requests.get(url,headers=my_headers)
    print json.dumps(r.json(), indent=4)
    #print r
	
def listUsersOnTenant(token_id):
    url =  'http://129.114.110.198:35357/v2.0/tenants/bc6d6ffacb284cf4ae8b7688974d2b53/users'
	
    my_headers = {"X-Auth-Token": token_id}
    #json_body = json.dumps(body)

    r = requests.get(url,headers=my_headers)
    print json.dumps(r.json(), indent=4)
    #print r


	
