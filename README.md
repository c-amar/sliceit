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
The application is coded in python3 using django framework. I have used gunicorn as the application server. Deplyoment is automated using a simple ansible playbook.

**Requirements/ Assumptions**
1. Two servers with centOS.
2. Ansible server 

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
`cd ansible && cd ansible/ && ansible-playbook deploy.yml -i hosts -u my_user`
