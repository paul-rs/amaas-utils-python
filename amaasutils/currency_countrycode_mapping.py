
# country code used is alpha 3 country code

currency_countrycode_mapping = {'AED':'ARE',
'AFN':'AFG',
'ALL':'ALB',
'AMD':'ARM',
'ANG':'ANT',
'AOA':'AGO',
'ARS':'ARG',
'AUD':'AUS',
'AWG':'ABW',
'AZN':'AZE',
'BAM':'BIH',
'BBD':'BRB',
'BDT':'BGD',
'BGN':'BGR',
'BHD':'BHR',
'BIF':'BDI',
'BMD':'BMU',
'BND':'BRN',
'BOB':'BOL',
'BRL':'BRA',
'BSD':'BHS',
'BTN':'BTN',
'BWP':'BWA',
'BYR':'BLR',
'BZD':'BLZ',
'CAD':'CAN',
'CDF':'COD',
'XAF':'CAF',
'CHF':'CHE',
'CLP':'CHL',
'CNH':'CHN',
'CNY':'CHN',
'COP':'COL',
'CRC':'CRI',
'CUP':'CUB',
'CVE':'CPV',
'CZK':'CZE',
'DJF':'DJI',
'DKK':'DNK',
'DOP':'DOM',
'DZD':'DZA',
'ECS':'ECU',
'EGP':'EGY',
'ERN':'ERI',
'ETB':'ETH',
'FJD':'FJI',
'FKP':'FLK',
'GBP':'GBR',
'GEL':'GEO',
'GHS':'GHA',
'GIP':'GIB',
'GMD':'GMB',
'GNF':'GIN',
'GTQ':'GTM',
'GYD':'GUY',
'HKD':'HKG',
'HNL':'HND',
'HRK':'HRV',
'HTG':'HTI',
'HUF':'HUN',
'IDR':'IDN',
'ILS':'ISR',
'INR':'IND',
'IQD':'IRQ',
'ISK':'ISL',
'JMD':'JAM',
'JOD':'JOR',
'JPY':'JPN',
'KES':'KEN',
'KGS':'KGZ',
'KHR':'KHM',
'KRW':'KOR',
'KWD':'KWT',
'KYD':'CYM',
'KZT':'KAZ',
'LAK':'LAO',
'LBP':'LBN',
'LKR':'LKA',
'LRD':'LBR',
'LSL':'LSO',
'LYD':'LBY',
'MAD':'MAR',
'MDL':'MDA',
'MGA':'MDG',
'MKD':'MKD',
'MMK':'MMR',
'MNT':'MNG',
'MOP':'MAC',
'MRO':'MRT',
'MUR':'MUS',
'MVR':'MDV',
'MWK':'MWI',
'MXN':'MEX',
'MYR':'MYS',
'MZN':'MOZ',
'NAD':'NAM',
'NGN':'NGA',
'NIO':'NIC',
'NOK':'NOR',
'NPR':'NPL',
'NZD':'NZL',
'OMR':'OMN',
'PAB':'PAN',
'PEN':'PER',
'XPF':'PYF',
'PGK':'PNG',
'PHP':'PHL',
'PKR':'PAK',
'PLN':'POL',
'PYG':'PRY',
'QAR':'QAT',
'RON':'ROU',
'RSD':'SRB',
'RUB':'RUS',
'RWF':'RWA',
'SAR':'SAU',
'SBD':'SLB',
'SCR':'SYC',
'SEK':'SWE',
'SGD':'SGP',
'SHP':'SHN',
'SLL':'SLE',
'SOS':'SOM',
'SRD':'SUR',
'STD':'STP',
'SVC':'SLV',
'SZL':'SWZ',
'THB':'THA',
'TJS':'TJK',
'TND':'TUN',
'TOP':'TON',
'TRY':'TUR',
'TTD':'TTO',
'TWD':'TWN',
'TZS':'TZA',
'UAH':'UKR',
'UGX':'UGA',
'USD':'USA',
'UYU':'URY',
'UZS':'UZB',
'VEF':'VEN',
'VND':'VNM',
'VUV':'VUT',
'WST':'WSM',
'YER':'YEM',
'ZAR':'ZAF',
'ZMW':'ZMB',
}

def currency_to_countrycode(currency):
    return currency_countrycode_mapping.get(currency,None)

def countrycode_to_currency(country):
    for currency, countrycode in currency_countrycode_mapping.items():
        if countrycode == country:
            return currency
    return None