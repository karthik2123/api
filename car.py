import json
x="""{"Honda":[{
        "Model":"Accord",
        "Oil":["Petrol","CNG"]
        },
        {
            "Model":"Amaze",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Brio",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"City",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"City IVTEC",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"City ZX",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Civic",
            "Oil":["Petrol","CNG"]
            },
         {
            "Model":"CRV",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Jazz",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Mobilio",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"BRV",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"WRV",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"Accord Hybrid",
            "Oil":["Petrol"]
            },
        {
            "Model":" City IDTEC",
            "Oil":["Diesel"]
            }
        
        ],
    "Hyundai":[
        {
            "Model":"Accent",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Accent Viva ",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Creta",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Elantra",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Elite i20",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Eon",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Getz",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Getz Prime",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":" i10",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Grand i10",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"i20",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"i20 Active",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"SantaFE",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Santro Xing",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Sonata",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Sonata Embera",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Sonata Transform",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Tucson",
            "Oil":["Diesel"]
            },
        {
            "Model":"Verna",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Verna Fluidic",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Verna Transform",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Xcent",
            "Oil":["Petrol","CNG","Diesel"]
            }]
        ,
    "Maruti Suzuki":[
        {
            "Model":"800",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Alto",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Alto 800",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Alto K10",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"A-Star",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Baleno",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Celerio",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Ciaz",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Eeco",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Ertiga",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Esteem",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Estilo",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Grand Vitara",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Gypsy",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Kizash",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Omni",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Ritz",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"S-Cross",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Swift",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Swift Dzire",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"SX4",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Versa",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"WagonR",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Zen",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Vitara Brezza",
            "Oil":["Diesel"]
            }
         ],
         "Chevrolet":[
        {
            "Model":" Aveo",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Beat",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Captiva",
            "Oil":["Diesel"]
            },
        {
            "Model":"Cruze",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Enjoy",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Forester",
            "Oil":["Diesel","CNG"]
            },
        {
            "Model":"Optra",
            "Oil":["Diesel","CNG","Petrol"]
            },
        {
            "Model":"Optra SRV",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":" Sail",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Sail Hatchback",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Spark",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Tavera",
            "Oil":["Diesel"]
            },
        {
            "Model":"UVA ",
            "Oil":["Diesel"]
            },
        {
            "Model":"Trailblazer",
            "Oil":["Diesel"]
            }
         ],
    "Daewoo":[
        {
            "Model":" Cielo",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Matiz",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":" Nexia",
            "Oil":["Petrol","CNG"]
            }
        ],
          "Datsun":[
        {
            "Model":"Go",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"GO Plus ",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Redi Go ",
            "Oil":["Petrol","Diesel"]
            }
        
         ],
    "Fiat":[
        {
            "Model":"Adventure",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Avventura",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Linea",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Linea Classic",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Palio D ",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Palio NV",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Palio Stile",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Petra",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Punto",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Punto Evo ",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"Uno",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Abarth Punto",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"Urban Cross",
            "Oil":["Petrol","Diesel"]
            }
    ],
        "Ford":[
        {
            "Model":"Eco Sport ",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Endeavour ",
            "Oil":["Diesel"]
            },
        {
            "Model":"Escort",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"Fiesta",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Fiesta Classic",
            "Oil":["Petrol","Diesel","CNG"]
            },
        {
            "Model":"Figo",
            "Oil":["Petrol","Diesel","CNG"]
            },
        {
            "Model":"Figo Aspire",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Fusion",
            "Oil":["Petrol","Diesel","CNG"]
            },
        {
            "Model":"Ikon",
            "Oil":["Petrol","Diesel","CNG"]
            },
        {
            "Model":"Mondeo",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Mustang",
            "Oil":["Petrol","Diesel","CNG"]
            },
        {
            "Model":"Freestyle",
            "Oil":["Petrol","Diesel","CNG"]
            }],
    "Mahindra":[
                {
            "Model":"Bolero",
            "Oil":["Diesel"]
            },
        {
            "Model":"Quanto",
            "Oil":["Diesel"]
            },
        {
            "Model":"Scorpio",
            "Oil":["Diesel"]
            },
        {
            "Model":"Scorpio Getaway",
            "Oil":["Diesel"]
            },
        {
            "Model":"Thar",
            "Oil":["Diesel"]
            },
        {
            "Model":"Verito",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"Verito Vibe CS",
            "Oil":["Diesel"]
            },
        {
            "Model":"XUV 500",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Xylo",
            "Oil":["Diesel"]
            },
        {
            "Model":"TUV 300",
            "Oil":["Diesel"]
            },
        {
            "Model":"KUV 100",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"NuvoSport",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"Logan",
            "Oil":["Diesel"]
            },
        {
            "Model":"Marazzo",
            "Oil":["Diesel"]
            },
        {
            "Model":"E20 Plus",
            "Oil":["Diesel"]
            },
        {
            "Model":"XUV 300",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"Bolero Camper",
            "Oil":["Diesel"]
            },
        {
            "Model":"Bolero Pickup",
            "Oil":["Diesel"]
            }],
    "Mitsubishi":[
                {
            "Model":"Pajero",
            "Oil":["Diesel"]
            },
        {
            "Model":"Pajero Sport",
            "Oil":["Diesel"]
            },
        {
            "Model":"Outlander",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Montero",
            "Oil":["Diesel"]
            },
        {
            "Model":"Lancer",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Cedia",
            "Oil":["Petrol","Diesel"]
            }],
    "Nissan":[ {
            "Model":"Evalia",
            "Oil":["Diesel"]
            },
        {
            "Model":"Micra",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Micra Active",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Sunny",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Teana",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Terrano",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"X-Trail ",
            "Oil":["Diesel"]
            },
        {
            "Model":"GTR",
            "Oil":["Petrol"]
            }],
        "Renault":[{
            "Model":"Duster",
            "Oil":["Diesel","Patrol"]
            },
        {
            "Model":"Fluence",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Koleos",
            "Oil":["Diesel"]
            },
        {
            "Model":"Lodgy",
            "Oil":["Diesel"]
            },
        {
            "Model":"Pulse",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Scala",
            "Oil":["Petrol","Diesel","CNG"]
            },
        {
            "Model":"Kwid ",
            "Oil":["Petrol","Diesel","CNG"]
            },
        {
            "Model":"Triber",
            "Oil":["Petrol","Diesel","CNG"]
            },
        {
            "Model":"Captur",
            "Oil":["Petrol","Diesel"]
            }],
    "Skoda":[{
            "Model":"Fabia",
            "Oil":["Diesel","Patrol","CNG"]
            },
        {
            "Model":"Fabia Scout",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Laura",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Octavia",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Rapid",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Superb",
            "Oil":["Petrol","Diesel","CNG"]
            },
        {
            "Model":"Yeti ",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"Kodiaq",
            "Oil":["Petrol","Diesel"]
            }],
    "Tata":[{
            "Model":"Aria",
            "Oil":["Diesel"]
            },
        {
            "Model":"Bolt",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Indica",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Indica eV2",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Indica V2",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Indica Vista",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Indigo",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Indigo CS",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Indigo eCS",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Indigo Marina",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Indigo XL",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":" Manza ",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Nano",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Nano Genx",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Safari",
            "Oil":["Diesel"]
            },
        {
            "Model":"Safari Storme",
            "Oil":["Diesel"]
            },
        {
            "Model":"Sumo Gold",
            "Oil":["Diesel"]
            },
        {
            "Model":"Sumo Grande",
            "Oil":["Diesel"]
            },
        {
            "Model":" Sumo Grande MK II",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Sumo Spacio",
            "Oil":["Diesel"]
            },
        {
            "Model":"Sumo Victa",
            "Oil":["Diesel"]
            },
        {
            "Model":"Zest",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Tiago ",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Nexon",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"Tigor",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Hexa",
            "Oil":["Diesel"]
            },
        {
            "Model":"Venture",
            "Oil":["Diesel"]
            }],
        "Toyota":[
        {
            "Model":"Fortuner",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Camry",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Corolla",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Corolla Altis",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Etios",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Etios Cross",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Etios Liva",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Innova",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Land Cruiser",
            "Oil":["Diesel"]
            },
        {
            "Model":"Land Cruiser Prado",
            "Oil":["Diesel"]
            },
        {
            "Model":"Innova Crysta",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Yaris",
            "Oil":["Petrol","CNG"]
            },
        {
            "Model":"Glanza",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Qualis",
            "Oil":["Diesel","Petrol"]
            }],
    "Volkswagen":[{
            "Model":"Cross Polo",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Jetta",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Passat",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Polo",
            "Oil":["Diesel","Petrol","CNG"]
            },
                {
            "Model":"Vento",
            "Oil":["Petrol","CNG","Diesel"]
            },
        {
            "Model":"Ameo",
            "Oil":["Diesel","Petrol","CNG"]
            },
        {
            "Model":"Beetle",
            "Oil":["Petrol"]
            },
                {
            "Model":"Tiguan",
            "Oil":["Diesel"]
            }
        ],
        "Aston Martin":[{
            "Model":"DB9",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Rapide",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"Vanquish",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Vantage",
            "Oil":["Diesel","Petrol"]
            }],
        "Audi":[{
            "Model":"A3",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"A4",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"A6",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"A7",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"A8",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"A8L",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Q5",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Q7",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Q3",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"R8",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"TT",
            "Oil":["Diesel","Petrol"]
            }],
    "Bentley":[
    {
            "Model":"Continental",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":" Flying Spur",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Mulsanne",
            "Oil":["Diesel","Petrol"]
            }],
        "BMW":[
        {
            "Model":"1 Series",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"3 Series",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"3 Series GT",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"5 Series",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"5 Series GT",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"6 Series",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"7 Series",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"M3",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"M5",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"X1",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"X3",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"X5",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"X6",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Z4",
            "Oil":["Diesel","Petrol"]
            }],
    "Ferrari":[
        {
            "Model":"458 Italia",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"458 Speciale",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"488",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"California",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"F12 Berlinetta",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"FF",
            "Oil":["Diesel","Petrol"]
            }],
            "Jaguar":[
        {
            "Model":"F Type",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"XE",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"XF",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"XJ",
            "Oil":["Diesel","Petrol"]
            }],
         "Lamborghini":[
        {
            "Model":"Aventador",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Gallardo",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"Huracan",
            "Oil":["Diesel","Petrol"]
            }],
        "Land Rover":[
    {
            "Model":"Discovery 4",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":" Discovery Sport",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Freelander 2",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Range Rover",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Range Rover Evoque",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Range Rover Sport ",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Range Rover Vogue",
            "Oil":["Diesel","Petrol"]
            }],
        "Maserati":[
            {
            "Model":"Ghibli",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"GranCabrio",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":" GranTurismo",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Quattroporte",
            "Oil":["Diesel","Petrol"]
            }],
         "Mercedes":[
        {
            "Model":"A-Class",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"AMG GT",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":" B-Class",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":" C-Class",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"CLA Class",
            "Oil":["Petrol","Diesel"]
            },
        {
            "Model":"CLS Class",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"E-Class",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"G63 AMGr",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"GL Class",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"GLA Class",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"GLE Class",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"ML Class",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"S-Class",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"SL 500 AMG",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"SLK Class",
            "Oil":["Diesel","Petrol"]
            }],
         "Mini":[
        {
            "Model":"Cooper",
            "Oil":["Diesel","Petrol"]
            },
        {
            "Model":"Countryman",
            "Oil":["Petrol","Diesel"]
            }],
    "Porsche":
    [{
            "Model":"911",
            "Oil":["Diesel","Petrol"]
            },
            {
            "Model":"Boxter",
            "Oil":["Diesel","Petrol"]
            },
            {
            "Model":"Cayenne",
            "Oil":["Diesel","Petrol"]
            },
            {
            "Model":"Cayman",
            "Oil":["Diesel","Petrol"]
            },
            {
            "Model":"Panamera",
            "Oil":["Diesel","Petrol"]
            },
            {
            "Model":"Macan",
            "Oil":["Diesel","Petrol"]
            }],
    "Rolls Royce":
    [{
            "Model":"Ghost",
            "Oil":["Diesel","Petrol"]
            },
            {
            "Model":"Phantom",
            "Oil":["Diesel","Petrol"]
            },
            {
            "Model":"Wraith",
            "Oil":["Diesel","Petrol"]
            }],
    "Volvo":
    [{
            "Model":"S60",
            "Oil":["Diesel","Petrol"]
            },
            {
            "Model":"S60 Cross Country",
            "Oil":["Diesel","Petrol"]
            },
            {
            "Model":"S80",
            "Oil":["Diesel","Petrol"]
            },
            {
            "Model":"V40",
            "Oil":["Diesel","Petrol"]
            },
            {
            "Model":"V40 Cross Country",
            "Oil":["Diesel","Petrol"]
            },
            {
            "Model":"XC60",
            "Oil":["Diesel","Petrol"]
            },
            {
            "Model":"XC90",
            "Oil":["Diesel","Petrol"]
            }],
        "Force":
    [{
            "Model":"One",
            "Oil":["Diesel"]
            },
            {
            "Model":"Traveller 3350",
            "Oil":["Diesel","Petrol"]
            },
            {
            "Model":"Trax",
            "Oil":["Diesel","Petrol"]
            },
            {
            "Model":"Gurkha",
            "Oil":["Diesel","Petrol"]
            }],
        
        "Isuzu":
    [{
            "Model":"MU7",
            "Oil":["Diesel"]
            },
            {
            "Model":"Isuzu Dmax Vcross",
            "Oil":["Diesel"]
            }],
            "Hindustan Motors":
    [{
            "Model":"Ambassador",
            "Oil":["Diesel","Petrol","CNG"]
            }],
            "Jeep":
    [{
            "Model":"Compass",
            "Oil":["Diesel","Petrol"]
            }],
        "Opel":[{
            "Model":"Astra",
            "Oil":["Diesel","Petrol","CNG"]
            },
            {
            "Model":"Corsa",
            "Oil":["Diesel","Petrol"]
            }],
        "Ssangyong":[{
            "Model":"Rexton",
            "Oil":["Diesel","Petrol"]
            }],
            "MG":[{
            "Model":"Hector",
            "Oil":["Diesel","Petrol"]
            }],
            "Kia":[{
            "Model":"Seltos",
            "Oil":["Diesel","Petrol"]
            }],
            "Photon":[{
            "Model":"VIW CS2",
            "Oil":["Diesel","Petrol"]
            }],
            "Jayem":[{
            "Model":"Neo",
            "Oil":["Electric "]
            }]

            
            }"""
y = json.loads(x)
for i in y["Jeep"]:
    print(i)

