# Plenteum ID Network Iroha Proof of Concept

Plenteum ID Network uses Hyperledger Iroha at its core.

Roles: Sets of permissions applied to users accounts

## Hyperledger Iroha Distributed Ledger

### System Requirements

* Ubuntu 16 or 18
* Docker + Docker Compose
* 4 GB RAM or Larger
* 40 GB SSD or Larger
* 2 Core CPU
* Ports to be publically accessable:
  * Default Ports 10001 & 50051

## How To Setup

Clone this repository

### Important

*New Node Keypairs need to be generated and are not included for security.*

Run the following commands with included scripts to install all of the required depencies automatically.

For manual configurations, ensure that the Python 3.6 or Later, build-essentials

#### Install Docker + Docker-compose

* Excecute ./PLE-ID-Core/scripts/install-docker.sh in Terminal

#### Install Python & Crypto Depencies

* Excecute ./Command-Centre/scripts/install-python.sh in Terminal

#### PLE ID Core Configuration

Generate new keys using the script located in ./Command-Centre/generate_node_key.py

* cd ./Command-Centre
* run python3 generate_node_key.py
* provide node keypair name. default is node0
* copy node keys e.g node0.priv & node0.pub to ./PLE-ID-Core/node/keys NODE KEYS MUST MATCH

Request To Join Network.

PLE ID Network is permissioned based hence peers need to be authenticated before being able to join the network and vote.

Testnet only - Contact Plenteum Development Team(@blockhain_Bobby) for adding peers

* docker-compose up -d (Runs in background)
* docker-compose up Runs with Interactive Logs

You verify that both Plenteum ID Daemon (Iroha) & Postgres are running with

'''
docker ps
'''

in a seperate terminal if required

the current container names should appear

To Tear Down or Restart.

docker-compose down
or
docker-compose restart

Note that in ./iroha/entrypoint.sh is a bash command which starts Irohas daemon.

For development and easy tear down, --overwrite-ledger flags are provided

This will delete the existing blockstore each time the stack is started.

irohad --genesis_block genesis.block --config config.docker --keypair_name $KEY --overwrite-ledger

To persist storage.

remove --overwrite-ledger flag. The last line of the bash script will look like this:

irohad --genesis_block genesis.block --config config.docker --keypair_name $KEY

## Advanced Config

If launching multiple nodes, the following enviroment variables will need to be amended accordingly.

It is *not recomended* to have more that 1 IDN Cluster running on a Server

Please ensure that the files match their expected naming convetions else the Daemon will not find the correct keys and cannot start the ledger

services:
  iroha:
    image: hyperledger/iroha:latest
    container_name: iroha-testnet
    depends_on:
      - some-postgres
    restart: always
    tty: true
    environment:
      - KEY=keys/node0 - Change to the corrosding key pair location, and name. node0 looks for
      node0.pub & node0.priv
      - IROHA_POSTGRES_HOST=some-postgres
      - IROHA_POSTGRES_PORT=5432
      - IROHA_POSTGRES_USER=postgres
      - IROHA_POSTGRES_PASSWORD=mysecretpassword - Change this for production, as well as on all of the corrosponding config files
    entrypoint:
      - /opt/iroha_data/entrypoint.sh
    networks:
      - iroha
    volumes:
      - ./iroha:/opt/iroha_data
    ports:
      - 50051:50051
      Default gRPC port for Iroha, if this port is occupied change it accordingly. Note that all commands & queries will need to Correct Ports and would need to know this in advance for commiting transactions. This is exposed to the public. Normal security mesures will need to be implemented
      - 10001:10001
      Default Torrii port for Irorha Daemon peer communications
