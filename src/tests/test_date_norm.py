"""
Test number normaliser
"""

from techiaith.tts.testun.date_norm import expand_date_welsh

tests = [
    [
        "1/1/2020",
        "cyntaf o Ionawr dwy fil ac ugain",
    ],  # arolwg Twitter yn rhoi 53% o blaid "ac ugain vs 19% "dau ddeg" (n=206)
    ["02/2/2023", "ail o Chwefror dwy fil dau ddeg tri"],
    ["3/03/2021", "trydydd o Fawrth dwy fil dau ddeg un"],
    ["04/04/2021", "pedwerydd o Ebrill dwy fil dau ddeg un"],
    ["5/5/1995", "pumed o Fai mil naw naw pump"],
    ["15/06/2021", "pymthegfed o Fehefin dwy fil dau ddeg un"],
    ["31/7/2000", "tri deg un o Orffennaf dwy fil"],
    ["25/8/2010", "dau ddeg pump o Awst dwy fil a ddeg"],
    ["6/9/1999", "chweched o Fedi mil naw naw naw"],
    ["01/10/1920", "cyntaf o Hydref mil naw dau ddeg"],
    ["9/11/2024", "nawfed o Dachwedd dwy fil dau ddeg pedwar"],
    ["21/12/2024", "dau ddeg un o Ragfyr dwy fil dau ddeg pedwar"],  # unfed ar hugain?
    ["1/1/2023", "cyntaf o Ionawr dwy fil dau ddeg tri"],
    ["2/1/2023", "ail o Ionawr dwy fil dau ddeg tri"],
    ["3/1/2023", "trydydd o Ionawr dwy fil dau ddeg tri"],
    ["4/1/2023", "pedwerydd o Ionawr dwy fil dau ddeg tri"],
    ["5/1/2023", "pumed o Ionawr dwy fil dau ddeg tri"],
    ["6/1/2023", "chweched o Ionawr dwy fil dau ddeg tri"],
    ["7/1/2023", "seithfed o Ionawr dwy fil dau ddeg tri"],
    ["8/1/2023", "wythfed o Ionawr dwy fil dau ddeg tri"],
    ["9/1/2023", "nawfed o Ionawr dwy fil dau ddeg tri"],
    ["10/1/2023", "degfed o Ionawr dwy fil dau ddeg tri"],
    ["11/1/2023", "un ar ddegfed o Ionawr dwy fil dau ddeg tri"],
    ["12/1/2023", "deuddegfed o Ionawr dwy fil dau ddeg tri"],
    ["13/1/2023", "un deg tri o Ionawr dwy fil dau ddeg tri"],
    ["14/1/2023", "un deg pedwar o Ionawr dwy fil dau ddeg tri"],
    ["15/1/2023", "pymthegfed o Ionawr dwy fil dau ddeg tri"],
    ["16/1/2023", "un deg chwech o Ionawr dwy fil dau ddeg tri"],
    ["17/1/2023", "un deg saith o Ionawr dwy fil dau ddeg tri"],
    ["18/1/2023", "deunawfed o Ionawr dwy fil dau ddeg tri"],
    ["19/1/2023", "un deg naw o Ionawr dwy fil dau ddeg tri"],
    ["20/1/2023", "ugeinfed o Ionawr dwy fil dau ddeg tri"],
    ["21/1/2023", "dau ddeg un o Ionawr dwy fil dau ddeg tri"],
    ["22/1/2023", "dau ddeg dau o Ionawr dwy fil dau ddeg tri"],
    ["23/1/2023", "dau ddeg tri o Ionawr dwy fil dau ddeg tri"],
    ["24/1/2023", "dau ddeg pedwar o Ionawr dwy fil dau ddeg tri"],
    ["25/1/2023", "dau ddeg pump o Ionawr dwy fil dau ddeg tri"],
    ["26/1/2023", "dau ddeg chwech o Ionawr dwy fil dau ddeg tri"],
    ["27/1/2023", "dau ddeg saith o Ionawr dwy fil dau ddeg tri"],
    ["28/1/2023", "dau ddeg wyth o Ionawr dwy fil dau ddeg tri"],
    ["29/1/2023", "dau ddeg naw o Ionawr dwy fil dau ddeg tri"],
    ["30/1/2023", "tri deg o Ionawr dwy fil dau ddeg tri"],
    ["31/1/2023", "tri deg un o Ionawr dwy fil dau ddeg tri"],
    ["1/2/2023", "cyntaf o Chwefror dwy fil dau ddeg tri"],
    ["2/2/2023", "ail o Chwefror dwy fil dau ddeg tri"],
    ["3/2/2023", "trydydd o Chwefror dwy fil dau ddeg tri"],
    ["4/2/2023", "pedwerydd o Chwefror dwy fil dau ddeg tri"],
    ["5/2/2023", "pumed o Chwefror dwy fil dau ddeg tri"],
    ["6/2/2023", "chweched o Chwefror dwy fil dau ddeg tri"],
    ["7/2/2023", "seithfed o Chwefror dwy fil dau ddeg tri"],
    ["8/2/2023", "wythfed o Chwefror dwy fil dau ddeg tri"],
    ["9/2/2023", "nawfed o Chwefror dwy fil dau ddeg tri"],
    ["10/2/2023", "degfed o Chwefror dwy fil dau ddeg tri"],
    ["11/2/2023", "un ar ddegfed o Chwefror dwy fil dau ddeg tri"],
    ["12/2/2023", "deuddegfed o Chwefror dwy fil dau ddeg tri"],
    ["13/2/2023", "un deg tri o Chwefror dwy fil dau ddeg tri"],
    ["14/2/2023", "un deg pedwar o Chwefror dwy fil dau ddeg tri"],
    ["15/2/2023", "pymthegfed o Chwefror dwy fil dau ddeg tri"],
    ["16/2/2023", "un deg chwech o Chwefror dwy fil dau ddeg tri"],
    ["17/2/2023", "un deg saith o Chwefror dwy fil dau ddeg tri"],
    ["18/2/2023", "deunawfed o Chwefror dwy fil dau ddeg tri"],
    ["19/2/2023", "un deg naw o Chwefror dwy fil dau ddeg tri"],
    ["20/2/2023", "ugeinfed o Chwefror dwy fil dau ddeg tri"],
    ["21/2/2023", "dau ddeg un o Chwefror dwy fil dau ddeg tri"],
    ["22/2/2023", "dau ddeg dau o Chwefror dwy fil dau ddeg tri"],
    ["23/2/2023", "dau ddeg tri o Chwefror dwy fil dau ddeg tri"],
    ["24/2/2023", "dau ddeg pedwar o Chwefror dwy fil dau ddeg tri"],
    ["25/2/2023", "dau ddeg pump o Chwefror dwy fil dau ddeg tri"],
    ["26/2/2023", "dau ddeg chwech o Chwefror dwy fil dau ddeg tri"],
    ["27/2/2023", "dau ddeg saith o Chwefror dwy fil dau ddeg tri"],
    ["28/2/2023", "dau ddeg wyth o Chwefror dwy fil dau ddeg tri"],
    ["29/2/2023", "dau ddeg naw o Chwefror dwy fil dau ddeg tri"],
    ["30/2/2023", "tri deg o Chwefror dwy fil dau ddeg tri"],
    ["31/2/2023", "tri deg un o Chwefror dwy fil dau ddeg tri"],
    ["1/3/2023", "cyntaf o Fawrth dwy fil dau ddeg tri"],
    ["2/3/2023", "ail o Fawrth dwy fil dau ddeg tri"],
    ["3/3/2023", "trydydd o Fawrth dwy fil dau ddeg tri"],
    ["4/3/2023", "pedwerydd o Fawrth dwy fil dau ddeg tri"],
    ["5/3/2023", "pumed o Fawrth dwy fil dau ddeg tri"],
    ["6/3/2023", "chweched o Fawrth dwy fil dau ddeg tri"],
    ["7/3/2023", "seithfed o Fawrth dwy fil dau ddeg tri"],
    ["8/3/2023", "wythfed o Fawrth dwy fil dau ddeg tri"],
    ["9/3/2023", "nawfed o Fawrth dwy fil dau ddeg tri"],
    ["10/3/2023", "degfed o Fawrth dwy fil dau ddeg tri"],
    ["11/3/2023", "un ar ddegfed o Fawrth dwy fil dau ddeg tri"],
    ["12/3/2023", "deuddegfed o Fawrth dwy fil dau ddeg tri"],
    ["13/3/2023", "un deg tri o Fawrth dwy fil dau ddeg tri"],
    ["14/3/2023", "un deg pedwar o Fawrth dwy fil dau ddeg tri"],
    ["15/3/2023", "pymthegfed o Fawrth dwy fil dau ddeg tri"],
    ["16/3/2023", "un deg chwech o Fawrth dwy fil dau ddeg tri"],
    ["17/3/2023", "un deg saith o Fawrth dwy fil dau ddeg tri"],
    ["18/3/2023", "deunawfed o Fawrth dwy fil dau ddeg tri"],
    ["19/3/2023", "un deg naw o Fawrth dwy fil dau ddeg tri"],
    ["20/3/2023", "ugeinfed o Fawrth dwy fil dau ddeg tri"],
    ["21/3/2023", "dau ddeg un o Fawrth dwy fil dau ddeg tri"],
    ["22/3/2023", "dau ddeg dau o Fawrth dwy fil dau ddeg tri"],
    ["23/3/2023", "dau ddeg tri o Fawrth dwy fil dau ddeg tri"],
    ["24/3/2023", "dau ddeg pedwar o Fawrth dwy fil dau ddeg tri"],
    ["25/3/2023", "dau ddeg pump o Fawrth dwy fil dau ddeg tri"],
    ["26/3/2023", "dau ddeg chwech o Fawrth dwy fil dau ddeg tri"],
    ["27/3/2023", "dau ddeg saith o Fawrth dwy fil dau ddeg tri"],
    ["28/3/2023", "dau ddeg wyth o Fawrth dwy fil dau ddeg tri"],
    ["29/3/2023", "dau ddeg naw o Fawrth dwy fil dau ddeg tri"],
    ["30/3/2023", "tri deg o Fawrth dwy fil dau ddeg tri"],
    ["31/3/2023", "tri deg un o Fawrth dwy fil dau ddeg tri"],
    ["1/4/2023", "cyntaf o Ebrill dwy fil dau ddeg tri"],
    ["2/4/2023", "ail o Ebrill dwy fil dau ddeg tri"],
    ["3/4/2023", "trydydd o Ebrill dwy fil dau ddeg tri"],
    ["4/4/2023", "pedwerydd o Ebrill dwy fil dau ddeg tri"],
    ["5/4/2023", "pumed o Ebrill dwy fil dau ddeg tri"],
    ["6/4/2023", "chweched o Ebrill dwy fil dau ddeg tri"],
    ["7/4/2023", "seithfed o Ebrill dwy fil dau ddeg tri"],
    ["8/4/2023", "wythfed o Ebrill dwy fil dau ddeg tri"],
    ["9/4/2023", "nawfed o Ebrill dwy fil dau ddeg tri"],
    ["10/4/2023", "degfed o Ebrill dwy fil dau ddeg tri"],
    ["11/4/2023", "un ar ddegfed o Ebrill dwy fil dau ddeg tri"],
    ["12/4/2023", "deuddegfed o Ebrill dwy fil dau ddeg tri"],
    ["13/4/2023", "un deg tri o Ebrill dwy fil dau ddeg tri"],
    ["14/4/2023", "un deg pedwar o Ebrill dwy fil dau ddeg tri"],
    ["15/4/2023", "pymthegfed o Ebrill dwy fil dau ddeg tri"],
    ["16/4/2023", "un deg chwech o Ebrill dwy fil dau ddeg tri"],
    ["17/4/2023", "un deg saith o Ebrill dwy fil dau ddeg tri"],
    ["18/4/2023", "deunawfed o Ebrill dwy fil dau ddeg tri"],
    ["19/4/2023", "un deg naw o Ebrill dwy fil dau ddeg tri"],
    ["20/4/2023", "ugeinfed o Ebrill dwy fil dau ddeg tri"],
    ["21/4/2023", "dau ddeg un o Ebrill dwy fil dau ddeg tri"],
    ["22/4/2023", "dau ddeg dau o Ebrill dwy fil dau ddeg tri"],
    ["23/4/2023", "dau ddeg tri o Ebrill dwy fil dau ddeg tri"],
    ["24/4/2023", "dau ddeg pedwar o Ebrill dwy fil dau ddeg tri"],
    ["25/4/2023", "dau ddeg pump o Ebrill dwy fil dau ddeg tri"],
    ["26/4/2023", "dau ddeg chwech o Ebrill dwy fil dau ddeg tri"],
    ["27/4/2023", "dau ddeg saith o Ebrill dwy fil dau ddeg tri"],
    ["28/4/2023", "dau ddeg wyth o Ebrill dwy fil dau ddeg tri"],
    ["29/4/2023", "dau ddeg naw o Ebrill dwy fil dau ddeg tri"],
    ["30/4/2023", "tri deg o Ebrill dwy fil dau ddeg tri"],
    ["31/4/2023", "tri deg un o Ebrill dwy fil dau ddeg tri"],
    ["1/5/2023", "cyntaf o Fai dwy fil dau ddeg tri"],
    ["2/5/2023", "ail o Fai dwy fil dau ddeg tri"],
    ["3/5/2023", "trydydd o Fai dwy fil dau ddeg tri"],
    ["4/5/2023", "pedwerydd o Fai dwy fil dau ddeg tri"],
    ["5/5/2023", "pumed o Fai dwy fil dau ddeg tri"],
    ["6/5/2023", "chweched o Fai dwy fil dau ddeg tri"],
    ["7/5/2023", "seithfed o Fai dwy fil dau ddeg tri"],
    ["8/5/2023", "wythfed o Fai dwy fil dau ddeg tri"],
    ["9/5/2023", "nawfed o Fai dwy fil dau ddeg tri"],
    ["10/5/2023", "degfed o Fai dwy fil dau ddeg tri"],
    ["11/5/2023", "un ar ddegfed o Fai dwy fil dau ddeg tri"],
    ["12/5/2023", "deuddegfed o Fai dwy fil dau ddeg tri"],
    ["13/5/2023", "un deg tri o Fai dwy fil dau ddeg tri"],
    ["14/5/2023", "un deg pedwar o Fai dwy fil dau ddeg tri"],
    ["15/5/2023", "pymthegfed o Fai dwy fil dau ddeg tri"],
    ["16/5/2023", "un deg chwech o Fai dwy fil dau ddeg tri"],
    ["17/5/2023", "un deg saith o Fai dwy fil dau ddeg tri"],
    ["18/5/2023", "deunawfed o Fai dwy fil dau ddeg tri"],
    ["19/5/2023", "un deg naw o Fai dwy fil dau ddeg tri"],
    ["20/5/2023", "ugeinfed o Fai dwy fil dau ddeg tri"],
    ["21/5/2023", "dau ddeg un o Fai dwy fil dau ddeg tri"],
    ["22/5/2023", "dau ddeg dau o Fai dwy fil dau ddeg tri"],
    ["23/5/2023", "dau ddeg tri o Fai dwy fil dau ddeg tri"],
    ["24/5/2023", "dau ddeg pedwar o Fai dwy fil dau ddeg tri"],
    ["25/5/2023", "dau ddeg pump o Fai dwy fil dau ddeg tri"],
    ["26/5/2023", "dau ddeg chwech o Fai dwy fil dau ddeg tri"],
    ["27/5/2023", "dau ddeg saith o Fai dwy fil dau ddeg tri"],
    ["28/5/2023", "dau ddeg wyth o Fai dwy fil dau ddeg tri"],
    ["29/5/2023", "dau ddeg naw o Fai dwy fil dau ddeg tri"],
    ["30/5/2023", "tri deg o Fai dwy fil dau ddeg tri"],
    ["31/5/2023", "tri deg un o Fai dwy fil dau ddeg tri"],
    ["1/6/2023", "cyntaf o Fehefin dwy fil dau ddeg tri"],
    ["2/6/2023", "ail o Fehefin dwy fil dau ddeg tri"],
    ["3/6/2023", "trydydd o Fehefin dwy fil dau ddeg tri"],
    ["4/6/2023", "pedwerydd o Fehefin dwy fil dau ddeg tri"],
    ["5/6/2023", "pumed o Fehefin dwy fil dau ddeg tri"],
    ["6/6/2023", "chweched o Fehefin dwy fil dau ddeg tri"],
    ["7/6/2023", "seithfed o Fehefin dwy fil dau ddeg tri"],
    ["8/6/2023", "wythfed o Fehefin dwy fil dau ddeg tri"],
    ["9/6/2023", "nawfed o Fehefin dwy fil dau ddeg tri"],
    ["10/6/2023", "degfed o Fehefin dwy fil dau ddeg tri"],
    ["11/6/2023", "un ar ddegfed o Fehefin dwy fil dau ddeg tri"],
    ["12/6/2023", "deuddegfed o Fehefin dwy fil dau ddeg tri"],
    ["13/6/2023", "un deg tri o Fehefin dwy fil dau ddeg tri"],
    ["14/6/2023", "un deg pedwar o Fehefin dwy fil dau ddeg tri"],
    ["15/6/2023", "pymthegfed o Fehefin dwy fil dau ddeg tri"],
    ["16/6/2023", "un deg chwech o Fehefin dwy fil dau ddeg tri"],
    ["17/6/2023", "un deg saith o Fehefin dwy fil dau ddeg tri"],
    ["18/6/2023", "deunawfed o Fehefin dwy fil dau ddeg tri"],
    ["19/6/2023", "un deg naw o Fehefin dwy fil dau ddeg tri"],
    ["20/6/2023", "ugeinfed o Fehefin dwy fil dau ddeg tri"],
    ["21/6/2023", "dau ddeg un o Fehefin dwy fil dau ddeg tri"],
    ["22/6/2023", "dau ddeg dau o Fehefin dwy fil dau ddeg tri"],
    ["23/6/2023", "dau ddeg tri o Fehefin dwy fil dau ddeg tri"],
    ["24/6/2023", "dau ddeg pedwar o Fehefin dwy fil dau ddeg tri"],
    ["25/6/2023", "dau ddeg pump o Fehefin dwy fil dau ddeg tri"],
    ["26/6/2023", "dau ddeg chwech o Fehefin dwy fil dau ddeg tri"],
    ["27/6/2023", "dau ddeg saith o Fehefin dwy fil dau ddeg tri"],
    ["28/6/2023", "dau ddeg wyth o Fehefin dwy fil dau ddeg tri"],
    ["29/6/2023", "dau ddeg naw o Fehefin dwy fil dau ddeg tri"],
    ["30/6/2023", "tri deg o Fehefin dwy fil dau ddeg tri"],
    ["31/6/2023", "tri deg un o Fehefin dwy fil dau ddeg tri"],
    ["1/7/2023", "cyntaf o Orffennaf dwy fil dau ddeg tri"],
    ["2/7/2023", "ail o Orffennaf dwy fil dau ddeg tri"],
    ["3/7/2023", "trydydd o Orffennaf dwy fil dau ddeg tri"],
    ["4/7/2023", "pedwerydd o Orffennaf dwy fil dau ddeg tri"],
    ["5/7/2023", "pumed o Orffennaf dwy fil dau ddeg tri"],
    ["6/7/2023", "chweched o Orffennaf dwy fil dau ddeg tri"],
    ["7/7/2023", "seithfed o Orffennaf dwy fil dau ddeg tri"],
    ["8/7/2023", "wythfed o Orffennaf dwy fil dau ddeg tri"],
    ["9/7/2023", "nawfed o Orffennaf dwy fil dau ddeg tri"],
    ["10/7/2023", "degfed o Orffennaf dwy fil dau ddeg tri"],
    ["11/7/2023", "un ar ddegfed o Orffennaf dwy fil dau ddeg tri"],
    ["12/7/2023", "deuddegfed o Orffennaf dwy fil dau ddeg tri"],
    ["13/7/2023", "un deg tri o Orffennaf dwy fil dau ddeg tri"],
    ["14/7/2023", "un deg pedwar o Orffennaf dwy fil dau ddeg tri"],
    ["15/7/2023", "pymthegfed o Orffennaf dwy fil dau ddeg tri"],
    ["16/7/2023", "un deg chwech o Orffennaf dwy fil dau ddeg tri"],
    ["17/7/2023", "un deg saith o Orffennaf dwy fil dau ddeg tri"],
    ["18/7/2023", "deunawfed o Orffennaf dwy fil dau ddeg tri"],
    ["19/7/2023", "un deg naw o Orffennaf dwy fil dau ddeg tri"],
    ["20/7/2023", "ugeinfed o Orffennaf dwy fil dau ddeg tri"],
    ["21/7/2023", "dau ddeg un o Orffennaf dwy fil dau ddeg tri"],
    ["22/7/2023", "dau ddeg dau o Orffennaf dwy fil dau ddeg tri"],
    ["23/7/2023", "dau ddeg tri o Orffennaf dwy fil dau ddeg tri"],
    ["24/7/2023", "dau ddeg pedwar o Orffennaf dwy fil dau ddeg tri"],
    ["25/7/2023", "dau ddeg pump o Orffennaf dwy fil dau ddeg tri"],
    ["26/7/2023", "dau ddeg chwech o Orffennaf dwy fil dau ddeg tri"],
    ["27/7/2023", "dau ddeg saith o Orffennaf dwy fil dau ddeg tri"],
    ["28/7/2023", "dau ddeg wyth o Orffennaf dwy fil dau ddeg tri"],
    ["29/7/2023", "dau ddeg naw o Orffennaf dwy fil dau ddeg tri"],
    ["30/7/2023", "tri deg o Orffennaf dwy fil dau ddeg tri"],
    ["31/7/2023", "tri deg un o Orffennaf dwy fil dau ddeg tri"],
    ["1/8/2023", "cyntaf o Awst dwy fil dau ddeg tri"],
    ["2/8/2023", "ail o Awst dwy fil dau ddeg tri"],
    ["3/8/2023", "trydydd o Awst dwy fil dau ddeg tri"],
    ["4/8/2023", "pedwerydd o Awst dwy fil dau ddeg tri"],
    ["5/8/2023", "pumed o Awst dwy fil dau ddeg tri"],
    ["6/8/2023", "chweched o Awst dwy fil dau ddeg tri"],
    ["7/8/2023", "seithfed o Awst dwy fil dau ddeg tri"],
    ["8/8/2023", "wythfed o Awst dwy fil dau ddeg tri"],
    ["9/8/2023", "nawfed o Awst dwy fil dau ddeg tri"],
    ["10/8/2023", "degfed o Awst dwy fil dau ddeg tri"],
    ["11/8/2023", "un ar ddegfed o Awst dwy fil dau ddeg tri"],
    ["12/8/2023", "deuddegfed o Awst dwy fil dau ddeg tri"],
    ["13/8/2023", "un deg tri o Awst dwy fil dau ddeg tri"],
    ["14/8/2023", "un deg pedwar o Awst dwy fil dau ddeg tri"],
    ["15/8/2023", "pymthegfed o Awst dwy fil dau ddeg tri"],
    ["16/8/2023", "un deg chwech o Awst dwy fil dau ddeg tri"],
    ["17/8/2023", "un deg saith o Awst dwy fil dau ddeg tri"],
    ["18/8/2023", "deunawfed o Awst dwy fil dau ddeg tri"],
    ["19/8/2023", "un deg naw o Awst dwy fil dau ddeg tri"],
    ["20/8/2023", "ugeinfed o Awst dwy fil dau ddeg tri"],
    ["21/8/2023", "dau ddeg un o Awst dwy fil dau ddeg tri"],
    ["22/8/2023", "dau ddeg dau o Awst dwy fil dau ddeg tri"],
    ["23/8/2023", "dau ddeg tri o Awst dwy fil dau ddeg tri"],
    ["24/8/2023", "dau ddeg pedwar o Awst dwy fil dau ddeg tri"],
    ["25/8/2023", "dau ddeg pump o Awst dwy fil dau ddeg tri"],
    ["26/8/2023", "dau ddeg chwech o Awst dwy fil dau ddeg tri"],
    ["27/8/2023", "dau ddeg saith o Awst dwy fil dau ddeg tri"],
    ["28/8/2023", "dau ddeg wyth o Awst dwy fil dau ddeg tri"],
    ["29/8/2023", "dau ddeg naw o Awst dwy fil dau ddeg tri"],
    ["30/8/2023", "tri deg o Awst dwy fil dau ddeg tri"],
    ["31/8/2023", "tri deg un o Awst dwy fil dau ddeg tri"],
    ["1/9/2023", "cyntaf o Fedi dwy fil dau ddeg tri"],
    ["2/9/2023", "ail o Fedi dwy fil dau ddeg tri"],
    ["3/9/2023", "trydydd o Fedi dwy fil dau ddeg tri"],
    ["4/9/2023", "pedwerydd o Fedi dwy fil dau ddeg tri"],
    ["5/9/2023", "pumed o Fedi dwy fil dau ddeg tri"],
    ["6/9/2023", "chweched o Fedi dwy fil dau ddeg tri"],
    ["7/9/2023", "seithfed o Fedi dwy fil dau ddeg tri"],
    ["8/9/2023", "wythfed o Fedi dwy fil dau ddeg tri"],
    ["9/9/2023", "nawfed o Fedi dwy fil dau ddeg tri"],
    ["10/9/2023", "degfed o Fedi dwy fil dau ddeg tri"],
    ["11/9/2023", "un ar ddegfed o Fedi dwy fil dau ddeg tri"],
    ["12/9/2023", "deuddegfed o Fedi dwy fil dau ddeg tri"],
    ["13/9/2023", "un deg tri o Fedi dwy fil dau ddeg tri"],
    ["14/9/2023", "un deg pedwar o Fedi dwy fil dau ddeg tri"],
    ["15/9/2023", "pymthegfed o Fedi dwy fil dau ddeg tri"],
    ["16/9/2023", "un deg chwech o Fedi dwy fil dau ddeg tri"],
    ["17/9/2023", "un deg saith o Fedi dwy fil dau ddeg tri"],
    ["18/9/2023", "deunawfed o Fedi dwy fil dau ddeg tri"],
    ["19/9/2023", "un deg naw o Fedi dwy fil dau ddeg tri"],
    ["20/9/2023", "ugeinfed o Fedi dwy fil dau ddeg tri"],
    ["21/9/2023", "dau ddeg un o Fedi dwy fil dau ddeg tri"],
    ["22/9/2023", "dau ddeg dau o Fedi dwy fil dau ddeg tri"],
    ["23/9/2023", "dau ddeg tri o Fedi dwy fil dau ddeg tri"],
    ["24/9/2023", "dau ddeg pedwar o Fedi dwy fil dau ddeg tri"],
    ["25/9/2023", "dau ddeg pump o Fedi dwy fil dau ddeg tri"],
    ["26/9/2023", "dau ddeg chwech o Fedi dwy fil dau ddeg tri"],
    ["27/9/2023", "dau ddeg saith o Fedi dwy fil dau ddeg tri"],
    ["28/9/2023", "dau ddeg wyth o Fedi dwy fil dau ddeg tri"],
    ["29/9/2023", "dau ddeg naw o Fedi dwy fil dau ddeg tri"],
    ["30/9/2023", "tri deg o Fedi dwy fil dau ddeg tri"],
    ["31/9/2023", "tri deg un o Fedi dwy fil dau ddeg tri"],
    ["1/10/2023", "cyntaf o Hydref dwy fil dau ddeg tri"],
    ["2/10/2023", "ail o Hydref dwy fil dau ddeg tri"],
    ["3/10/2023", "trydydd o Hydref dwy fil dau ddeg tri"],
    ["4/10/2023", "pedwerydd o Hydref dwy fil dau ddeg tri"],
    ["5/10/2023", "pumed o Hydref dwy fil dau ddeg tri"],
    ["6/10/2023", "chweched o Hydref dwy fil dau ddeg tri"],
    ["7/10/2023", "seithfed o Hydref dwy fil dau ddeg tri"],
    ["8/10/2023", "wythfed o Hydref dwy fil dau ddeg tri"],
    ["9/10/2023", "nawfed o Hydref dwy fil dau ddeg tri"],
    ["10/10/2023", "degfed o Hydref dwy fil dau ddeg tri"],
    ["11/10/2023", "un ar ddegfed o Hydref dwy fil dau ddeg tri"],
    ["12/10/2023", "deuddegfed o Hydref dwy fil dau ddeg tri"],
    ["13/10/2023", "un deg tri o Hydref dwy fil dau ddeg tri"],
    ["14/10/2023", "un deg pedwar o Hydref dwy fil dau ddeg tri"],
    ["15/10/2023", "pymthegfed o Hydref dwy fil dau ddeg tri"],
    ["16/10/2023", "un deg chwech o Hydref dwy fil dau ddeg tri"],
    ["17/10/2023", "un deg saith o Hydref dwy fil dau ddeg tri"],
    ["18/10/2023", "deunawfed o Hydref dwy fil dau ddeg tri"],
    ["19/10/2023", "un deg naw o Hydref dwy fil dau ddeg tri"],
    ["20/10/2023", "ugeinfed o Hydref dwy fil dau ddeg tri"],
    ["21/10/2023", "dau ddeg un o Hydref dwy fil dau ddeg tri"],
    ["22/10/2023", "dau ddeg dau o Hydref dwy fil dau ddeg tri"],
    ["23/10/2023", "dau ddeg tri o Hydref dwy fil dau ddeg tri"],
    ["24/10/2023", "dau ddeg pedwar o Hydref dwy fil dau ddeg tri"],
    ["25/10/2023", "dau ddeg pump o Hydref dwy fil dau ddeg tri"],
    ["26/10/2023", "dau ddeg chwech o Hydref dwy fil dau ddeg tri"],
    ["27/10/2023", "dau ddeg saith o Hydref dwy fil dau ddeg tri"],
    ["28/10/2023", "dau ddeg wyth o Hydref dwy fil dau ddeg tri"],
    ["29/10/2023", "dau ddeg naw o Hydref dwy fil dau ddeg tri"],
    ["30/10/2023", "tri deg o Hydref dwy fil dau ddeg tri"],
    ["31/10/2023", "tri deg un o Hydref dwy fil dau ddeg tri"],
    ["1/11/2023", "cyntaf o Dachwedd dwy fil dau ddeg tri"],
    ["2/11/2023", "ail o Dachwedd dwy fil dau ddeg tri"],
    ["3/11/2023", "trydydd o Dachwedd dwy fil dau ddeg tri"],
    ["4/11/2023", "pedwerydd o Dachwedd dwy fil dau ddeg tri"],
    ["5/11/2023", "pumed o Dachwedd dwy fil dau ddeg tri"],
    ["6/11/2023", "chweched o Dachwedd dwy fil dau ddeg tri"],
    ["7/11/2023", "seithfed o Dachwedd dwy fil dau ddeg tri"],
    ["8/11/2023", "wythfed o Dachwedd dwy fil dau ddeg tri"],
    ["9/11/2023", "nawfed o Dachwedd dwy fil dau ddeg tri"],
    ["10/11/2023", "degfed o Dachwedd dwy fil dau ddeg tri"],
    ["11/11/2023", "un ar ddegfed o Dachwedd dwy fil dau ddeg tri"],
    ["12/11/2023", "deuddegfed o Dachwedd dwy fil dau ddeg tri"],
    ["13/11/2023", "un deg tri o Dachwedd dwy fil dau ddeg tri"],
    ["14/11/2023", "un deg pedwar o Dachwedd dwy fil dau ddeg tri"],
    ["15/11/2023", "pymthegfed o Dachwedd dwy fil dau ddeg tri"],
    ["16/11/2023", "un deg chwech o Dachwedd dwy fil dau ddeg tri"],
    ["17/11/2023", "un deg saith o Dachwedd dwy fil dau ddeg tri"],
    ["18/11/2023", "deunawfed o Dachwedd dwy fil dau ddeg tri"],
    ["19/11/2023", "un deg naw o Dachwedd dwy fil dau ddeg tri"],
    ["20/11/2023", "ugeinfed o Dachwedd dwy fil dau ddeg tri"],
    ["21/11/2023", "dau ddeg un o Dachwedd dwy fil dau ddeg tri"],
    ["22/11/2023", "dau ddeg dau o Dachwedd dwy fil dau ddeg tri"],
    ["23/11/2023", "dau ddeg tri o Dachwedd dwy fil dau ddeg tri"],
    ["24/11/2023", "dau ddeg pedwar o Dachwedd dwy fil dau ddeg tri"],
    ["25/11/2023", "dau ddeg pump o Dachwedd dwy fil dau ddeg tri"],
    ["26/11/2023", "dau ddeg chwech o Dachwedd dwy fil dau ddeg tri"],
    ["27/11/2023", "dau ddeg saith o Dachwedd dwy fil dau ddeg tri"],
    ["28/11/2023", "dau ddeg wyth o Dachwedd dwy fil dau ddeg tri"],
    ["29/11/2023", "dau ddeg naw o Dachwedd dwy fil dau ddeg tri"],
    ["30/11/2023", "tri deg o Dachwedd dwy fil dau ddeg tri"],
    ["31/11/2023", "tri deg un o Dachwedd dwy fil dau ddeg tri"],
    ["1/12/2023", "cyntaf o Ragfyr dwy fil dau ddeg tri"],
    ["2/12/2023", "ail o Ragfyr dwy fil dau ddeg tri"],
    ["3/12/2023", "trydydd o Ragfyr dwy fil dau ddeg tri"],
    ["4/12/2023", "pedwerydd o Ragfyr dwy fil dau ddeg tri"],
    ["5/12/2023", "pumed o Ragfyr dwy fil dau ddeg tri"],
    ["6/12/2023", "chweched o Ragfyr dwy fil dau ddeg tri"],
    ["7/12/2023", "seithfed o Ragfyr dwy fil dau ddeg tri"],
    ["8/12/2023", "wythfed o Ragfyr dwy fil dau ddeg tri"],
    ["9/12/2023", "nawfed o Ragfyr dwy fil dau ddeg tri"],
    ["10/12/2023", "degfed o Ragfyr dwy fil dau ddeg tri"],
    ["11/12/2023", "un ar ddegfed o Ragfyr dwy fil dau ddeg tri"],
    ["12/12/2023", "deuddegfed o Ragfyr dwy fil dau ddeg tri"],
    ["13/12/2023", "un deg tri o Ragfyr dwy fil dau ddeg tri"],
    ["14/12/2023", "un deg pedwar o Ragfyr dwy fil dau ddeg tri"],
    ["15/12/2023", "pymthegfed o Ragfyr dwy fil dau ddeg tri"],
    ["16/12/2023", "un deg chwech o Ragfyr dwy fil dau ddeg tri"],
    ["17/12/2023", "un deg saith o Ragfyr dwy fil dau ddeg tri"],
    ["18/12/2023", "deunawfed o Ragfyr dwy fil dau ddeg tri"],
    ["19/12/2023", "un deg naw o Ragfyr dwy fil dau ddeg tri"],
    ["20/12/2023", "ugeinfed o Ragfyr dwy fil dau ddeg tri"],
    ["21/12/2023", "dau ddeg un o Ragfyr dwy fil dau ddeg tri"],
    ["22/12/2023", "dau ddeg dau o Ragfyr dwy fil dau ddeg tri"],
    ["23/12/2023", "dau ddeg tri o Ragfyr dwy fil dau ddeg tri"],
    ["24/12/2023", "dau ddeg pedwar o Ragfyr dwy fil dau ddeg tri"],
    ["25/12/2023", "dau ddeg pump o Ragfyr dwy fil dau ddeg tri"],
    ["26/12/2023", "dau ddeg chwech o Ragfyr dwy fil dau ddeg tri"],
    ["27/12/2023", "dau ddeg saith o Ragfyr dwy fil dau ddeg tri"],
    ["28/12/2023", "dau ddeg wyth o Ragfyr dwy fil dau ddeg tri"],
    ["29/12/2023", "dau ddeg naw o Ragfyr dwy fil dau ddeg tri"],
    ["30/12/2023", "tri deg o Ragfyr dwy fil dau ddeg tri"],
    ["31/12/2023", "tri deg un o Ragfyr dwy fil dau ddeg tri"],
]


def test_date():
    for date in tests:
        result = expand_date_welsh(date[0])
        assert result == date[1]
