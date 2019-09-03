from iroha_tools import IrohaClient

admin = IrohaClient('admin@plenteum','35.246.47.41','50051')
#add platcorp node
admin.create_domain('platcorp','user')