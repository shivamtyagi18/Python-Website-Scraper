import os
citiesContraCosta=["Antioch",
"Brentwood",
"Clayton",
"Concord",
"Town of Danville",
"El Cerrito",
"Hercules",
"Lafayette",
"Martinez",
"Town of Moraga",
"Oakley",
"Orinda",
"Pinole",
"Pittsburg",
"Pleasant Hill",
"Richmond",
"San Pablo",
"San Ramon",
"Walnut Creek"]

citiesImperial=["Brawley",
"Calexico",
"Calipatria",
"El Centro",
"Holtville",
"Imperial",
"Westmorland"]

citiesRiverside=[
"Blythe",
"Calimesa",
"Canyon Lake",
"Cathedral City",
"Coachella",
"Corona",
"Desert Hot Springs",
"Eastvale",
"Hemet",
"Indian Wells",
"Indio",
"Jurupa Valley",
"La Quinta",
"Lake Elsinore",
"Menifee",
"Moreno Valley",
"Murrieta",
"Norco",
"Palm Desert",
"Palm Springs",
"Perris",
"Rancho Mirage",
"Riverside",
"San Jacinto",
"Temecula",
"Wildomar"
]

citiesSanDiego=[
"Carlsbad",
"Chula Vista",
"Coronado",
"Del Mar",
"El Cajon",
"Encinitas",
"Escondido",
"Imperial Beach",
"La Mesa",
"Lemon Grove",
"National City",
"Oceanside",
"Poway",
"San Diego",
"San Marcos",
"Santee",
"Solana Beach",
"Vista"
]

years=["2007-08",
"2008-09",
"2009-10",
"2010-11",
"2011-12",
"2012-13",
"2013-14",
"2014-15",
"2015-16",
"2016-17",
"2017-18" ]

Counties=[
    "Alameda",
    "Orange",
    "ContraCosta",
    "Imperial",
    "SanDiego",
    "Riverside",
    "LosAngeles",
    "Fresno"
]



for j in years:
    county=Counties[2]
    path = "/Users/"+county+"/Local Return Spending/City Documents/"+j+"/"
    access_rights = 0o755
#     try:  
#         os.mkdir(path, access_rights)
#     except OSError:  
#         print ("Creation of the directory %s failed" % path)
#     else:  
#         print ("Successfully created the directory %s" % path)
    for i in citiesContraCosta:
        path1 = path+i+"/"

# define the access rights
        access_rights = 0o755
        try:  
            os.makedirs(path1, access_rights)
            #os.rmdir(path)
        except OSError:  
            print ("Creation of the directory %s failed" % path1)
        else:  
            print ("Successfully created the directory %s" % path1)
