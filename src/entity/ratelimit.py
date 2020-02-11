import graphene

from src.entity.base_entity import BaseEntity


class RateLimit(BaseEntity):
    nodeCount = graphene.Int(required=True)
    maxNodeCount = graphene.Int(required=True)
    cost = graphene.Int(required=True)
    limit = graphene.Int(required=True)
    remaining = graphene.Int(required=True)
    retryAfter = graphene.Int(required=True)
    resetAt = graphene.Int(required=True)
    
    
    def __init__(self):
        super(RateLimit, self).__init__()
