from core.ple_id_tools import Identity_Client

#Login as IDN Admin
#Keypair must reside in same folder
admin = Identity_Client('admin@plenteum','35.246.47.41','50051')

#create bank org domains
peer_address = input('Peer IP Address',end='\n')
peer_port = input('Peer Port',end='\n')
peer_key = input('Peer Public Key',end='\n')

peer_ip = peer_address + peer_port

admin.add_peer(peer_ip=peer_ip,peer_key=peer_key)