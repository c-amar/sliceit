Problem Statement:
======================

Code an application server with the following endpoints.

/internal -> responds with text response "internal"
/external -> responds with text response "external"
/cached -> responds with text response "cached"

Front this application server with Nginx. In Nginx, add the following rules for the endpoints.

/cached should be cached(use Nginx caching, not external caches like Redis or Memcached).
/internal should be accessible only from specific IP addresses.
/external should be accessible to the general public.

You have to deploy the application server in one machine and Nginx in another. Automate the provisioning of both these servers using Ansible(or some other parallel framework).

Solution:
======================
The application is coded in python3 using django framework. I have used gunicorn as the application server. Deployment is automated using a simple ansible playbook.

**Requirements/ Assumptions**
1. Two servers with centOS.
2. Ansible server 

***This no longer works. Use method mentioned in the second assignment section**
**Deployment**
1. Use `git clone https://github.com/c-amar/sliceit.git` to clone the repo
2. Edit the ansible/vars/var.yml and add the following details:

internal_ips: list of internal IPs  
nginx_bind_ip: 'IP to bind nginx'  
app_bind_ip: 'IP to bind app'  

Example:
```yml
internal_ips: ['192.168.99.1','192.168.99.2','192.168.99.3']
nginx_bind_ip: '192.168.99.101'
app_bind_ip: '192.168.99.102'
```
3. Edit ansible/hosts file and add ips/hostname for the app server and nginx server in appropriate section. 
Example:
```ini
[nginx_server]
192.168.99.101

[app_server]
192.168.99.102
```
4. Run the ansible playbook ansible/deploy.yml  
`cd ansible && ansible-playbook deploy.yml -i hosts -u my_user`  

Note : Use "--ask-pass" and "--ask-become-pass" if ssh keys are not setup for "my_user" 

Second Assignment Problem Statement:
======================

When you are provisioning a production server to run a web application, what and all hardening would you do on the server? List down all the hardening steps in a markdown file in the repo.

Also, implement these hardening steps in the servers(Nginx and application) you have provisioned as part of the previous assignment.

Solution
======================
The hardening steps are mentioned in the file hardening.MD. These are implemented using the ansible roles server_hardening and nginx_hardening.

I have also segregated the app deployment and nginx deployment into separate ansible roles called app_server and nginx_server respectively. 

**Deployment**

1. Edit ansible/app_server/vars/main.yml and ansible/nginx_server/vars/main.yml

 ansible/nginx_server/vars/main.yml:
 
 internal_ips: list of internal IPs  
 nginx_bind_ip: 'IP to bind nginx'  
 app_bind_ip: 'IP to bind app'  

Example:
```yml
internal_ips: ['192.168.99.1','192.168.99.2','192.168.99.3']
nginx_bind_ip: '192.168.99.101'
app_bind_ip: '192.168.99.102'
```

 ansible/app_server/vars/main.yml:
 
 app_bind_ip: 'IP to bind app'  

Example:
```yml
app_bind_ip: '192.168.99.102'
```
2. Edit ansible/hosts file and add ips/hostname for the app server and nginx server in appropriate section. 
Example:
```ini
[nginx_server]
192.168.99.101

[app_server]
192.168.99.102
```
3. Run the ansible playbook ansible/deploy.yml  
`cd ansible && ansible-playbook deploy.yml -i hosts -u my_user`  

Note : Use "--ask-pass" and "--ask-become-pass" if ssh keys are not setup for "my_user" 


