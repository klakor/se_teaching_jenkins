import jenkins

server = jenkins.Jenkins('http://localhost:8080',
                         username='admin',
                         password='')  # place password here


user = server.get_whoami()
version = server.get_version()
plugins = server.get_plugins_info()

print('Hello %s from Jenkins %s' % (user['fullName'], version))
print ('Installed plugins: ', plugins)
