#CRICKET KNOWLEDGE GAME
import random
import tkinter as tk
from tkinter import ttk
cricket_grounds = [
    # Australia
    "Adelaide Oval, Adelaide",
    "Melbourne Cricket Ground (MCG), Melbourne",
    "Sydney Cricket Ground (SCG), Sydney",
    "The Gabba, Brisbane",
    "Perth Stadium (Optus Stadium), Perth",
    "Bellerive Oval, Hobart",
    "Manuka Oval, Canberra",
    "Metricon Stadium, Gold Coast",

    # England
    "Lord’s, London",
    "The Oval, London",
    "Old Trafford, Manchester",
    "Edgbaston, Birmingham",
    "Headingley, Leeds",
    "Trent Bridge, Nottingham",
    "The Rose Bowl, Southampton",
    "County Ground, Bristol",
    "Riverside Ground, Chester-le-Street",
    "Sophia Gardens, Cardiff",

    # India
    "Eden Gardens, Kolkata",
    "Wankhede Stadium, Mumbai",
    "M. Chinnaswamy Stadium, Bengaluru",
    "Feroz Shah Kotla Ground (Arun Jaitley Stadium), Delhi",
    "M. A. Chidambaram Stadium, Chennai",
    "Sardar Patel Stadium (Narendra Modi Stadium), Ahmedabad",
    "Rajiv Gandhi International Stadium, Hyderabad",
    "Holkar Cricket Stadium, Indore",
    "PCA Stadium (IS Bindra Stadium), Mohali",
    "Green Park Stadium, Kanpur",
    "Saurashtra Cricket Association Stadium, Rajkot",
    "Maharashtra Cricket Association Stadium, Pune",
    "Barabati Stadium, Cuttack",
    "Vidarbha Cricket Association Stadium, Nagpur",
    "Sawai Mansingh Stadium, Jaipur",

    # South Africa
    "Newlands, Cape Town",
    "Wanderers Stadium, Johannesburg",
    "Kingsmead, Durban",
    "Centurion Park, Centurion",
    "St George’s Park, Port Elizabeth",

    # New Zealand
    "Eden Park, Auckland",
    "Hagley Oval, Christchurch",
    "Basin Reserve, Wellington",
    "Seddon Park, Hamilton",
    "McLean Park, Napier",
    "University Oval, Dunedin",
    "Bay Oval, Mount Maunganui",

    # Pakistan
    "Gaddafi Stadium, Lahore",
    "National Stadium, Karachi",
    "Rawalpindi Cricket Stadium, Rawalpindi",
    "Multan Cricket Stadium, Multan",
    "Pindi Cricket Stadium, Rawalpindi",

    # Sri Lanka
    "R. Premadasa Stadium, Colombo",
    "Galle International Stadium, Galle",
    "Pallekele International Cricket Stadium, Kandy",
    "Rangiri Dambulla International Stadium, Dambulla",
    "Sinhalese Sports Club Ground (SSC), Colombo",

    # West Indies
    "Kensington Oval, Barbados",
    "Queen’s Park Oval, Trinidad",
    "Sabina Park, Jamaica",
    "Sir Vivian Richards Stadium, Antigua",
    "Warner Park, St. Kitts",
    "National Cricket Stadium, Grenada",
    "Providence Stadium, Guyana",

    # Bangladesh
    "Sher-e-Bangla National Stadium, Dhaka",
    "Zahur Ahmed Chowdhury Stadium, Chittagong",
    "Sylhet International Cricket Stadium, Sylhet",
    "Khan Shaheb Osman Ali Stadium, Fatullah",

    # Zimbabwe
    "Harare Sports Club, Harare",
    "Queens Sports Club, Bulawayo",

    # Afghanistan
    "Sharjah Cricket Stadium, Sharjah (UAE)",
    "Greater Noida Sports Complex Ground, Greater Noida (India)",

    # Ireland
    "Malahide Cricket Club Ground, Dublin",
    "The Village, Dublin",
    "Stormont, Belfast",

    # Scotland
    "The Grange Club, Edinburgh",

    # Netherlands
    "VRA Cricket Ground, Amstelveen",

    # United Arab Emirates
    "Dubai International Stadium, Dubai",
    "Sheikh Zayed Stadium, Abu Dhabi",
    "Sharjah Cricket Stadium, Sharjah",

    # Nepal
    "Tribhuvan University International Cricket Ground, Kathmandu"
]
batsmen = [
    # Australia
    "Ricky Ponting", "Steve Smith", "David Warner", "Matthew Hayden", "Michael Clarke", 
    "Justin Langer", "Mark Waugh", "Allan Border", "Aaron Finch", "Dean Jones",
    "Damien Martyn", "Chris Rogers", "Phil Hughes", "George Bailey", "Usman Khawaja",
    "Shaun Marsh", "Simon Katich", "David Boon", "Brad Hodge", "Andrew Symonds",
    "Greg Chappell", "Steve Waugh",

    # India
    "Sachin Tendulkar", "Virat Kohli", "Rohit Sharma", "Sunil Gavaskar", "Virender Sehwag", 
    "Rahul Dravid", "VVS Laxman", "Sourav Ganguly", "Yuvraj Singh", "Gautam Gambhir",
    "Ajinkya Rahane", "Shikhar Dhawan", "Mohammad Kaif", "Suresh Raina", "KL Rahul",
    "Cheteshwar Pujara", "Robin Uthappa", "Dilip Vengsarkar", "Navjot Sidhu", "Vinod Kambli",
    "Shubman Gill", "Manish Pandey", "Krishnamachari Srikkanth", "Raman Lamba", "Sanjay Manjrekar",
    "Ajay Jadeja", "Amol Muzumdar", "Murali Vijay", "Wasim Jaffer", "Pravin Amre",

    # England
    "Joe Root", "Alastair Cook", "Kevin Pietersen", "Graham Gooch", "Geoff Boycott",
    "Ian Bell", "David Gower", "Eoin Morgan", "Jason Roy", "Michael Atherton",
    "Marcus Trescothick", "Nick Compton", "Andrew Strauss", "Jonathan Trott", "James Vince",
    "Paul Collingwood", "Alex Hales", "Dawid Malan", "Tom Banton", "Ravi Bopara",
    "Nasser Hussain", "Ollie Pope", "Mike Gatting", "Alan Lamb", "David Lloyd",

    # Pakistan
    "Babar Azam", "Inzamam-ul-Haq", "Javed Miandad", "Mohammad Yousuf", "Younis Khan",
    "Saeed Anwar", "Zaheer Abbas", "Imam-ul-Haq", "Fakhar Zaman", "Ijaz Ahmed",
    "Rameez Raja", "Saleem Malik", "Asif Iqbal", "Taufeeq Umar", "Shoaib Mohammad",
    "Aamer Sohail", "Mudassar Nazar", "Hanif Mohammad", "Salman Butt", "Fawad Alam",
    "Ahmed Shehzad", "Kamran Akmal", "Shoaib Malik",

    # South Africa
    "AB de Villiers", "Hashim Amla", "Graeme Smith", "Jacques Kallis", "Faf du Plessis",
    "Herschelle Gibbs", "Gary Kirsten", "Aiden Markram", "Daryll Cullinan", "Ashwell Prince",
    "JP Duminy", "Neil McKenzie", "Peter Kirsten", "Kepler Wessels", "Rassie van der Dussen",
    "Dean Elgar", "Temba Bavuma", "David Miller", "Stephen Cook", "Colin Ingram",
    "Gerhardus Liebenberg",

    # New Zealand
    "Kane Williamson", "Martin Guptill", "Ross Taylor", "Stephen Fleming", "Brendon McCullum",
    "Glenn Turner", "Nathan Astle", "John Wright", "Mark Richardson", "Craig McMillan",
    "Mathew Sinclair", "Rob Nicol", "Lou Vincent", "Hamish Rutherford", "James Marshall",
    "Henry Nicholls", "BJ Watling", "Tom Latham", "Neil Broom", "Bruce Edgar",

    # Sri Lanka
    "Kumar Sangakkara", "Mahela Jayawardene", "Sanath Jayasuriya", "Tillakaratne Dilshan", 
    "Aravinda de Silva", "Marvan Atapattu", "Angelo Mathews", "Upul Tharanga", 
    "Roshan Mahanama", "Asanka Gurusinha", "Chamari Atapattu", "Niroshan Dickwella",
    "Thilan Samaraweera", "Dhananjaya de Silva", "Kusal Mendis", "Avishka Gunawardene",
    "Hashan Tillakaratne", "Kusal Perera", "Lahiru Thirimanne", "Russel Arnold",

    # West Indies
    "Brian Lara", "Viv Richards", "Chris Gayle", "Shivnarine Chanderpaul", "Clive Lloyd",
    "Gordon Greenidge", "Desmond Haynes", "Rohan Kanhai", "Shai Hope", "Darren Bravo",
    "Lawrence Rowe", "Carl Hooper", "Ramnaresh Sarwan", "Richie Richardson", "Dwayne Smith",
    "Brendan Nash", "Marlon Samuels", "Darren Ganga", "Lendl Simmons", "Adrian Barath",
    "Phil Simmons", "Kieran Powell",

    # Bangladesh
    "Tamim Iqbal", "Shakib Al Hasan", "Mushfiqur Rahim", "Mahmudullah", "Mohammad Ashraful",
    "Soumya Sarkar", "Liton Das", "Imrul Kayes", "Anamul Haque", "Shahriar Nafees",
    "Naim Sheikh", "Nazimuddin", "Nafees Iqbal", "Aminul Islam", "Atahar Ali Khan",
    "Sabbir Rahman", "Raqibul Hasan", "Akram Khan", "Javed Omar", "Mohammad Naim",

    # Zimbabwe
    "Andy Flower", "Grant Flower", "Brendan Taylor", "Tatenda Taibu", "Hamilton Masakadza",
    "Sean Williams", "Sikandar Raza", "Alistair Campbell", "Craig Ervine", "Charles Coventry",
    "Stuart Carlisle", "Mark Vermeulen", "Vusi Sibanda", "Murray Goodwin", "Andy Waller",
    "Neil Johnson", "Guy Whittall", "Paul Strang", "Bryan Strang", "Carlisle Best",

    # Afghanistan
    "Mohammad Shahzad", "Rahmat Shah", "Hashmatullah Shahidi", "Asghar Afghan", "Najibullah Zadran",
    "Hazratullah Zazai", "Ibrahim Zadran", "Noor Ali Zadran", "Karim Sadiq", "Javed Ahmadi",
    "Usman Ghani", "Najeeb Tarakai", "Samiullah Shenwari", "Mohammad Nabi",

    # Ireland
    "Paul Stirling", "William Porterfield", "Kevin O'Brien", "Ed Joyce", "Niall O'Brien",
    "Andrew Balbirnie", "Harry Tector", "James McCollum", "John Anderson", "Lorcan Tucker",
    "Gary Wilson", "Jack Tector",

    # Scotland
    "Kyle Coetzer", "Calum MacLeod", "Richie Berrington", "George Munsey", "Gavin Hamilton",
    "Ryan Watson", "Craig Wallace", "Matthew Cross", "Preston Mommsen", "Gordon Goudie",
    "Fraser Watts", "Majid Haq", "Colin Smith", "Euan Chalmers", "Michael Leask",

    # Netherlands
    "Tom Cooper", "Stephan Myburgh", "Bas de Leede", "Ben Cooper", "Max O'Dowd",
    "Wesley Barresi", "Michael Swart", "Eric Szwarczynski", "Peter Borren", "Roland Lefebvre",
    "Tim de Leede", "Ruud Nijman",

    # Nepal
    "Paras Khadka", "Gyanendra Malla", "Sharad Vesawkar", "Dipendra Singh Airee", 
    "Binod Bhandari", "Rohit Paudel", "Kushal Bhurtel", "Sompal Kami", "Rajesh Pulami",
    "Aarif Sheikh",

    # UAE
    "Chirag Suri", "Shaiman Anwar", "Swapnil Patil", "Mohammad Naveed", "Rameez Shahzad",
    "Arshad Ali", "Khurram Khan", "Amjad Ali", "Abdul Shakoor"
]
wicketkeepers = [
    # Australia
    "Adam Gilchrist", "Ian Healy", "Brad Haddin", "Tim Paine", "Matthew Wade", 
    "Alex Carey", "Graham Manou", "Phil Emery", "Peter Nevill", "Rod Marsh",
    
    # India
    "MS Dhoni", "Rishabh Pant", "Nayan Mongia", "Parthiv Patel", "Wriddhiman Saha", 
    "Syed Kirmani", "Kiran More", "Dinesh Karthik", "KL Rahul", "Farokh Engineer",
    "Ishaan Kishan", "Ajay Ratra", "Saba Karim",

    # England
    "Jos Buttler", "Jonny Bairstow", "Matt Prior", "Alec Stewart", "James Foster",
    "Geraint Jones", "Paul Downton", "Chris Read", "Alan Knott", "Ben Foakes",
    "Steve Rhodes", "Tim Ambrose", "Craig Kieswetter", "Phil Mustard",

    # Pakistan
    "Sarfaraz Ahmed", "Moin Khan", "Kamran Akmal", "Rashid Latif", "Imtiaz Ahmed", 
    "Zulqarnain Haider", "Adnan Akmal", "Umar Akmal", "Wasim Bari", "Salim Yousuf",

    # South Africa
    "Mark Boucher", "Quinton de Kock", "Dave Richardson", "Thami Tsolekile", 
    "Dane Vilas", "AB de Villiers", "Morne van Wyk", "Heino Kuhn", "Nic Pothas",
    "Lee Irvine", "Denis Lindsay",

    # New Zealand
    "Brendon McCullum", "BJ Watling", "Tom Latham", "Luke Ronchi", "Adam Parore", 
    "Ian Smith", "Jock Edwards", "Gareth Hopkins", "Peter McGlashan", "Glenn Phillips",
    "Ken Wadsworth", "Lee Germon", "Kruk Sebesky",

    # Sri Lanka
    "Kumar Sangakkara", "Romesh Kaluwitharana", "Niroshan Dickwella", "Kusal Perera", 
    "Prasanna Jayawardene", "Chandrika Hathurusingha", "Mahes Goonatilleke", 
    "Dinesh Chandimal", "Kaushal Silva", "Pubudu Dassanayake", "Brendon Kuruppu",

    # West Indies
    "Jeff Dujon", "Ridley Jacobs", "Denesh Ramdin", "Shai Hope", "Chadwick Walton", 
    "Andre Fletcher", "Courtney Browne", "Junior Murray", "David Williams", 
    "Patrick Browne", "Sylvester Joseph",

    # Bangladesh
    "Mushfiqur Rahim", "Khaled Mashud", "Anamul Haque", "Nurul Hasan", "Liton Das",
    "Jahurul Islam", "Shahriar Nafees", "Mohammad Mithun", "Manjural Islam",

    # Zimbabwe
    "Andy Flower", "Tatenda Taibu", "Brendan Taylor", "Regis Chakabva", "Wayne James", 
    "Adam Huckle", "Charles Coventry", "Forster Mutizwa", "Richmond Mutumbami", 
    "PJ Moor", "Wayne James",

    # Afghanistan
    "Mohammad Shahzad", "Afsar Zazai", "Shafiqullah Shafiq", "Ikram Ali Khil", 
    "Rahmanullah Gurbaz",

    # Ireland
    "Niall O'Brien", "Gary Wilson", "Lorcan Tucker", "Neil Rock", "Denis Smith",

    # Scotland
    "Matthew Cross", "Craig Wallace", "Colin Smith", "David Murphy",

    # Netherlands
    "Wesley Barresi", "Jeroen Smits", "Scott Edwards", "Atse Buurman", "Peter Cantrell",

    # Nepal
    "Binod Bhandari", "Subash Khakurel", "Aarif Sheikh",

    # UAE
    "Swapnil Patil", "Abdul Shakoor", "Ghulam Shabber",

    # Canada
    "Ashish Bagai", "Patricia Heron", "Jimmy Hansra", "Puskar Khadka",

    # Kenya
    "David Obuya", "Kennedy Otieno", "Morris Ouma", "Hiren Varaiya", "Aga Khan",
    
    # Namibia
    "Zane Green", "Gerrie Snyman", "JP Kotze", "Lohan Louwrens"
]
all_rounders = [
    # Australia
    "Shane Watson", "Andrew Symonds", "Steve Waugh", "Michael Bevan", "Mitchell Marsh", 
    "Glenn Maxwell", "Marcus Stoinis", "Moises Henriques", "Cameron Green", 
    "James Faulkner", "Keith Miller", "Tom Moody", "Simon O'Donnell", "Chris Green", 
    "Ron Archer", "Ken Mackay",

    # India
    "Kapil Dev", "Ravindra Jadeja", "Hardik Pandya", "Yuvraj Singh", "Irfan Pathan", 
    "Manoj Prabhakar", "Ravi Shastri", "Ajit Agarkar", "Stuart Binny", "Vijay Shankar", 
    "Vinoo Mankad", "Lala Amarnath", "Sandeep Patil", "Madan Lal", "Mohinder Amarnath", 
    "Karsan Ghavri", "Ravichandran Ashwin",

    # England
    "Ben Stokes", "Andrew Flintoff", "Chris Woakes", "Paul Collingwood", "Ian Botham", 
    "David Willey", "Sam Currie", "Moeen Ali", "Craig White", "Derek Pringle", 
    "Chris Lewis", "Tom Curran", "Dominic Cork", "Tony Greig", "Darren Gough", 
    "Trevor Bailey", "Pat Pocock",

    # Pakistan
    "Imran Khan", "Shahid Afridi", "Wasim Akram", "Abdul Razzaq", "Shoaib Malik", 
    "Mohammad Hafeez", "Sarfaraz Nawaz", "Shadab Khan", "Aamer Yamin", "Mohammad Nawaz", 
    "Azhar Mahmood", "Yasir Arafat", "Imad Wasim", "Anwar Ali", "Mudassar Nazar", 
    "Fawad Alam",

    # South Africa
    "Jacques Kallis", "Shaun Pollock", "Lance Klusener", "Dwayne Pretorius", "Chris Morris", 
    "Albie Morkel", "Brian McMillan", "Andile Phehlukwayo", "Ryan McLaren", 
    "Robin Peterson", "JP Duminy", "David Wiese", "Adrian Kuiper", "Clive Rice", 
    "Vernon Philander", "Morne Morkel", "Wayne Parnell", "Mark Boucher",

    # New Zealand
    "Richard Hadlee", "Chris Cairns", "Corey Anderson", "Scott Styris", "Jacob Oram", 
    "James Neesham", "Mitchell Santner", "Colin de Grandhomme", "Daniel Vettori", 
    "Nathan McCullum", "Daryl Mitchell", "Chris Harris", "Andre Adams", 
    "Gavin Larsen", "Dipak Patel", "Bruce Taylor", "Andrew Ellis",

    # Sri Lanka
    "Sanath Jayasuriya", "Angelo Mathews", "Thisara Perera", "Farveez Maharoof", 
    "Chaminda Vaas", "Russel Arnold", "Dilruwan Perera", "Jeevan Mendis", "Dilhara Lokuhettige", 
    "Asanka Gurusinha", "Nuwan Kulasekara", "Chamara Kapugedera", "Kaushalya Weeraratne", 
    "Upul Chandana", "Lahiru Madushanka", "Lasith Malinga", "Pramodya Wickramasinghe",

    # West Indies
    "Sir Garfield Sobers", "Carl Hooper", "Dwayne Bravo", "Andre Russell", "Kieron Pollard", 
    "Jason Holder", "Chris Gayle", "Carlos Brathwaite", "Viv Richards", "Roston Chase", 
    "Marlon Samuels", "Phil Simmons", "Keith Boyce", "Clive Lloyd", "Sherwin Campbell", 
    "Bernard Julien", "Fidel Edwards", "Ottis Gibson",

    # Bangladesh
    "Shakib Al Hasan", "Mahmudullah", "Mohammad Rafique", "Mashrafe Mortaza", 
    "Nasir Hossain", "Mohammad Saifuddin", "Soumya Sarkar", "Mohammad Ashraful", 
    "Khaled Mahmud", "Aminul Islam", "Alok Kapali", "Abdur Razzak", "Naimur Rahman", 
    "Ebadot Hossain", "Mohammad Naim", "Mohammad Mithun",

    # Zimbabwe
    "Heath Streak", "Andy Blignaut", "Elton Chigumbura", "Sean Williams", "Sikandar Raza", 
    "Paul Strang", "Guy Whittall", "Grant Flower", "Ryan Burl", "Douglas Hondo", 
    "Neil Johnson", "John Traicos", "Keith Dabengwa", "Mluleki Nkala", "Hamilton Masakadza", 
    "Dion Ebrahim", "Chamu Chibhabha", "Malcolm Waller",

    # Afghanistan
    "Mohammad Nabi", "Gulbadin Naib", "Rashid Khan", "Karim Janat", "Azmatullah Omarzai", 
    "Sharafuddin Ashraf", "Samiullah Shinwari", "Aftab Alam", "Fareed Ahmad", 
    "Shapoor Zadran", "Dawlat Zadran",

    # Ireland
    "Kevin O'Brien", "Paul Stirling", "George Dockrell", "Curtis Campher", "Andy McBrine", 
    "Simi Singh", "John Mooney", "Trent Johnston", "Andre Botha", "Kyle McCallan", 
    "Max Sorensen", "William McClintock",

    # Scotland
    "Josh Davey", "Safyaan Sharif", "Richie Berrington", "Michael Leask", "Gavin Hamilton", 
    "Gordon Goudie", "Craig Wallace", "Calum MacLeod", "Majid Haq", "Preston Mommsen", 
    "John Blain", "Paul Hoffmann",

    # Netherlands
    "Ryan ten Doeschate", "Roelof van der Merwe", "Pieter Seelaar", "Logan van Beek", 
    "Michael Rippon", "Bas de Leede", "Paul van Meekeren", "Tom Cooper", "Daan van Bunge", 
    "Eric Szwarczynski",

    # UAE
    "Rohan Mustafa", "Amjad Javed", "Ahmed Raza", "Mohammad Naveed", "Fahad Nawaz", 
    "Shaiman Anwar", "Khurram Khan", "Sultan Zarawani",

    # Nepal
    "Paras Khadka", "Dipendra Singh Airee", "Sharad Vesawkar", "Sompal Kami", 
    "Karan KC", "Bhim Sharki", "Rohit Paudel",

    # Canada
    "John Davison", "Ashish Bagai", "Jimmy Hansra", "Rizwan Cheema", "Henry Osinde", 
    "Zubin Surkari", "Sunil Dhaniram", "Abdool Samad",

    # Kenya
    "Thomas Odoyo", "Collins Obuya", "Steve Tikolo", "Rakep Patel", "Nehemiah Odhiambo", 
    "Tanmay Mishra", "Hiren Varaiya", "Ragheb Aga", "Duncan Allan",

    # Namibia
    "JJ Smit", "David Wiese", "Gerhard Erasmus", "Craig Williams", "Jan Frylinck", 
    "Bernard Scholtz", "Sarel Burger", "Nicolaas Scholtz"
]
bowlers = [
    # Australia
    "Glenn McGrath", "Shane Warne", "Brett Lee", "Mitchell Starc", "Pat Cummins", 
    "Nathan Lyon", "Mitchell Johnson", "Jason Gillespie", "Stuart Clark", 
    "Craig McDermott", "Damien Fleming", "Terry Alderman", "Nathan Bracken", 
    "Brad Hogg", "Adam Zampa", "Josh Hazlewood", "Shaun Tait", "Merv Hughes",

    # India
    "Anil Kumble", "Javagal Srinath", "Zaheer Khan", "Kapil Dev", "Harbhajan Singh", 
    "Ravichandran Ashwin", "Bhuvneshwar Kumar", "Mohammed Shami", "Ishant Sharma", 
    "Yuzvendra Chahal", "Jasprit Bumrah", "Ashish Nehra", "Venkatesh Prasad", 
    "Shardul Thakur", "Kuldeep Yadav", "Sreesanth", "Ravi Bishnoi", "Praveen Kumar",

    # England
    "James Anderson", "Stuart Broad", "Darren Gough", "Graeme Swann", "Adil Rashid", 
    "Chris Woakes", "Jofra Archer", "Steve Harmison", "Dominic Cork", "Andy Caddick", 
    "Mark Wood", "Phil DeFreitas", "David Willey", "John Emburey", "Monty Panesar", 
    "Gus Fraser", "Tim Bresnan", "Ryan Sidebottom", "Reece Topley", "Peter Such",

    # Pakistan
    "Wasim Akram", "Waqar Younis", "Shoaib Akhtar", "Saqlain Mushtaq", "Shahid Afridi", 
    "Imran Khan", "Mohammad Amir", "Shaheen Afridi", "Shadab Khan", "Danish Kaneria", 
    "Mushtaq Ahmed", "Abdul Qadir", "Mohammad Asif", "Umar Gul", "Mohammad Sami", 
    "Aqib Javed", "Yasir Shah", "Fazal Mahmood", "Junaid Khan", "Hassan Ali",

    # South Africa
    "Dale Steyn", "Makhaya Ntini", "Allan Donald", "Shaun Pollock", "Imran Tahir", 
    "Kagiso Rabada", "Lungi Ngidi", "Fanie de Villiers", "Paul Adams", "Morne Morkel", 
    "Vernon Philander", "Wayne Parnell", "Andre Nel", "Nicky Boje", "Charl Langeveldt", 
    "Tabraiz Shamsi", "Keshav Maharaj", "Pieter Malan", "Claude Henderson", "Chris Morris",

    # New Zealand
    "Trent Boult", "Tim Southee", "Daniel Vettori", "Shane Bond", "Richard Hadlee", 
    "Chris Martin", "Ewen Chatfield", "Kyle Mills", "Daryl Tuffey", "Mitchell McClenaghan", 
    "Lockie Ferguson", "Jeetan Patel", "Bruce Taylor", "Neil Wagner", "Mark Gillespie", 
    "Jacob Duffy", "Matt Henry", "Ish Sodhi", "Ajaz Patel", "Simon Doull",

    # Sri Lanka
    "Muttiah Muralitharan", "Chaminda Vaas", "Lasith Malinga", "Rangana Herath", 
    "Nuwan Kulasekara", "Dilhara Fernando", "Ajantha Mendis", "Suranga Lakmal", 
    "Pramodya Wickramasinghe", "Dushmantha Chameera", "Angelo Mathews", 
    "Shaminda Eranga", "Lahiru Kumara", "Dilshan Madushanka", "Ruchira Perera", 
    "Sachithra Senanayake", "Upul Chandana", "Thilan Thushara", "Vishwa Fernando",

    # West Indies
    "Courtney Walsh", "Curtly Ambrose", "Michael Holding", "Joel Garner", "Malcolm Marshall", 
    "Andy Roberts", "Ian Bishop", "Dwayne Bravo", "Fidel Edwards", "Kemar Roach", 
    "Sunil Narine", "Ravi Rampaul", "Jason Holder", "Shannon Gabriel", "Jerome Taylor", 
    "Devendra Bishoo", "Veerasammy Permaul", "Carlos Brathwaite", "Keemo Paul", 
    "Alzarri Joseph", "Obed McCoy", "Sheldon Cottrell", "Samuel Badree",

    # Bangladesh
    "Mashrafe Mortaza", "Mustafizur Rahman", "Taskin Ahmed", "Abdur Razzak", "Rubel Hossain", 
    "Shakib Al Hasan", "Mehidy Hasan", "Mohammad Rafique", "Enamul Haque Jr", 
    "Nazmul Islam", "Shafiul Islam", "Al-Amin Hossain", "Tapash Baisya", 
    "Khaled Mahmud", "Mohammad Saifuddin", "Razzak Hossain",

    # Zimbabwe
    "Heath Streak", "Henry Olonga", "Andy Blignaut", "Paul Strang", "Bryan Strang", 
    "Eddo Brandes", "Kyle Jarvis", "Tinashe Panyangara", "Ray Price", "Graeme Cremer", 
    "Blessing Muzarabani", "Tendai Chatara", "John Nyumbu", "Mpumelelo Mbangwa", 
    "Prosper Utseya", "Chris Mpofu", "Sean Ervine", "Richard Ngarava",

    # Afghanistan
    "Rashid Khan", "Mujeeb Ur Rahman", "Naveen-ul-Haq", "Hamid Hassan", "Dawlat Zadran", 
    "Shapoor Zadran", "Fareed Ahmad", "Zahir Khan", "Mohammad Nabi", 
    "Aftab Alam", "Gulbadin Naib",

    # Ireland
    "Boyd Rankin", "George Dockrell", "Tim Murtagh", "Barry McCarthy", 
    "Craig Young", "Joshua Little", "Andy McBrine", "Peter Chase", 
    "Tyrone Kane", "Kevin O'Brien", "Stuart Thompson",

    # Scotland
    "Safyaan Sharif", "Mark Watt", "Josh Davey", "Gavin Hamilton", "Majid Haq", 
    "John Blain", "Alasdair Evans", "Bradley Wheal", "Chris Sole", "Matthew Cross",

    # Netherlands
    "Timm van der Gugten", "Paul van Meekeren", "Logan van Beek", "Pieter Seelaar", 
    "Fred Klaassen", "Ahsan Malik", "Michael Rippon", "Vivian Kingma", 
    "Ryan ten Doeschate", "Mudassar Bukhari",

    # UAE
    "Zahoor Khan", "Mohammad Naveed", "Ahmed Raza", "Rohan Mustafa", 
    "Qadeer Ahmed", "Junaid Siddique", "Amjad Javed", "Sultan Zarawani", "Fayyaz Ahmed",

    # Nepal
    "Sandeep Lamichhane", "Karan KC", "Sompal Kami", "Lalit Rajbanshi", 
    "Dipendra Singh Airee", "Basir Ahmad", "Kushal Bhurtel",

    # Canada
    "Henry Osinde", "Ashish Bagai", "Rizwan Cheema", "Jimmy Hansra", 
    "Abzal Dean", "Parth Desai", "Harvir Baidwan",

    # Kenya
    "Thomas Odoyo", "Collins Obuya", "Peter Ongondo", "Ragheb Aga", 
    "Nehemiah Odhiambo", "Martin Suji", "Lameck Onyango",

    # Namibia
    "Ruben Trumpelmann", "Bernard Scholtz", "David Wiese", "Jan Frylinck", 
    "JJ Smit", "Christi Viljoen", "Gerrie Snyman"
]
pitch_conditions = [
    "Green Pitch",
    "Dry/Dusty Pitch",
    "Flat Pitch",
    "Hard Pitch",
    "Soft Pitch",
    "Slow Pitch",
    "Cracked Pitch",
    "Damp/Wet Pitch",
    "Sticky Wicket"
]
# Function to filter dropdown menu based on user input
def show_selection():
    selected_players = [player_var[i].get() for i in range(11)]
    label.config(text=f"Selected Players: {selected_players}")

# Create the main window
root = tk.Tk()
root.title("Team Selector")

# Combine all players into a single list
all_players = batsmen + bowlers + all_rounders + wicketkeepers

# Tkinter variables to store the dropdown selections for each player
player_var = [tk.StringVar() for _ in range(11)]

# Create 11 dropdown menus, each labeled Player 1 to Player 11
for i in range(11):
    label = tk.Label(root, text=f"Player {i+1}", font=("Arial", 12))
    label.pack(padx=10, pady=5)
    
    player_menu = ttk.Combobox(root, textvariable=player_var[i])
    player_menu['values'] = all_players
    player_menu.pack(padx=20, pady=5)

# Create a label to display the selected players
label = tk.Label(root, text="Selected Players: None")
label.pack(padx=20, pady=20)

# Create the Submit button
submit_button = tk.Button(root, text="Submit", command=show_selection)
submit_button.pack(padx=20, pady=10)

# Run the application
root.mainloop()
