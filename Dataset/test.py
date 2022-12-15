import pandas as pd
import numpy as np
import calendar
from geopy.geocoders import Nominatim
import time
from pprint import pprint
app = Nominatim(user_agent="tutorial")

df = pd.read_csv("disasters.csv")
pd.set_option('display.max_columns', None)

country_list = ['Andorra','United Arab Emirates','Afghanistan','Antigua and Barbuda','Anguilla','Albania','Armenia','Netherlands Antilles','Angola','Antarctica','Argentina','American Samoa','Austria','Australia','Aruba','Azerbaijan','Bosnia and Herzegovina','Barbados','Bangladesh','Belgium','Burkina Faso','Bulgaria','Bahrain','Burundi','Benin','Bermuda','Brunei','Bolivia','Brazil','Bahamas','Bhutan','Bouvet Island','Botswana','Belarus','Belize','Canada','Cocos [Keeling] Islands','Congo [DRC]','Central African Republic','Congo [Republic]','Switzerland','Cook Islands','Chile','Cameroon','China','Colombia','Costa Rica','Cuba','Cape Verde','Christmas Island','Cyprus','Czech Republic','Germany','Djibouti','Denmark','Dominica','Dominican Republic','Algeria','Ecuado'","'Estonia','Egypt','Western Sahara','Eritrea','Spain','Ethiopia','Finland','Fiji','Falkland Islands [Islas Malvinas]','Micronesia','Faroe Islands','France','Gabon','United Kingdom','Grenada','Georgia','French Guiana','Guernsey','Ghana','Gibralta'","'Greenland','Gambia','Guinea','Guadeloupe','Equatorial Guinea','Greece','South Georgia and the South Sandwich Islands','Guatemala','Guam','Guinea-Bissau','Guyana','Gaza Strip','Hong Kong','Heard Island and McDonald Islands','Honduras','Croatia','Haiti','Hungary','Indonesia','Ireland','Israel','Isle of Man','India','British Indian Ocean Territory','Iraq','Iran','Iceland','Italy','Jersey','Jamaica','Jordan','Japan','Kenya','Kyrgyzstan','Cambodia','Kiribati','Comoros','Saint Kitts and Nevis','North Korea','South Korea','Kuwait','Cayman Islands','Kazakhstan','Laos','Lebanon','Saint Lucia','Liechtenstein','Sri Lanka','Liberia','Lesotho','Lithuania','Luxembourg','Latvia','Libya','Morocco','Monaco','Moldova','Montenegro','Madagasca'","'Marshall Islands','Macedonia [FYROM]','Mali','Myanmar [Burma]','Mongolia','Macau','Northern Mariana Islands','Martinique','Mauritania','Montserrat','Malta','Mauritius','Maldives','Malawi','Mexico','Malaysia','Mozambique','Namibia','New Caledonia','Nige'","'Norfolk Island','Nigeria','Nicaragua','Netherlands','Norway','Nepal','Nauru','Niue','New Zealand','Oman','Panama','Peru','French Polynesia','Papua New Guinea','Philippines','Pakistan','Poland','Saint Pierre and Miquelon','Pitcairn Islands','Puerto Rico','Palestinian Territories','Portugal','Palau','Paraguay','Qata'","'Réunion','Romania','Serbia','Russia','Rwanda','Saudi Arabia','Solomon Islands','Seychelles','Sudan','Sweden','Singapore','Saint Helena','Slovenia','Svalbard and Jan Mayen','Slovakia','Sierra Leone','San Marino','Senegal','Somalia','Suriname','São Tomé and Príncipe','El Salvado'","'Syria','Swaziland','Turks and Caicos Islands','Chad','French Southern Territories','Togo','Thailand','Tajikistan','Tokelau','Timor-Leste','Turkmenistan','Tunisia','Tonga','Turkey','Trinidad and Tobago','Tuvalu','Taiwan','Tanzania','Ukraine','Uganda','U.S. Minor Outlying Islands','United States','Uruguay','Uzbekistan','Vatican City','Saint Vincent and the Grenadines','Venezuela','British Virgin Islands','U.S. Virgin Islands','Vietnam','Vanuatu','Wallis and Futuna','Samoa','Kosovo','Yemen','Mayotte','South Africa','Zambia','Zimbabwe']
disaster_types = ['Drought', 'Earthquake', 'Extreme temperature', 'Flood', 'Storm', 'Volcanic activity', 'Wildfire']

df = df[df['Country'].isin(country_list)]
df = df[df['Disaster Type'].isin(disaster_types)]

df = df.drop('Seq', axis=1)
df = df.drop('Glide', axis=1)
df = df.drop('Disaster Group', axis=1)
df = df.drop('Disaster Subsubtype', axis=1)
df = df.drop('Event Name', axis=1)
df = df.drop('OFDA Response', axis=1)
df = df.drop('Appeal', axis=1)
df = df.drop('Associated Dis', axis=1)
df = df.drop('Associated Dis2', axis=1)
df = df.drop('Declaration', axis=1)
df = df.drop('Aid Contribution', axis=1)
df = df.drop('Local Time', axis=1)
df = df.drop('Adm Level', axis=1)
df = df.drop('Admin1 Code', axis=1)
df = df.drop('Admin2 Code', axis=1)
df = df.drop('Geo Locations', axis=1)

df["CPI"].fillna(100, inplace = True)
df["Total Damages Adjusted ('000 US$)"] = (df["Total Damages ('000 US$)"].astype(float) / (df["CPI"].astype(float)/100)).round(2)

for value in df["Location"]:
    if value != None:
        location = app.geocode("Nairobi, Kenya").raw
        df["Latitude"] = location['lat']
        df["Longitude"] = location['lon']

print(df.head(30000))
