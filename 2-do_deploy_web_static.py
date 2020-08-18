#!/usr/bin/python3
# Script that distributes an archive to your web servers, 
# using the function do_deploy
"""do deploy web static"""
from fabric.api import *


env.user = "ubuntu"
env.hosts = ["104.196.116.233", "54.165.130.77"]


def do_pack():
    """Do_pack function"""
    today = datetime.datetime.now()
    file_local = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(today.year,
                                                               today.month,
                                                               today.day,
                                                               today.hour,
                                                               today.minute,
                                                               today.second)

    local('mkdir -p versions')
    check = local('tar -cvzf {} web_static'.format(file_local))
    if check.failed:
        return None
    else:
        return file_local

def do_deploy(archive_path):
    """function do_deploy"""
    path_file = archive_path.split('/')[-1]
    folder = path_file.split('.')[0]
    
     # Upload directory
    upload = put(archive_path, '/tmp/{}'.format(path_file))

    if archive_path is None or upload.failed:
        return False
    
    
    if put(archive_path, "/tmp/{}".format(path_file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(folder)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(folder)).failed is True:
        return False
    
    # run("rm -rf /data/web_static/releases/{}/".format(folder))
    # Create folder
    # run('mkdir -p /data/web_static/releases/{}/'.format(folder))
    #if stat.failed:
    #    return False

    # Uncompress the archive
    command = 'tar xvzf /tmp/{}'.format(path_file)
    command += '-C /data/web_static/releases/{}'.format(folder)
    run(command)
    run('rm -rf /tmp/{}'.format(path_file))
    command = 'mv /data/web_static/releases/{}/web_static/*'.format(folder)
    command += '/data/web_static/releases/{}/'.format(folder)
    run(command)
    
    clean = 'rm -rf /data/web_static/releases/{} /data/web_static/current'.format(folder)
    run(clean)
    
    #Delete symbolic link
    run('rm -rf /data/web_static/current')
    # Create new symbolic link
    run('ln -sfn /data/web_static/releases/{} /data/web_static/current'.format(folder))

def deploy():
    """Verify the status of deploy"""
    file_name = do_pack()
    if file_name is None:
        return False
    return do_deploy(file_name)
