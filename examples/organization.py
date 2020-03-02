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


'''query = \
"""
{
    organization {
        id
        name
        
      playerGroups(first:100) {
        totalCount
        pageInfo {
          hasNextPage
          endCursor
        }
        nodes{
          id
          name
          tags
          loop(name:PRIMARY){
            id
            kind
            items(first:100){
              edges{
                id
                isPaused
              }
            }
          }
          players(first: 100){
            pageInfo{
              endCursor
              hasNextPage
            }
            totalCount
            nodes {
              id
              name
              isConnected
            }
          }
        }
      }
    }
}
"""'''

'''query = \
"""
{
    organization {
      id
      name
      
    }
}
"""'''

'''query = \
"""
{
  organization {
    id
    name
    
  }
}
"""'''

query = \
"""
{
  organization {
    id
    name
    
  }
}

"""

query = \
"""
{
  organization {
    id
    name
    
    players(first: 100) {
            nodes {
              id
              name
              errorCount
              lastSeen
              isConnected
              syncProgress
              signalStrength
              timezone
              utcOffset
              workingHours {
                weekDays
                startTime
                endTime
              }
              version
              tags
              attrs
              updateRequested
              updateReady
              loop(name:PRIMARY) {
                id
                kind
                items(first:100) {
                  totalCount
                  pageInfo {
                    endCursor
                    hasNextPage
                  }
                  edges {
                    id
                    position
                    restrictions{
                      tag {
                        action
                        tags
                      }
                      calendar {
                        endDate
                        weekDays
                        startTime
                        startDate
                      }
                    }
                    isPaused
                    node{
                      name
                      __typename
                    }
                  }
                }
              }
            }
        }
    playerGroups(first:100) {
        pageInfo {
          hasNextPage
          endCursor
        }
        totalCount
        nodes {
          id
          name
          tags
          players(first: 100) {
            nodes {
              id
              name
            }
            pageInfo {
              hasNextPage
              endCursor
            }
            totalCount
          }
        }
      }
    playlists(first: 100) {
      pageInfo {
        hasNextPage
        endCursor
      }
      totalCount
      nodes {
        id
        name
        tags
        items(first:100) {
          edges {
            id
            isPaused
            position
            node{
              name
              __typename
            }
          }
        }
      }
    }
    campaigns(first: 100) {
      pageInfo {
        hasNextPage
        endCursor
      }
      totalCount
      nodes {
        id
        name
        tags
        category
        isPaused
        restrictions {
          tag {
            action
            tags
          }
        }
      }
    }
    contentRoot {
      id
      name
      kind
      children(first:100) {
        nodes{
          id
          name
        }
      }
    }
    contents(first: 100) {
        nodes {
            id
            name
        }
    }
    reports(first: 100) {
        nodes {
            id
            __typename
        }
    }
  }
}
"""

result = factory.get_entity('Organization').post(create_graphql_request(query, True))
print(result)
print(result.players.nodes[0])
print(result.players.nodes[0].workingHours)
print(result.players.nodes[0].loop.items.edges[0])
print()
print(result.playerGroups.nodes[0])
print(result.playerGroups.nodes[0].players.nodes[0])
print()
print(result.playlists.nodes[0])
print()
print(result.campaigns.nodes[0])
print()
print(result.contentRoot.children.nodes[0])
print()
print(result.contents.nodes[1])
print()
print(result.reports.nodes[0])