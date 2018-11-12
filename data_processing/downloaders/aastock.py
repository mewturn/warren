import urllib.request
from bs4 import BeautifulSoup
import time

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

def getURL():
    pre = "http://www.etnet.com.hk/www/tc/stocks/ci_ipo_info.php?page="
    with open("url.txt", "w") as outp:
        try:
            outp_links = set()
            for page in range(1, 12): 
                opener = AppURLopener()
                url = pre + str(page)
                resp = opener.open(url)
                web = resp.read()
                soup = BeautifulSoup(web, "lxml")
                content = soup.find("div", {"class": "DivFigureContent"})
                links = content.findAll('a')
                
                for link in links:
                    href = link.get("href")
                    if not href == None and not "page" in href:
                        outp_links.add(href)
                
                for i in outp_links:
                    outp.write(i + "\n")
                    
        except Exception as e:
            print(e)
    
    return 

def getText(url, lang):
    opener = AppURLopener()
    resp = opener.open(url)
    web = resp.read()
    soup = BeautifulSoup(web, "lxml")
    #content = soup.findAll("div", {"class" : "DivArticleList", "class" : "dotLine"})
    #content = soup.findAll("div", {"class" : "ipoColumnBlock"})
    
    if lang == "en":
        splitter = "Corporate Profile"
    else:
        splitter = "公司業務"
    
    content = soup.findAll("td", {"class" : "mcFont"})

    text = list(content)
    outp = " ".join([i.text for i in text])

    out_text = " ".join(outp.split(splitter)[1:])
    
    return out_text
    
