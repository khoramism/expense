#import doctest
#from django_elasticsearch_dsl import DocType, fields, Index 
#from .models import Transaction
#
#trans_index = Index('trans')
#
#trans_index.settings(
#    number_of_shards = 1,
#    number_of_replicas = 0,
#)
#
#@trans_index.doc_type
#class TransDocument(DocType):
#    name = fields.TextField(
#        attr = 'name',
#        
#    )