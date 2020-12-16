import requests
import operator

url = ('https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json')
def calculate(url):
    response = requests.get(url)
    details = response.json()
    number_water_points = {}
    number_functional = 0
    community_ranking = {}
    
    for detail in details:
        community_name = detail['communities_villages']


        if detail['water_functioning'] == 'yes':
            number_functional +=1
        elif detail['water_point_condition'] == 'broken':
            value = 1
            for key in community_ranking:
             if key == community_name:
                value += number_water_points[key]
                break
            community_ranking[community_name]=value
            

        value = 1
        for key in number_water_points:
            if key == community_name:
                value += number_water_points[key]
                break

        number_water_points[community_name]=value
    

    sorted_community_ranking = sorted(community_ranking.items(), key=operator.itemgetter(1))
    community_ranking = {k: v for k, v in sorted_community_ranking}


    resp = {
        'number_functional':number_functional,
        'number_water_points':number_water_points,
        'community_ranking': community_ranking,
    }

    return resp

#calling the function to test
print(calculate(url))
