#Regions and groups listings

regions = ['Africa (Region)',
 'Asia and pacific',
 'Australia and New Zealand',
 'Central Asia and the Caucasus',
 'Caribbean',
 'Central America',
 'East asia',
 'Eastern Europe',
 'Europe',
 'Middle East (Region)',
 'North Africa',
 'North America',
 'Pacific Islands',
 'South Asia',
 'Southeast Asia',
 'South America',
 'Sub-saharan Africa (Region)',
 'Western Europe',
 'Western Hemisphere (Region)']

groups = ['Major Advanced economies (G7)',
 'Asean-5',
 'Emerging and developing asia',
 'European union',
 'Euro area',
 'Other advanced economies',
 'Emerging market and developing economies',
 'Sub-saharan Africa',
 'Latin america and the Caribbean',
 'Emerging and developing europe',
 'Middle east and Central asia']

#Economic Groups

# Major Advanced Economies
major_advanced_economies = ["Canada", "France", "Germany", "Italy", "Japan", "United Kingdom", "United States"]

# Other Advanced Economies
other_advanced_economies = ["Andorra", "Australia", "Czech Republic", "Denmark", 
                            "Hong Kong SAR", "Iceland", "Israel", "Republic of Korea", "Macao SAR", 
                            "New Zealand", "Norway", "Puerto Rico", "San Marino", "Singapore", "Sweden", "Switzerland", 
                            "Taiwan Province of China"]

# European Union
european_union = ["Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czech Republic", 
                  "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary",
                  "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", 
                  "Netherlands", "Poland", "Portugal", "Romania", "Slovak Republic", "Slovenia", "Spain", "Sweden"]

# ASEAN-5
asean_5 = ["Indonesia", "Malaysia", "Philippines", "Singapore", "Thailand"]

# Euro Area
euro_area = ["Austria", "Belgium", "Croatia", "Cyprus", "Estonia", "Finland", "France", "Germany", "Greece", "Ireland",
             "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Portugal", "Slovak Republic", 
             "Slovenia", "Spain"]

# Emerging Developing Asia
emerging_developing_asia = ["Bangladesh", "Bhutan", "Brunei Darussalam", "Cambodia", "People's Republic of China", "Fiji", "India", "Indonesia",
                            "Kiribati", "Lao P.D.R.", "Malaysia", "Maldives", "Marshall Islands", "Fed. States of Micronesia", 
                            "Mongolia", "Myanmar", "Nauru", "Nepal", "Palau", "Papua New Guinea", "Philippines", "Samoa",
                            "Solomon Islands", "Sri Lanka", "Thailand", "Timor-Leste", "Tonga", "Tuvalu", "Vanuatu",
                            "Vietnam"]

# Emerging Developing Europe
emerging_developing_europe = ["Albania", "Belarus", "Bosnia and Herzegovina", "Bulgaria", "Hungary", "Kosovo", "Moldova",
                              "Montenegro", "North Macedonia", "Poland", "Romania", "Russian Federation", "Serbia", "Republic of Türkiye", "Ukraine"]

# Latin American and Caribbean
latin_american_caribbean = ["Antigua and Barbuda", "Argentina", "Aruba", "The Bahamas", "Barbados",
                            "Belize", "Bolivia", "Brazil", "Chile", "Colombia", "Costa Rica", "Dominica", 
                            "Dominican Republic", "Ecuador", "El Salvador", "Grenada", "Guatemala", "Guyana",
                            "Haiti", "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Paraguay", "Peru", 
                            "Suriname", "Trinidad and Tobago", "Uruguay", "Venezuela"]

# Middle East and Central Asia
middle_east_central_asia = ["Afghanistan", "Algeria", "Armenia", "Azerbaijan", "Bahrain", "Djibouti", "Egypt", "Georgia",
                            "Iran", "Iraq", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyz Republic", "Lebanon", "Libya",
                            "Mauritania", "Morocco", "Oman", "Pakistan", "Qatar", "Saudi Arabia", "Somalia", "Sudan",
                            "Syria", "Tajikistan", "Tunisia", "Turkmenistan", "United Arab Emirates", "Uzbekistan", 
                            "West Bank and Gaza", "Yemen"]

# Sub-Saharan Africa
sub_saharan_africa = ["Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", 
                      "Central African Republic", "Chad", "Comoros", "Dem. Rep. of the Congo",
                      "Republic of Congo", "Côte d'Ivoire", "Equatorial Guinea", "Eritrea", "Eswatini",
                      "Ethiopia", "Gabon", "The Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho",
                      "Liberia", "Madagascar", "Malawi", "Mali", "Mauritius", "Mozambique", "Namibia", "Niger",
                      "Nigeria", "Rwanda", "São Tomé and Príncipe", "Senegal", "Seychelles", "Sierra Leone",
                      "South Africa", "Republic of South Sudan", "Tanzania", "Togo", "Uganda", "Zambia", "Zimbabwe"]

emerging_market_developing_economies = emerging_developing_asia + emerging_developing_europe + sub_saharan_africa + middle_east_central_asia + latin_american_caribbean


#Continents and regions

