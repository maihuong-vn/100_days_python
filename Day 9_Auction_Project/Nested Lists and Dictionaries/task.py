# capitals = {
#    " France": "Paris",
#    "Germany": "Berlin"
# }


# travel_log ={
#     "France": {
#         "city_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },

#     "Germany": {
#         "city_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 5
#     },
# }

# print(travel_log["Germany"]["city_visited"][2])


order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}


print(order["main"][2][0])     #2: is key value "2" inside a dict {"2"}, 0 is index no. of Steak inside a LIST


