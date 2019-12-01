city ={
    "karachi" : {
        "country": "Pakistan",
        "approximate_population":"14.91 million",
        "fact":"Karachi is the Capital of the Pakistani province od Sindh it is the most populous city in Pakistan and fifth-most-populous city proper in the world"
    },
    "Dubai" : {
        "country": "UAE",
        "approximate_population":"3.137 million approx",
        "fact":"Dubai is a city & emirate in the United Arab Emirates known for luxury shopping, ultramodren architecture and a lively nightlife scene"
    },
    "paris" : {
        "country": "France",
        "approximate_population":"2.141 million approx",
        "fact":"Paris, France's capital, is a major European city and a global center for art, fashion gastronomy and culture"
    }
}
    
for i in city.keys():
    print("Name of city is ", i)
    print("Country Name is : " , city[i]["country"])
    print("Approximate population is : " , city[i]["approximate_population"])
    print("Fact of the city is : " , city[i]["fact"])
    print("===================================================================================================================")