# eea.sanap


Self Assessment for National Adaptation Policy


## Prerequisites - System packages

These packages should be installed as superuser (root).

### Install Python2.7

    Use PUIAS: https://gist.github.com/nico4/9616638
    curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python2.7 -
    pip2.7 install virtualenv


### Install MongoDB

    vim /etc/yum.repos.d/mongodb.repo

    [mongodb]
    name=MongoDB Repository
    baseurl=http://downloads-distro.mongodb.org/repo/redhat/os/x86_64/
    gpgcheck=0
    enabled=1

    yum install mongo-10gen mongo-10gen-server

**MongoDB commands**

    service mongod start
    service mongod status
    mongo
    service mongod stop

**Export/import data from production**

    mongoexport --port [port] --db [database] --collection [collection] > [filename].json
    mongoimport --port [port] --db [database] --collection [collection] --file [filename].json

### Install wkhtmltopdf

Download and install the package from http://wkhtmltopdf.org/downloads.html

    rpm -ivh wkhtmltox-0.12.1_linux-centos6-amd64.rpm
