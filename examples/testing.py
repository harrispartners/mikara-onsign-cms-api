from config_load import ConfigLoad
config = ConfigLoad()
from src.onsign import OnSign
from src.onsign_factory import OnSignFactory
from src.entity.organization import Organization

from src.utils import *


factory = OnSignFactory({
    'BASE_URL': config.get('BASE_URL'),
    'CLIENT_SECRET': config.get('CLIENT_SECRET')
})


query =\
"""
{
    organization
    {
        id
        name
        players(first: 100)
        {
            pageInfo {
              endCursor
              hasNextPage
            }
            nodes {
              id
              lastSeen
            }
            totalCount
        }
    }
}
"""
query =\
"""
{
    organization
    {
        id
        player(id: "8BCYV14")
        {
            id
            name
        }
    }
}
"""
result = factory.get_entity('Player').post(create_graphql_request(query, True))
print(result)
exit(0)



query =\
"""
{
    organization
    {
        id
        name
    }
}
"""
result = factory.get_entity('Organization').post(create_graphql_request(query, True))
print(result.id)

query =\
"""
{
    organization
    {
        players(first: 100)
        {
            nodes
            {
                id
                name
                errorCount
                lastSeen
                lastSeenAgo
                workingHours
                {
                    weekDays
                    startTime
                    endTime
                }
                tags
                attrs
                updateReady
                updateRequested
            }
        }
    }
}
"""
result = factory.get_entity('PlayerConnection').post(create_graphql_request(query, True))
print(result.nodes)
print(result.nodes[0].name)
print(result.nodes[0].workingHours[0].startTime)
print(result.nodes[0].updateRequested)


query =\
"""
{
    organization
    {
        playerGroups(first: 100)
        {
            nodes
            {
                id
                name
                tags
                players(first: 100) {
                    nodes {
                        id
                        name
                    }
                    totalCount
                }
            }
        }
    }
}
"""
result = factory.get_entity('PlayerGroupConnection').post(create_graphql_request(query, True))
print(result.nodes)
print(result.nodes[0].name)