africa_region = [
    "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi",
    "Cabo Verde", "Cameroon", "Central African Republic", "Chad", "Comoros",
    "Côte d'Ivoire", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea",
    "Eswatini", "Ethiopia", "Gabon", "The Gambia", "Ghana", "Guinea",
    "Guinea-Bissau", "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar",
    "Malawi", "Mali", "Mauritania", "Mauritius", "Morocco", "Mozambique", "Namibia",
    "Niger", "Nigeria", "Rwanda", "São Tomé and Príncipe", "Senegal", "Seychelles",
    "Sierra Leone", "Somalia", "South Africa", "Republic of South Sudan", "Sudan", "Tanzania",
    "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"
]

asia_and_pacific = [
    "Afghanistan", "Armenia", "Azerbaijan", "Bangladesh", "Bhutan",
    "Brunei Darussalam", "Cambodia", "People's Republic of China", "Georgia", "India", "Indonesia",
    "Iran", "Iraq", "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyz Republic",
    "Lao P.D.R.", "Lebanon", "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal",
    "Pakistan", "Philippines", "Qatar", "Saudi Arabia", "Sri Lanka", "Syria",
    "Tajikistan", "Thailand", "Timor-Leste", "Turkmenistan", "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"
]
australia_and_new_zealand = ["Australia", "New Zealand"]

central_asia_and_the_caucasus = ["Armenia", "Azerbaijan", "Georgia", "Kazakhstan", "Kyrgyz Republic", "Tajikistan", "Turkmenistan", "Uzbekistan"]

caribbean = ["Antigua and Barbuda", "Barbados", "Dominica", "Grenada", "Haiti", "The Bahamas","Jamaica", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Trinidad and Tobago"]

central_america = ["Belize", "Costa Rica", "El Salvador", "Guatemala", "Honduras", "Nicaragua", "Panama"]

east_asia = ["People's Republic of China", "Japan","Republic of Korea", "Mongolia", "Taiwan Province of China"]

eastern_europe = ["Belarus", "Bulgaria", "Moldova", "Romania", "Russian Federation", "Ukraine"]

europe = [
    "Albania", "Andorra", "Austria", "Belgium", "Bosnia and Herzegovina", "Croatia", "Cyprus", "Czech Republic",
    "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kosovo",
    "Latvia", "Lithuania", "Luxembourg", "Malta", "Montenegro", "Netherlands", "North Macedonia",
    "Norway", "Poland", "Portugal", "Serbia", "Slovenia", "Spain", "Sweden", "Switzerland", "United Kingdom"
]

middle_east_region = ["Bahrain", "Cyprus", "Iran", "Iraq", "Israel", "Jordan", "Kuwait", "Lebanon", "Oman", "Qatar", "Saudi Arabia", "Syria", "Republic of Türkiye", "United Arab Emirates", "Yemen"]

north_africa = ["Algeria", "Egypt", "Libya", "Mauritania", "Morocco", "Sudan", "Tunisia"]

north_america = ["Canada", "United States"]

pacific_islands = ["Fiji", "Kiribati", "Marshall Islands", "Fed. States of Micronesia", "Nauru", "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"]

south_asia = ["Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives", "Nepal", "Pakistan", "Sri Lanka"]

southeast_asia = ["Brunei Darussalam", "Cambodia", "Indonesia", "Lao P.D.R.", "Malaysia", "Myanmar", "Philippines", "Singapore", "Thailand", "Timor-Leste", "Vietnam"]

south_america = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]

sub_saharan_africa_region = [
    "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon", 
    "Central African Republic", "Chad", "Comoros", "Dem. Rep. of the Congo", 
    "Republic of Congo", "Côte d'Ivoire", "Equatorial Guinea", "Eritrea", "Eswatini", 
    "Ethiopia", "Gabon", "The Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", 
    "Liberia", "Madagascar", "Malawi", "Mali", "Mauritius", "Mozambique", "Namibia", "Niger", 
    "Nigeria", "Rwanda", "São Tomé and Príncipe", "Senegal", "Seychelles", "Sierra Leone", 
    "South Africa", "Republic of South Sudan", "Tanzania", "Togo", "Uganda", "Zambia", "Zimbabwe"
]

western_europe = [
    "Austria", "Belgium", "France", "Germany", "Ireland", "Italy", "Luxembourg", "Netherlands", "Portugal", "Spain", "United Kingdom"]
western_hemisphere_region = central_america + south_america


regions_dict = {'africa_region':africa_region,
'asia_and_pacific':asia_and_pacific,
'australia_and_new_zealand':australia_and_new_zealand,
'central_asia_and_the_caucasus':central_asia_and_the_caucasus,
'caribbean':caribbean,
'central_america':central_america,
'east_asia':east_asia,
'eastern_europe':eastern_europe,
'europe':europe,
'middle_east_region':middle_east_region,
'north_africa':north_africa,
'north_america':north_america,
'pacific_islands':pacific_islands,
'south_asia':south_asia,
'southeast_asia':southeast_asia,
'south_america':south_america,
'sub_saharan_africa_region':sub_saharan_africa_region,
'western_europe':western_europe,
'western_hemisphere_region':western_hemisphere_region}

