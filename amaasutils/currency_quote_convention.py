

currency_quote_convention = {
'XPT':'XPTUSD',
'XPD':'XPDUSD',
'XAU':'XAUUSD',
'XAG':'XAGUSD',
'WST':'WSTUSD',
'ZMW':'USDZMW',
'ZAR':'USDZAR',
'YER':'USDYER',
'XPF':'USDXPF',
'XOF':'USDXOF',
'XCD':'USDXCD',
'XAF':'USDXAF',
'VUV':'USDVUV',
'VND':'USDVND',
'VEF':'USDVEF',
'UZS':'USDUZS',
'UYU':'USDUYU',
'UGX':'USDUGX',
'UAH':'USDUAH',
'TZS':'USDTZS',
'TWD':'USDTWD',
'TTD':'USDTTD',
'TRY':'USDTRY',
'TND':'USDTND',
'TMM':'USDTMM',
'TJS':'USDTJS',
'THB':'USDTHB',
'SZL':'USDSZL',
'SYP':'USDSYP',
'SVC':'USDSVC',
'STD':'USDSTD',
'SRD':'USDSRD',
'SOS':'USDSOS',
'SLL':'USDSLL',
'SKK':'USDSKK',
'SIT':'USDSIT',
'SGD':'USDSGD',
'SEK':'USDSEK',
'SDG':'USDSDG',
'SCR':'USDSCR',
'SAR':'USDSAR',
'RWF':'USDRWF',
'RUB':'USDRUB',
'RSD':'USDRSD',
'RON':'USDRON',
'QAR':'USDQAR',
'PYG':'USDPYG',
'PTE':'USDPTE',
'PLN':'USDPLN',
'PKR':'USDPKR',
'PHP':'USDPHP',
'PEN':'USDPEN',
'PAB':'USDPAB',
'OMR':'USDOMR',
'NPR':'USDNPR',
'NOK':'USDNOK',
'NLG':'USDNLG',
'NIO':'USDNIO',
'NGN':'USDNGN',
'NAD':'USDNAD',
'MZN':'USDMZN',
'MYR':'USDMYR',
'MXN':'USDMXN',
'MWK':'USDMWK',
'MVR':'USDMVR',
'MUR':'USDMUR',
'MRO':'USDMRO',
'MOP':'USDMOP',
'MNT':'USDMNT',
'MMK':'USDMMK',
'MKD':'USDMKD',
'MGA':'USDMGA',
'MDL':'USDMDL',
'MAD':'USDMAD',
'LYD':'USDLYD',
'LVL':'USDLVL',
'LUF':'USDLUF',
'LTL':'USDLTL',
'LSL':'USDLSL',
'LRD':'USDLRD',
'LKR':'USDLKR',
'LBP':'USDLBP',
'LAK':'USDLAK',
'KZT':'USDKZT',
'KWD':'USDKWD',
'KRW':'USDKRW',
'KPW':'USDKPW',
'KMF':'USDKMF',
'KHR':'USDKHR',
'KGS':'USDKGS',
'KES':'USDKES',
'JPY':'USDJPY',
'JOD':'USDJOD',
'JMD':'USDJMD',
'ITL':'USDITL',
'ISK':'USDISK',
'IRR':'USDIRR',
'IQD':'USDIQD',
'INR':'USDINR',
'ILS':'USDILS',
'IDR':'USDIDR',
'HUF':'USDHUF',
'HTG':'USDHTG',
'HRK':'USDHRK',
'HNL':'USDHNL',
'HKD':'USDHKD',
'GYD':'USDGYD',
'GTQ':'USDGTQ',
'GRD':'USDGRD',
'GNF':'USDGNF',
'GMD':'USDGMD',
'GHS':'USDGHS',
'GEL':'USDGEL',
'FRF':'USDFRF',
'FIM':'USDFIM',
'ETB':'USDETB',
'ESP':'USDESP',
'ERN':'USDERN',
'EGP':'USDEGP',
'EEK':'USDEEK',
'ECS':'USDECS',
'DZD':'USDDZD',
'DOP':'USDDOP',
'DKK':'USDDKK',
'DJF':'USDDJF',
'DEM':'USDDEM',
'CZK':'USDCZK',
'CVE':'USDCVE',
'CUP':'USDCUP',
'CRC':'USDCRC',
'COP':'USDCOP',
'CNY':'USDCNY',
'CNH':'USDCNH',
'CLP':'USDCLP',
'CHF':'USDCHF',
'CDF':'USDCDF',
'CAD':'USDCAD',
'BZD':'USDBZD',
'BYR':'USDBYR',
'BTN':'USDBTN',
'BSD':'USDBSD',
'BRL':'USDBRL',
'BOB':'USDBOB',
'BND':'USDBND',
'BMD':'USDBMD',
'BIF':'USDBIF',
'BHD':'USDBHD',
'BGN':'USDBGN',
'BEF':'USDBEF',
'BDT':'USDBDT',
'BBD':'USDBBD',
'BAM':'USDBAM',
'AZN':'USDAZN',
'AWG':'USDAWG',
'ATS':'USDATS',
'ARS':'USDARS',
'AOA':'USDAOA',
'ANG':'USDANG',
'AMD':'USDAMD',
'ALL':'USDALL',
'AFN':'USDAFN',
'AED':'USDAED',
'ADP':'USDADP',
'TOP':'TOPUSD',
'SHP':'SHPUSD',
'SBD':'SBDUSD',
'PGK':'PGKUSD',
'NZD':'NZDUSD',
'KYD':'KYDUSD',
'IEP':'IEPUSD',
'GIP':'GIPUSD',
'GBP':'GBPUSD',
'FKP':'FKPUSD',
'FJD':'FJDUSD',
'EUR':'EURUSD',
'BWP':'BWPUSD',
'AUD':'AUDUSD',
}

def get_currency_quote_convention(currency):
    return currency_quote_convention.get(currency,"None")