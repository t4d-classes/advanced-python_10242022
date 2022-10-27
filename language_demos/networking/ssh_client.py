from paramiko import SSHClient, AutoAddPolicy

# Paramike SSH Client/Server for Python: https://www.paramiko.org/

# create the SSH Client and load the keys
client = SSHClient()
client.load_system_host_keys()
client.set_missing_host_key_policy(AutoAddPolicy)

# connect to the SSH server with a username/password
client.connect('20.122.141.60', username='ericwgreene', password='testp@ss!')

# run a command on the SSH server
stdin, stdout, stderr = client.exec_command('ls -al')

# output the result of the command to the console
for line in stdout:
    print(line.rstrip())

# sftp is really just ssh, so using sftp upload a file to the server
with client.open_sftp() as sftp_client:
    sftp_client.chdir("/home/ericwgreene")
    print(sftp_client.getcwd())
    sftp_client.put('test.txt', "/home/ericwgreene/test.txt")

# get a directory listing to see if the file was uploaded
stdin, stdout, stderr = client.exec_command('ls -al')

for line in stdout:
    print(line.rstrip())