groups_dict = {'major_advanced_economies_g7':major_advanced_economies,
'other_advanced_economies':other_advanced_economies,
'european_union':european_union,
'asean_5':asean_5,
'euro_area':euro_area,
'emerging_market_and_developing_economies':emerging_market_developing_economies,
'emerging_and_developing_asia':emerging_developing_asia,
'emerging_and_developing_europe':emerging_developing_europe,
'latin_america_and_the_caribbean':latin_american_caribbean,
'middle_east_and_central_asia':middle_east_central_asia,
'sub_saharan_africa':sub_saharan_africa}

world_list = ['Honduras',
 'Algeria',
 'Jamaica',
 'Tajikistan',
 'Saint Kitts and Nevis',
 'Republic of Congo',
 'Nauru',
 'Burundi',
 'Russian Federation',
 'Brazil',
 'The Bahamas',
 'Cambodia',
 'Portugal',
 'Republic of Türkiye',
 'Kyrgyz Republic',
 'Iran',
 'Central African Republic',
 'Zambia',
 'Ireland',
 'Costa Rica',
 'Trinidad and Tobago',
 'Kuwait',
 'Guyana',
 'Israel',
 'Sri Lanka',
 'Lithuania',
 'Ethiopia',
 'Morocco',
 'Philippines',
 'Bahrain',
 'Afghanistan',
 'North Macedonia',
 'The Gambia',
 'Japan',
 'Andorra',
 'Vietnam',
 'Spain',
 'Mexico',
 'Iceland',
 'Turkmenistan',
 'Timor-Leste',
 'Paraguay',
 'Egypt',
 'Latvia',
 'France',
 'Saudi Arabia',
 'Belarus',
 'Bulgaria',
 'Albania',
 'Denmark',
 'Uruguay',
 'Puerto Rico',
 'Guinea',
 'Djibouti',
 'Palau',
 'Namibia',
 'Togo',
 'Moldova',
 'Cabo Verde',
 'Cameroon',
 'Dominican Republic',
 'Mali',
 'Senegal',
 'Guatemala',
 'Papua New Guinea',
 'Nicaragua',
 'Ukraine',
 'Syria',
 'Peru',
 'San Marino',
 'Sweden',
 'Fed. States of Micronesia',
 'Saint Lucia',
 'Rwanda',
 'Dem. Rep. of the Congo',
 'Switzerland',
 'Libya',
 'Belize',
 'Armenia',
 'Gabon',
 'Bhutan',
 'Brunei Darussalam',
 'Czech Republic',
 'Mauritania',
 'Lao P.D.R.',
 'Antigua and Barbuda',
 'Jordan',
 'Norway',
 'Dominica',
 'Equatorial Guinea',
 'Madagascar',
 'Guinea-Bissau',
 'Mongolia',
 'Argentina',
 'New Zealand',
 'Azerbaijan',
 'Bosnia and Herzegovina',
 'Solomon Islands',
 'Samoa',
 'Eswatini',
 'Kenya',
 'United States',
 'Seychelles',
 'Finland',
 'Chile',
 'Malaysia',
 'Saint Vincent and the Grenadines',
 'Lesotho',
 'Qatar',
 'Cyprus',
 'Poland',
 'Slovak Republic',
 'Burkina Faso',
 'Taiwan Province of China',
 'Montenegro',
 'Lebanon',
 'Colombia',
 'El Salvador',
 'Panama',
 'Angola',
 'Niger',
 'Canada',
 'Nigeria',
 'Venezuela',
 'Indonesia',
 'Kiribati',
 'Botswana',
 'Uzbekistan',
 'Suriname',
 'Myanmar',
 'Italy',
 'United Kingdom',
 'Iraq',
 'Australia',
 'Bangladesh',
 'Benin',
 'Kosovo',
 'Tanzania',
 'Thailand',
 'Hungary',
 'São Tomé and Príncipe',
 'United Arab Emirates',
 'Haiti',
 'Tonga',
 'Luxembourg',
 'Pakistan',
 'Yemen',
 'Eritrea',
 'Austria',
 'Bolivia',
 'Malawi',
 'Somalia',
 'Slovenia',
 'Macao SAR',
 'Germany',
 'South Africa',
 'Maldives',
 'Aruba',
 "Côte d'Ivoire",
 'Republic of Korea',
 'Mozambique',
 'Netherlands',
 'Comoros',
 'Croatia',
 'Estonia',
 'Serbia',
 'Georgia',
 'Liberia',
 'Sudan',
 'Uganda',
 'Nepal',
 'Zimbabwe',
 'Barbados',
 'Singapore',
 'Ecuador',
 'Mauritius',
 'India',
 'Republic of South Sudan',
 'Hong Kong SAR',
 'Grenada',
 'Chad',
 'Ghana',
 'Tunisia',
 'Greece',
 'Oman',
 'Fiji',
 'Vanuatu',
 'West Bank and Gaza',
 'Marshall Islands',
 'Belgium',
 'Malta',
 'Romania',
 'Sierra Leone',
 'Kazakhstan',
 "People's Republic of China",
 'Tuvalu']