def getData():
    pre = "http://www.aastocks.com/en/stocks/analysis/company-fundamental/?symbol="
    i = 0
    dir = "temp_aastock/"
    completed = {"0001", "0002", "0003", "0004", "0005", "0006", "0007", "0008", "0009", "0010", "0011", "0012", "0014", "0015", "0016", "0017", "0018", "0019", "0020", "0021", "0022", "0023", "0024", "0025", "0026", "0027", "0028", "0029", "0030", "0031", "0032", "0033",
"0034",
"0035",
"0036",
"0037",
"0038",
"0039",
"0040",
"0041",
"0042",
"0043",
"0044",
"0045",
"0046",
"0047",
"0048",
"0050",
"0051",
"0052",
"0053",
"0054",
"0055",
"0056",
"0057",
"0058",
"0059",
"0060",
"0061",
"0062",
"0063",
"0064",
"0065",
"0066",
"0067",
"0068",
"0069",
"0070",
"0071",
"0072",
"0073",
"0075",
"0076",
"0077",
"0078",
"0079",
"0080",
"0081",
"0082",
"0083",
"0084",
"0085",
"0086",
"0087",
"0088",
"0089",
"0090",
"0091",
"0092",
"0093",
"0094",
"0095",
"0096",
"0097",
"0098",
"0099",
"0100",
"0101",
"0102",
"0103",
"0104",
"0105",
"0106",
"0107",
"0108",
"0109",
"0110",
"0111",
"0112",
"0113",
"0114",
"0115",
"0116",
"0117",
"0118",
"0119",
"0120",
"0121",
"0122",
"0123",
"0124",
"0125",
"0126",
"0127",
"0128",
"0129",
"0130",
"0131",
"0132",
"0133",
"0135",
"0136",
"0137",
"0138",
"0139",
"0141",
"0142",
"0143",
"0144",
"0145",
"0146",
"0147",
"0148",
"0149",
"0151",
"0152",
"0153",
"0154",
"0155",
"0156",
"0157",
"0158",
"0159",
"0160",
"0161",
"0162",
"0163",
"0164",
"0165",
"0166",
"0167",
"0168",
"0169",
"0171",
"0172",
"0173",
"0174",
"0175",
"0176",
"0177",
"0178",
"0179",
"0180",
"0181",
"0182",
"0183",
"0184",
"0185",
"0186",
"0187",
"0188",
"0189",
"0190",
"0191",
"0193",
"0194",
"0195",
"0196",
"0197",
"0198",
"0199",
"0200",
"0201",
"0202",
"0204",
"0205",
"0206",
"0207",
"0208",
"0209",
"0210",
"0211",
"0212",
"0213",
"0214",
"0215",
"0216",
"0217",
"0218",
"0219",
"0220",
"0221",
"0222",
"0223",
"0224",
"0225",
"0226",
"0227",
"0228",
"0229",
"0230",
"0231",
"0232",
"0233",
"0234",
"0235",
"0236",
"0237",
"0238",
"0239",
"0240",
"0241",
"0242",
"0243",
"0244",
"0245",
"0246",
"0247",
"0248",
"0250",
"0251",
"0252",
"0253",
"0254",
"0255",
"0256",
"0257",
"0258",
"0259",
"0260",
"0261",
"0262",
"0263",
"0264",
"0265",
"0266",
"0267",
"0268",
"0269",
"0270",
"0271",
"0272",
"0273",
"0274",
"0275",
"0276",
"0277",
"0278",
"0279",
"0280",
"0281",
"0282",
"0285",
"0286",
"0287",
"0288",
"0289",
"0290",
"0291",
"0292",
"0293",
"0294",
"0295",
"0296",
"0297",
"0298",
"0299",
"0300",
"0303",
"0305",
"0306",
"0307",
"0308",
"0309",
"0310",
"0311",
"0312",
"0313",
"0315",
"0316",
"0317",
"0318",
"0320",
"0321",
"0322",
"0323",
"0326",
"0327",
"0328",
"0329",
"0330",
"0331",
"0332",
"0333",
"0334",
"0335",
"0336",
"0337",
"0338",
"0339",
"0340",
"0341",
"0342",
"0343",
"0345",
"0346",
"0347",
"0348",
"0351",
"0352",
"0353",
"0354",
"0355",
"0356",
"0357",
"0358",
"0359",
"0360",
"0361",
"0362",
"0363",
"0364",
"0365",
"0366",
"0367",
"0368",
"0369",
"0370",
"0371",
"0372",
"0373",
"0374",
"0375",
"0376",
"0377",
"0378",
"0379",
"0380",
"0381",
"0383",
"0384",
"0385",
"0386",
"0387",
"0388",
"0389",
"0390",
"0391",
"0392",
"0393",
"0395",
"0396",
"0397",
"0398",
"0399",
"0400",
"0401",
"0402",
"0403",
"0404",
"0408",
"0410",
"0411",
"0412",
"0413",
"0416",
"0417",
"0418",
"0419",
"0420",
"0422",
"0423",
"0425",
"0426",
"0428",
"0430",
"0431",
"0432",
"0433",
"0434",
"0436",
"0439",
"0440",
"0442",
"0444",
"0445",
"0449",
"0450",
"0451",
"0455",
"0456",
"0458",
"0459",
"0460",
"0462",
"0464",
"0465",
"0467",
"0468",
"0469",
"0471",
"0472",
"0474",
"0475",
"0476",
"0479",
"0480",
"0482",
"0483",
"0484",
"0485",
"0486",
"0487",
"0488",
"0489",
"0491",
"0493",
"0494",
"0495",
"0496",
"0497",
"0498",
"0499",
"0500",
"0503",
"0505",
"0506",
"0508",
"0509",
"0510",
"0511",
"0512",
"0513",
"0515",
"0517",
"0518",
"0519",
"0520",
"0521",
"0522",
"0524",
"0525",
"0526",
"0527",
"0528",
"0529",
"0530",
"0531",
"0532",
"0533",
"0535",
"0536",
"0538",
"0539",
"0540",
"0542",
"0543",
"0544",
"0546",
"0547",
"0548",
"0550",
"0551",
"0552",
"0553",
"0554",
"0555",
"0556",
"0557",
"0558",
"0559",
"0560",
"0563",
"0564",
"0565",
"0566",
"0567",
"0568",
"0569",
"0570",
"0571",
"0572",
"0573",
"0574",
"0575",
"0576",
"0577",
"0578",
"0579",
"0580",
"0581",
"0582",
"0583",
"0585",
"0586",
"0587",
"0588",
"0590",
"0591",
"0592",
"0593",
"0595",
"0596",
"0598",
"0599",
"0600",
"0601",
"0602",
"0603",
"0604",
"0605",
"0606",
"0607",
"0608",
"0609",
"0610",
"0611",
"0612",
"0613",
"0616",
"0617",
"0618",
"0619",
"0620",
"0621",
"0622",
"0623",
"0626",
"0627",
"0629",
"0630",
"0631",
"0632",
"0633",
"0635",
"0636",
"0637",
"0638",
"0639",
"0640",
"0641",
"0643",
"0645",
"0646",
"0647",
"0648",
"0650",
"0651",
"0653",
"0655",
"0656",
"0657",
"0658",
"0659",
"0660",
"0661",
"0662",
"0663",
"0665",
"0666",
"0668",
"0669",
"0670",
"0672",
"0673",
"0674",
"0675",
"0676",
"0677",
"0678",
"0679",
"0680",
"0681",
"0682",
"0683",
"0684",
"0685",
"0686",
"0687",
"0688",
"0689",
"0690",
"0691",
"0692",
"0693",
"0694",
"0695",
"0696",
"0697",
"0698",
"0699",
"0700",
"0701",
"0702",
"0703",
"0704",
"0705",
"0706",
"0707",
"0708",
"0709",
"0710",
"0711",
"0712",
"0713",
"0715",
"0716",
"0717",
"0718",
"0719",
"0720",
"0721",
"0722",
"0723",
"0724",
"0725",
"0726",
"0727",
"0728",
"0729",
"0730",
"0731",
"0732",
"0733",
"0735",
"0736",
"0737",
"0738",
"0743",
"0745",
"0746",
"0747",
"0750",
"0751",
"0752",
"0753",
"0754",
"0755",
"0756",
"0757",
"0758",
"0759",
"0760",
"0762",
"0763",
"0764",
"0765",
"0766",
"0767",
"0768",
"0769",
"0770",
"0771",
"0772",
"0775",
"0776",
"0777",
"0784",
"0787",
"0788",
"0794",
"0797",
"0798",
"0799",
"0800",
"0801",
"0802",
"0803",
"0804",
"0806",
"0807",
"0809",
"0810",
"0811",
"0812",
"0814",
"0815",
"0816",
"0817",
"0818",
"0819",
"0821",
"0822",
"0825",
"0826",
"0827",
"0829",
"0830",
"0832",
"0833",
"0834",
"0835",
"0836",
"0837",
"0838",
"0839",
"0840",
"0841",
"0842",
"0844",
"0845",
"0846",
"0848",
"0850",
"0851",
"0852",
"0853",
"0854",
"0855",
"0856",
"0857",
"0858",
"0859",
"0860",
"0861",
"0862",
"0863",
"0864",
"0865",
"0866",
"0867",
"0868",
"0869",
"0871",
"0872",
"0873",
"0874",
"0875",
"0876",
"0877",
"0878",
"0880",
"0881",
"0882",
"0883",
"0884",
"0885",
"0886",
"0887",
"0888",
"0889",
"0891",
"0893",
"0894",
"0895",
"0896",
"0897",
"0898",
"0900",
"0901",
"0902",
"0903",
"0904",
"0905",
"0906",
"0907",
"0908",
"0909",
"0910",
"0911",
"0912",
"0913",
"0914",
"0915",
"0916",
"0918",
"0919",
"0921",
"0922",
"0923",
"0925",
"0926",
"0927",
"0928",
"0929",
"0931",
"0932",
"0933",
"0934",
"0935",
"0936",
"0938",
"0939",
"0940",
"0941",
"0943",
"0945",
"0947",
"0948",
"0950",
"0951",
"0952",
"0953",
"0954",
"0956",
"0958",
"0959",
"0960",
"0966",
"0967",
"0968",
"0969",
"0970",
"0973",
"0974",
"0975",
"0976",
"0978",
"0979",
"0980",
"0981",
"0982",
"0983",
"0984",
"0985",
"0986",
"0987",
"0988",
"0989",
"0990",
"0991",
"0992",
"0993",
"0994",
"0995",
"0996",
"0997",
"0998",
"0999",
"1000",
"1001",
"1002",
"1003",
"1004",
"1005",
"1006",
"1007",
"1008",
"1009",
"1010",
"1011",
"1013",
"1019",
"1020",
"1021",
"1022",
"1023",
"1026",
"1027",
"1029",
"1030",
"1031",
"1033",
"1035",
"1036",
"1037",
"1038",
"1039",
"1041",
"1043",
"1044",
"1045",
"1046",
"1047",
"1048",
"1049",
"1050",
"1051",
"1052",
"1053",
"1055",
"1057",
"1058",
"1059",
"1060",
"1061",
"1062",
"1063",
"1064",
"1065",
"1066",
"1068",
"1069",
"1070",
"1071",
"1072",
"1073",
"1075",
"1076",
"1079",
"1080",
"1082",
"1083",
"1085",
"1086",
"1087",
"1088",
"1089",
"1093",
"1094",
"1096",
"1097",
"1098",
"1099",
"1100",
"1101",
"1102",
"1103",
"1104",
"1105",
"1106",
"1107",
"1108",
"1109",
"1110",
"1111",
"1112",
"1113",
"1114",
"1115",
"1116",
"1117",
"1118",
"1120",
"1121",
"1122",
"1123",
"1124",
"1125",
"1126",
"1127",
"1128",
"1129",
"1130",
"1131",
"1132",
"1133",
"1135",
"1137",
"1138",
"1139",
"1140",
"1141",
"1142",
"1143",
"1145",
"1146",
"1148",
"1149",
"1150",
"1151",
"1152",
"1155",
"1157",
"1159",
"1160",
"1161",
"1164",
"1165",
"1166",
"1168",
"1169",
"1170",
"1171",
"1172",
"1173",
"1174",
"1175",
"1176",
"1177",
"1178",
"1180",
"1181",
"1182",
"1183",
"1184",
"1185",
"1186",
"1187",
"1188",
"1189",
"1190",
"1191",
"1192",
"1193",
"1194",
"1195",
"1196",
"1197",
"1198",
"1199",
"1200",
"1201",
"1202",
"1203",
"1205",
"1206",
"1207",
"1208",
"1210",
"1211",
"1212",
"1213",
"1215",
"1216",
"1217",
"1218",
"1219",
"1220",
"1221",
"1222",
"1223",
"1224",
"1225",
"1226",
"1227",
"1228",
"1229",
"1230",
"1231",
"1232",
"1233",
"1234",
"1235",
"1236",
"1237",
"1238",
"1239",
"1240",
"1241",
"1243",
"1245",
"1246",
"1247",
"1249",
"1250",
"1251",
"1252",
"1253",
"1255",
"1257",
"1258",
"1259",
"1260",
"1262",
"1263",
"1265",
"1266",
"1268",
"1269",
"1270",
"1271",
"1272",
"1273",
"1277",
"1278",
"1280",
"1281",
"1282",
"1285",
"1288",
"1289",
"1290",
"1292",
"1293",
"1297",
"1298",
"1299",
"1300",
"1301",
"1302",
"1303",
"1305",
"1308",
"1310",
"1312",
"1313",
"1314",
"1315",
"1316",
"1317",
"1318",
"1319",
"1321",
"1322",
"1323",
"1326",
"1327",
"1328",
"1329",
"1330",
"1332",
"1333",
"1335",
"1336",
"1337",
"1338",
"1339",
"1340",
"1341",
"1345",
"1347",
"1348",
"1349",
"1353",
"1355",
"1357",
"1358",
"1359",
"1360",
"1361",
"1362",
"1363",
"1365",
"1366",
"1367",
"1368",
"1369",
"1370",
"1371",
"1372",
"1373",
"1375",
"1378",
"1380",
"1381",
"1382",
"1383",
"1385",
"1386",
"1387",
"1388",
"1389",
"1393",
"1395",
"1396",
"1397",
"1398",
"1399",
"1400",
"1415",
"1417",
"1418",
"1419",
"1420",
"1421",
"1428",
"1430",
"1431",
"1432",
"1439",
"1443",
"1446",
"1447",
"1448",
"1450",
"1451",
"1452",
"1458",
"1459",
"1460",
"1461",
"1462",
"1466",
"1468",
"1469",
"1470",
"1475",
"1476",
"1478",
"1480",
"1483",
"1486",
"1488",
"1492",
"1495",
"1496",
"1498",
"1499",
"1500",
"1508",
"1509",
"1513",
"1515",
"1518",
"1522",
"1523",
"1526",
"1527",
"1528",
"1530",
"1532",
"1533",
"1536",
"1538",
"1539",
"1543",
"1546",
"1547",
"1548",
"1549",
"1551",
"1552",
"1555",
"1556",
"1557",
"1558",
"1559",
"1561",
"1565",
"1566",
"1568",
"1569",
"1570",
"1571",
"1572",
"1573",
"1575",
"1576",
"1577",
"1578",
"1579",
"1580",
"1581",
"1583",
"1585",
"1586",
"1587",
"1588",
"1589",
"1591",
"1592",
"1596",
"1598",
"1599",
"1600",
"1606",
"1608",
"1609",
"1610",
"1611",
"1612",
"1613",
"1616",
"1617",
"1618",
"1619",
"1620",
"1621",
"1622",
"1623",
"1626",
"1627",
"1628",
"1629",
"1630",
"1631",
"1632",
"1633",
"1635",
"1636",
"1637",
"1638",
"1639",
"1647",
"1649",
"1651",
"1652",
"1655",
"1656",
"1658",
"1659",
"1660",
"1661",
"1662",
"1663",
"1665",
"1666",
"1667",
"1668",
"1669",
"1671",
"1672",
"1673",
"1676",
"1678",
"1679",
"1680",
"1681",
"1682",
"1683",
"1685",
"1686",
"1689",
"1690",
"1693",
"1695",
"1696",
"1697",
"1698",
"1699",
"1700",
"1702",
"1705",
"1706",
"1707",
"1708",
"1709",
"1711",
"1715",
"1716",
"1717",
"1718",
"1719",
"1720",
"1721",
"1722",
"1725",
"1726",
"1727",
"1728",
"1729",
"1730",
"1731",
"1733",
"1735",
"1737",
"1738",
"1739",
"1742",
"1746",
"1749",
"1750",
"1751",
"1752",
"1757",
"1758",
"1760",
"1763",
"1765",
"1766",
"1771",
"1773",
"1775",
"1776",
"1777",
"1778",
"1783",
"1786",
"1788",
"1789",
"1798",
"1799",
"1800",
"1803",
"1806",
"1808",
"1810",
"1811",
"1812",
"1813",
"1815",
"1816",
"1818",
"1819",
"1822",
"1823",
"1826",
"1828",
"1829",
"1830",
"1831",
"1833",
"1836",
"1838",
"1848",
"1856",
"1858",
"1862",
"1863",
"1866",
"1868",
"1869",
"1878",
"1882",
"1883",
"1884",
"1885",
"1886",
"1888",
"1889",
"1898",
"1899",
"1900",
"1908",
"1910",
"1913",
"1916",
"1918",
"1919",
"1929",
"1932",
"1933",
"1938",
"1958",
"1962",
"1963",
"1966",
"1968",
"1970",
"1972",
"1975",
"1978",
"1979",
"1980",
"1982",
"1985",
"1986",
"1988",
"1989",
"1990",
"1991",
"1993",
"1996",
"1997",
"1998",
"1999",
"2000",
"2001",
"2002",
"2003",
"2005",
"2006",
"2007",
"2008",
"2009",
"2010",
"2011",
"2012",
"2014"}
    codes = ["2016",
"2017",
"2018",
"2020",
"2022",
"2023",
"2025",
"2028",
"2030",
"2031",
"2033",
"2038",
"2039",
"2048",
"2051",
"2066",
"2068",
"2078",
"2080",
"2083",
"2086",
"2088",
"2098",
"2099",
"2100",
"2111",
"2112",
"2113",
"2116",
"2118",
"2119",
"2120",
"2121",
"2122",
"2123",
"2128",
"2133",
"2136",
"2138",
"2139",
"2166",
"2178",
"2182",
"2183",
"2186",
"2188",
"2193",
"2196",
"2198",
"2199",
"2200",
"2202",
"2203",
"2208",
"2211",
"2212",
"2213",
"2218",
"2221",
"2222",
"2223",
"2225",
"2226",
"2227",
"2228",
"2229",
"2232",
"2233",
"2236",
"2238",
"2239",
"2255",
"2262",
"2266",
"2268",
"2269",
"2277",
"2278",
"2280",
"2281",
"2282",
"2283",
"2286",
"2288",
"2289",
"2292",
"2293",
"2298",
"2299",
"2300",
"2302",
"2303",
"2307",
"2308",
"2309",
"2310",
"2312",
"2313",
"2314",
"2317",
"2318",
"2319",
"2320",
"2322",
"2323",
"2324",
"2326",
"2327",
"2328",
"2329",
"2330",
"2331",
"2333",
"2336",
"2337",
"2338",
"2339",
"2340",
"2341",
"2342",
"2343",
"2345",
"2348",
"2349",
"2355",
"2356",
"2357",
"2358",
"2362",
"2363",
"2366",
"2368",
"2369",
"2371",
"2377",
"2378",
"2379",
"2380",
"2382",
"2383",
"2386",
"2388",
"2389",
"2393",
"2398",
"2399",
"2448",
"2488",
"2588",
"2600",
"2601",
"2607",
"2608",
"2611",
"2623",
"2628",
"2633",
"2638",
"2662",
"2663",
"2666",
"2668",
"2669",
"2678",
"2683",
"2698",
"2699",
"2700",
"2708",
"2722",
"2727",
"2728",
"2738",
"2768",
"2777",
"2779",
"2788",
"2789",
"2799",
"2858",
"2863",
"2866",
"2868",
"2869",
"2877",
"2878",
"2880",
"2882",
"2883",
"2886",
"2888",
"2889",
"2898",
"2899",
"2906",
"2970",
"2971",
"2972",
"2973",
"3339",
"3344",
"3355",
"3358",
"3360",
"3363",
"3366",
"3368",
"3369",
"3377",
"3378",
"3380",
"3382",
"3383",
"3389",
"3393",
"3395",
"3396",
"3398",
"3399",
"3600",
"3606",
"3608",
"3613",
"4338",
"4601",
"4603",
"4604",
"4605",
"4606",
"4607",
"4608",
"4609",
"4610",
"4611",
"4612",
"4613",
"4614",
"4615",
"4616",
"6030",
"6033",
"6036",
"6038",
"6060",
"6066",
"6068",
"6080",
"6083",
"6088",
"6090",
"6098",
"6099",
"6100",
"6108",
"6113",
"6116",
"6118",
"6119",
"6122",
"6123",
"6128",
"6133",
"6136",
"6138",
"6139",
"6158",
"6160",
"6161",
"6163",
"6166",
"6168",
"6169",
"6178",
"6182",
"6183",
"6188",
"6189",
"6190",
"6196",
"6198",
"6288",
"6808",
"6816",
"6818",
"6822",
"6823",
"6826",
"6828",
"6829",
"6830",
"6833",
"6836",
"6837",
"6838",
"6839",
"6858",
"6860",
"6863",
"6865",
"6866",
"6868",
"6869",
"6877",
"6878",
"6880",
"6881",
"6882",
"6885",
"6886",
"6888",
"6889",
"6893",
"6896",
"6898",
"6899",
"8001",
"8003",
"8005",
"8006",
"8007",
"8009",
"8011",
"8013",
"8016",
"8018",
"8019",
"8020",
"8021",
"8022",
"8023",
"8025",
"8026",
"8027",
"8028",
"8029",
"8030",
"8031",
"8032",
"8033",
"8035",
"8037",
"8039",
"8040",
"8041",
"8043",
"8045",
"8046",
"8047",
"8048",
"8158",
"8159",
"8160",
"8161",
"8162",
"8163",
"8400",
"8401",
"8402",
"8403",
"8405",
"8406",
"8407",
"8409",
"8410",
"8411",
"8412",
"8413",
"8415",
"8416",
"8417",
"6030",
"6033",
"6036",
"6038",
"6060",
"6066",
"6068",
"6080",
"6083",
"6088",
"6090",
"6098",
"6099",
"6100",
"6108",
"6113",
"6116",
"6118",
"6119",
"6122",
"6123",
"6128",
"6133",
"6136",
"6138",
"6139",
"6158",
"6160",
"6161",
"6163",
"6166",
"6168",
"6169",
"6178",
"6182",
"6183",
"6188",
"6189",
"6190",
"6196",
"6198",
"6288",
"6818",
"6822",
"6823",
"6826",
"6828",
"6829",
"6830",
"6833",
"6836",
"6837",
"6838",
"6839",
"6858",
"6860",
"6863",
"6865",
"6866",
"6868",
"6869",
"6877",
"6878",
"6880",
"6881",
"6882",
"6885",
"6886",
"6888",
"6889",
"6893",
"6896",
"6898",
"6899",
"8001",
"8003",
"8035",
"8037",
"8039",
"8040",
"8041",
"8043",
"8045",
"8046",
"8048",
"8049",
"8050",
"8051",
"8052",
"8053",
"8055",
"8056",
"8057",
"8059",
"8060",
"8062",
"8063",
"8065",
"8066",
"8067",
"8069",
"8070",
"8071",
"8072",
"8073",
"8075",
"8076",
"8078",
"8079",
"8080",
"8081",
"8082",
"8083",
"8085",
"8086",
"8087",
"8088",
"8089",
"8090",
"8091",
"8092",
"8093",
"8095",
"8098",
"8100",
"8101",
"8103",
"8105",
"8106",
"8107",
"8108",
"8109",
"8111",
"8112",
"8113",
"8115",
"8116",
"8117",
"8118",
"8119",
"8120",
"8121",
"8123",
"8125",
"8126",
"8128",
"8129",
"8130",
"8131",
"8132",
"8133",
"8135",
"8136",
"8137",
"8139",
"8140",
"8142",
"8143",
"8146",
"8147",
"8148",
"8149",
"8150",
"8151",
"8152",
"8153",
"8155",
"8156",
"8157",
"8158",
"8159",
"8160",
"8161",
"8162",
"8163",
"8165",
"8166",
"8167",
"8168",
"8169",
"8170",
"8171",
"8172",
"8173",
"8175",
"8176",
"8178",
"8179",
"8181",
"8182",
"8183",
"8186",
"8187",
"8188",
"8189",
"8190",
"8191",
"8192",
"8193",
"8195",
"8196",
"8197",
"8198",
"8199",
"8200",
"8201",
"8202",
"8203",
"8205",
"8206",
"8207",
"8210",
"8211",
"8212",
"8213",
"8215",
"8217",
"8218",
"8219",
"8220",
"8221",
"8222",
"8223",
"8225",
"8226",
"8227",
"8228",
"8229",
"8230",
"8231",
"8232",
"8235",
"8236",
"8237",
"8238",
"8239",
"8240",
"8241",
"8242",
"8243",
"8245",
"8246",
"8247",
"8249",
"8250",
"8251",
"8252",
"8255",
"8256",
"8257",
"8258",
"8260",
"8262",
"8265",
"8266",
"8267",
"8268",
"8269",
"8270",
"8271",
"8272",
"8273",
"8275",
"8277",
"8278",
"8279",
"8280",
"8281",
"8282",
"8283",
"8285",
"8286",
"8287",
"8290",
"8291",
"8292",
"8293",
"8295",
"8296",
"8297",
"8299",
"8300",
"8301",
"8305",
"8306",
"8307",
"8308",
"8309",
"8310",
"8311",
"8312",
"8313",
"8315",
"8316",
"8317",
"8319",
"8320",
"8321",
"8325",
"8326",
"8328",
"8329",
"8331",
"8333",
"8337",
"8340",
"8341",
"8342",
"8343",
"8345",
"8346",
"8347",
"8348",
"8349",
"8350",
"8351",
"8353",
"8355",
"8356",
"8357",
"8358",
"8359",
"8360",
"8361",
"8362",
"8363",
"8365",
"8366",
"8367",
"8368",
"8370",
"8371",
"8372",
"8373",
"8375",
"8376",
"8377",
"8379",
"8383",
"8385",
"8391",
"8392",
"8395",
"8400",
"8401",
"8402",
"8403",
"8405",
"8406",
"8407",
"8409",
"8410",
"8411",
"8412",
"8413",
"8415",
"8416",
"8417",
"8419",
"8420",
"8421",
"8422",
"8423",
"8425",
"8426",
"8427",
"8428",
"8429",
"8430",
"8431",
"8432",
"8436",
"8437",
"8439",
"8442",
"8445",
"8446",
"8447",
"8448",
"8450",
"8451",
"8452",
"8455",
"8456",
"8457",
"8460",
"8462",
"8463",
"8465",
"8469",
"8470",
"8471",
"8472",
"8473",
"8475",
"8476",
"8479",
"8480",
"8481",
"8482",
"8483",
"8485",
"8487",
"8490",
"8491",
"8493",
"8495",
"8501",
"8502",
"8506",
"8507",
"8509",
"8510",
"8511",
"8512",
"8513",
"8519",
"8521",
"8522",
"8523",
"8525",
"8526",
"8527",
"8532",
"8535",
"8536",
"8540",
"8545",
"8547",
"8551",
"8552",
"8553",
"8606",
"8609",
"8506",
"8507",
"8509",
"8510",
"8511",
"8512",
"8513",
"8519",
"8521",
"8522",
"8523",
"8525",
"8526",
"8527",
"8532",
"8535",
"8536",
"8540",
"8545",
"8547",
"8551",
"8552",
"8553",
"8606",
"8609",
"80737",
"84602"]
    for i in codes:
        try:           
            if i in completed:
                continue
            code = '0' * (5 - len(str(i))) + str(i)
            url = pre + code             
            url2 = url.replace("/en/", "/tc/")
            
            print (url, url2)
            with open(dir + str(i) + ".txt", "w", encoding='utf-8') as outp:
                text = getText(url, "en")

                if text.isspace():
                    break
                outp.write(text)
                print ("File",i,"created (English).")
                                
            with open(dir + str(i) + "_C.txt", "w", encoding='utf-8') as outp:
                text = getText(url2, "zh")
                outp.write(text)
                print ("File",i,"created (Chinese).")
            
        except Exception as e:
            print(e)
    return

if __name__ == "__main__":
    # getURL()
    getData()
    