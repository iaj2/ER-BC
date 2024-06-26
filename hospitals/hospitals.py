# Dummy data for hospitals and their wait times
hospitals = [
    {"id":"vgh", "name": "Vancouver General Hospital", "location": "920 West 10th Ave Vancouver, BC, V5Z 1M9", "phone-number": "(604) 875-4111", "wait_time": 30, "latitude": 49.26236, "longitude": -123.12422},
    {"id":"rh", "name": "Richmond Hospital", "location": "7000 Westminster Highway Richmond, BC, V6X 1A2", "phone-number": "(604) 278-9711", "wait_time": 45, "latitude": 49.16882, "longitude": -123.1468},
    {"id":"sph", "name": "St. Paul's Hospital", "location": "1081 Burrard St Vancouver, BC, V6Z 1Y6", "phone-number": "(604) 682-2344", "wait_time": 45, "latitude": 49.28072, "longitude": -123.12855},
    {"id":"lgh", "name": "Lions Gate Hospital", "location": "231 East 15th St North Vancouver, BC, V7L 2L7", "phone-number": "(604) 988-3131", "wait_time": 20, "latitude": 49.32087, "longitude": -123.06771},
    {"id":"msjh","name": "Mount Saint Joseph Hospital", "location": "3080 Prince Edward St Vancouver, BC, V5T 3N4", "phone-number": "(604) 874-1141", "wait_time": 15, "latitude": 49.25815, "longitude": -123.096},
    {"id":"ubch", "name": "UBC Hospital (UBCH)", "location": "2211 Wesbrook Mall Vancouver, BC, V6T 2B5", "phone-number": "(604) 822-7121", "wait_time": 20, "latitude": 49.26412, "longitude":  -123.24543},
    {"id":"bccch","name": "BC Children's Hospital", "location": "4480 Oak St Vancouver, BC, V6H 3V4", "phone-number": "(604) 875-2345", "wait_time": 30, "latitude": 49.24468, "longitude": -123.12534},
    {"id":"sh", "name": "Sechelt Hospital", "location": "5544 Sunshine Coast Highway Sechelt, BC V0N 3A0", "phone-number": "(604) 885-2224", "wait_time": 30, "latitude": 49.47564, "longitude": -123.74928},
    {"id":"arh", "name": "Abbotsford Regional Hospital", "location": "32900 Marshall Road Abbotsford, BC, V2S 0C2", "phone-number": "(604) 851-4700", "wait_time": 30, "latitude": 49.03686, "longitude": -122.31188},
    {"id":"bh", "name": "Burnaby Hospital", "location": "3935 Kincaid St Burnaby, BC, V5G 2X6", "phone-number": "(604) 434-4211", "wait_time": 30, "latitude": 49.24946, "longitude": -123.01563},
    {"id":"cgh", "name": "Chilliwack General Hospital", "location": "45600 Menholm Rd Chilliwack, BC, V2P 1P7", "phone-number": "(604) 795-4141", "wait_time": 30, "latitude": 49.16654, "longitude": -121.9628},
    {"id":"dh", "name": "Delta Hospital", "location": "5800 Mountain View Blvd Delta, BC, V4K 3V6", "phone-number": "(604) 946-1121", "wait_time": 30, "latitude": 49.08573, "longitude": -123.06164},
    {"id":"erh", "name": "Eagle Ridge Hospital", "location": "475 Guildford Way Port Moody, BC, V3H 3W9", "phone-number": "(604) 461-2022", "wait_time": 30, "latitude": 49.28549, "longitude": -122.82341},
    {"id":"lmh", "name": "Langley Memorial Hospital", "location": "22051 Fraser Hwy Langley, BC, V3A 4H4", "phone-number": "(604) 514-6000", "wait_time": 30, "latitude": 49.09285, "longitude": -122.61252},
    {"id":"pah", "name": "Peace Arch Hospital", "location": "15521 Russell Avenue White Rock, BC, V4B 2R4", "phone-number": "(604) 531-5512", "wait_time": 30, "latitude": 48.998999, "longitude": -122.740968},
    {"id":"rmh", "name": "Ridge Meadows Hospital", "location": "11666 Laity St Maple Ridge, BC, V2X 7G5", "phone-number": "(604) 463-4111", "wait_time": 30, "latitude": 49.21487, "longitude": -122.630951},
    {"id":"sgh", "name": "Squamish General Hospital", "location": "38140 Behrner Dr Squamish, BC, V8B 0J3", "phone-number": "(604) 892-5211", "wait_time": 30, "latitude": 49.69755, "longitude": -123.14132},
    {"id":"smh", "name": "Surrey Memorial Hospital", "location": "13750 96th Ave Surrey, BC, V3V 1Z2", "phone-number": "(604) 581-2211", "wait_time": 30, "latitude": 49.17645, "longitude": -122.84278},
    {"id":"rch", "name": "Royal Columbian Hospital", "location": "330 East Columbia St New Westminster, BC, V3L 3W7", "phone-number": "(604) 520-4253", "wait_time": 30, "latitude": 49.22657, "longitude": -122.89157},
    {"id":"qgh", "name": "qathet General Hospital", "location": "5000 Joyce Avenue Powell River, BC V8A 5R3", "phone-number": "(604) 485-3211", "wait_time": 30, "latitude": 49.85083, "longitude": -124.51847},
    {"id":"phc","name": "Pemberton Health Centre", "location": "1403 Portage Road Pemberton, BC, V0N 2L0", "phone-number": "(604) 894-6939", "wait_time": 30, "latitude": 50.32115, "longitude": -122.80478},
    {"id":"swupcc","name": "Surrey Whalley UPCC", "location": "9639 137a St Unit G2 Surrey, BC V3T 0M1", "phone-number": "(604) 572-2610", "wait_time": 30, "latitude": 49.17798, "longitude": -122.84232},
    {"id":"rmupcc","name": "Ridge Meadows UPCC", "location": "121-11900 Haney Place Maple Ridge, BC V2X 8R9", "phone-number": "(604) 476-4650", "wait_time": 30, "latitude": 49.21798, "longitude":  -122.59781},
    {"id":"pmupcc","name": "Port Moody UPCC", "location": "3105 Murray St Port Moody, BC V3H 1X3", "phone-number": "(604) 469-3123", "wait_time": 30, "latitude": 49.2788, "longitude": -122.8415},
    {"id":"mupcc","name": "Metrotown UPCC", "location": "Unit 102 - 4555 Kingsway Burnaby, BC V5H 4T8", "phone-number": "(604) 451-4888", "wait_time": 30, "latitude": 49.23007, "longitude": -123.00277},
    {"id":"eupcc","name": "Edmonds UPCC", "location": "Unit 201, 7315 Edmonds St Burnaby, BC V3N 1A7", "phone-number": "(604) 519-3787", "wait_time": 30, "latitude": 49.21873, "longitude": -122.95125},
]
