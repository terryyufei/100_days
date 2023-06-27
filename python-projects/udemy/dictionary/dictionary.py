#lists nested in a dictionary
travel_log = {
    "France": ["paris", "lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
    }
#print(travel_log)

#Nesting a dictionary in a dictionary
#travel_log2 = {}                                                                                         
#travel_log2 = travel_log.copy()
travel_log2 = {
      
    "France": {"cities_visited": ["paris", "lille", "Dijon"], "total_visits": 9},
    "Germany": {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 12},
    }
#print(travel_log2)
#print(travel_log2["France"]["cities_visited"])
print(travel_log2["Germany"]["total_visits"])


#Nesting dictionary in a list
travel_log3 = [
    {
    "counrty": "France", 
    "cities_visited": ["paris", "lille", "Dijon"], 
    "total_visits": 9
    },
    {
    "country": "Germany",
    "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 12,
    },
]


#print(travel_log3)