#!/bin/bash
set -e

# Install postgresql-9.5
PG_REPO_APT_SOURCE=/etc/apt/sources.list.d/pdgd.list
if [ ! -f $PG_REPO_APT_SOURCE ]; then
    echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > "$PG_REPO_APT_SOURCE"
    wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | apt-key add -
fi

apt-get update && apt-get --yes upgrade
apt-get install --yes \
    postgresql-9.5

if [ ! -d "/opt/conda" ]; then
    wget --quiet --no-clobber http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /opt/miniconda.sh
    bash /opt/miniconda.sh -b -p "/opt/conda"
    echo 'export PATH="/opt/conda/bin:$PATH"' >> /home/vagrant/.bashrc
    chown -R vagrant:vagrant /opt/conda
fi

export PATH="/opt/conda/bin:$PATH"
conda update --quiet --yes conda
conda env update --quiet --name app --file /vagrant/config/environment.yml
