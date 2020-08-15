# Server Hardening:

1. Install and configure auditd package. Auditd creates a log for every action on the server. We can track security-relevant events, record the events in a log file using this.

2. Disable core dump via system limits. Core dumps are usually not needed but may contain sensitive information
   
3. Login.defs Configuration File. This file provides password, mail, user id, group id, user home related configuration. For example here we configure password aging policies, automatic uid and gid selection for useradd and groupadd etc.
   
4. Securing shadow file and passwd file

5. Adding hidepid to /proc mount point. This will hide PID information in /proc from unauthorized users.

6. Pam module configuration. Enforce password complexity using pwquality module and lock users wrong password attempts using pamtally.

7. Upgrade Password Hashing Algorithm to SHA-512 using libuser.conf

8. Sysctl configurations and setting daemon umask. sysctl settings being configured along with their explanation in available in /ansible/server_hardening/vars/main.yml

9. Yum configurations. Remove unused packages and repos, enable gpgcheck for all config files.

10. SSH configuration. Disable root login, adjust idle session timeouts, change default port(changed to 2222). We can also disable logis using passwords if needed.
	
# Nginx Hardening

1. Setting server_token off to prevent exposing nginx version and server information.

2. Disabling weak ssl_protocols setting ssl_protocols to use only "TLSv1.2 and TLSv1.3".

3. Setting ssl_prefer_server_ciphers to "on" so that servers prefered cipher will be used.

4. Setting client_max_body_size  to 1k to prevent large file upload by client.

5. Setting client_body_buffer_size to 1k to limit any size of any POST action sent to the server.

6. Enabling X-XSS Protection to prevent XSS attacks

7. Setting X-Frame-Options to Deny to prevent clickjacking Attacks

8. Setting X-Content-Type-Options to "nosniff" to prevent MIME Sniffing attacks. X-Content-Type-Options HTTP response header set to nosniff will instruct browsers that support MIME sniffing to use the server-provided Content-Type and not interpret the content as a different content type.

9. Setting keepalive_timeout to 5 seconds so that Nginx will close connections with the client after this period of time.

10. Enabling SSL so that the connection between the client and server is encrypted. Here an self signed certificate is created and used to secure the communication. 
