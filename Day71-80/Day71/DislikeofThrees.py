# x=1666
# i=1
# arr=[]
# while i<x+1:
#     if i%3==0 or i%10==3:
#         continue
#     else:
#         arr.append(i)
#     i+=1
# print(arr)
x = 1000
i = 1
arr = []
while len(arr) < x:
    if i % 3 != 0 and i % 10 != 3:
        arr.append(i)
    i += 1
# print(arr)
# arr=[1, 2, 4, 5, 7, 8, 10, 11, 14, 16, 17, 19, 20, 22, 25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 40, 41, 44, 46, 47, 49, 50, 52, 55, 56, 58, 59, 61, 62, 64, 65, 67, 68, 70, 71, 74, 76, 77, 79, 80, 82, 85, 86, 88, 89, 91, 92, 94, 95, 97, 98, 100, 101, 104, 106, 107, 109, 110, 112, 115, 116, 118, 119, 121, 122, 124, 125, 127, 128, 130, 131, 134, 136, 137, 139, 140, 142, 145, 146, 148, 149, 151, 152, 154, 155, 157, 158, 160, 161, 164, 166, 167, 169, 170, 172, 175, 176, 178, 179, 181, 182, 184, 185, 187, 188, 190, 191, 194, 196, 197, 199, 200, 202, 205, 206, 208, 209, 211, 212, 214, 215, 217, 218, 220, 221, 224, 226, 227, 229, 230, 232, 235, 236, 238, 239, 241, 242, 244, 245, 247, 248, 250, 251, 254, 256, 257, 259, 260, 262, 265, 266, 268, 269, 271, 272, 274, 275, 277, 278, 280, 281, 284, 286, 287, 289, 290, 292, 295, 296, 298, 299, 301, 302, 304, 305, 307, 308, 310, 311, 314, 316, 317, 319, 320, 322, 325, 326, 328, 329, 331, 332, 334, 335, 337, 338, 340, 341, 344, 346, 347, 349, 350, 352, 355, 356, 358, 359, 361, 362, 364, 365, 367, 368, 370, 371, 374, 376, 377, 379, 380, 382, 385, 386, 388, 389, 391, 392, 394, 395, 397, 398, 400, 401, 404, 406, 407, 409, 410, 412, 415, 416, 418, 419, 421, 422, 424, 425, 427, 428, 430, 431, 434, 436, 437, 439, 440, 442, 445, 446, 448, 449, 451, 452, 454, 455, 457, 458, 460, 461, 464, 466, 467, 469, 470, 472, 475, 476, 478, 479, 481, 482, 484, 485, 487, 488, 490, 491, 494, 496, 497, 499, 500, 502, 505, 506, 508, 509, 511, 512, 514, 515, 517, 518, 520, 521, 524, 526, 527, 529, 530, 532, 535, 536, 538, 539, 541, 542, 544, 545, 547, 548, 550, 551, 554, 556, 557, 559, 560, 562, 565, 566, 568, 569, 571, 572, 574, 575, 577, 578, 580, 581, 584, 586, 587, 589, 590, 592, 595, 596, 598, 599, 601, 602, 604, 605, 607, 608, 610, 611, 614, 616, 617, 619, 620, 622, 625, 626, 628, 629, 631, 632, 634, 635, 637, 638, 640, 641, 644, 646, 647, 649, 650, 652, 655, 656, 658, 659, 661, 662, 664, 665, 667, 668, 670, 671, 674, 676, 677, 679, 680, 682, 685, 686, 688, 689, 691, 692, 694, 695, 697, 698, 700, 701, 704, 706, 707, 709, 710, 712, 715, 716, 718, 719, 721, 722, 724, 725, 727, 728, 730, 731, 734, 736, 737, 739, 740, 742, 745, 746, 748, 749, 751, 752, 754, 755, 757, 758, 760, 761, 764, 766, 767, 769, 770, 772, 775, 776, 778, 779, 781, 782, 784, 785, 787, 788, 790, 791, 794, 796, 797, 799, 800, 802, 805, 806, 808, 809, 811, 812, 814, 815, 817, 818, 820, 821, 824, 826, 827, 829, 830, 832, 835, 836, 838, 839, 841, 842, 844, 845, 847, 848, 850, 851, 854, 856, 857, 859, 860, 862, 865, 866, 868, 869, 871, 872, 874, 875, 877, 878, 880, 881, 884, 886, 887, 889, 890, 892, 895, 896, 898, 899, 901, 902, 904, 905, 907, 908, 910, 911, 914, 916, 917, 919, 920, 922, 925, 926, 928, 929, 931, 932, 934, 935, 937, 938, 940, 941, 944, 946, 947, 949, 950, 952, 955, 956, 958, 959, 961, 962, 964, 965, 967, 968, 970, 971, 974, 976, 977, 979, 980, 982, 985, 986, 988, 989, 991, 992, 994, 995, 997, 998, 1000, 1001, 1004, 1006, 1007, 1009, 1010, 1012, 1015, 1016, 1018, 1019, 1021, 1022, 1024, 1025, 1027, 1028, 1030, 1031, 1034, 1036, 1037, 1039, 1040, 1042, 1045, 1046, 1048, 1049, 1051, 1052, 1054, 1055, 1057, 1058, 1060, 1061, 1064, 1066, 1067, 1069, 1070, 1072, 1075, 1076, 1078, 1079, 1081, 1082, 1084, 1085, 1087, 1088, 1090, 1091, 1094, 1096, 1097, 1099, 1100, 1102, 1105, 1106, 1108, 1109, 1111, 1112, 1114, 1115, 1117, 1118, 1120, 1121, 1124, 1126, 1127, 1129, 1130, 1132, 1135, 1136, 1138, 1139, 1141, 1142, 1144, 1145, 1147, 1148, 1150, 1151, 1154, 1156, 1157, 1159, 1160, 1162, 1165, 1166, 1168, 1169, 1171, 1172, 1174, 1175, 1177, 1178, 1180, 1181, 1184, 1186, 1187, 1189, 1190, 1192, 1195, 1196, 1198, 1199, 1201, 1202, 1204, 1205, 1207, 1208, 1210, 1211, 1214, 1216, 1217, 1219, 1220, 1222, 1225, 1226, 1228, 1229, 1231, 1232, 1234, 1235, 1237, 1238, 1240, 1241, 1244, 1246, 1247, 1249, 1250, 1252, 1255, 1256, 1258, 1259, 1261, 1262, 1264, 1265, 1267, 1268, 1270, 1271, 1274, 1276, 1277, 1279, 1280, 1282, 1285, 1286, 1288, 1289, 1291, 1292, 1294, 1295, 1297, 1298, 1300, 1301, 1304, 1306, 1307, 1309, 1310, 1312, 1315, 1316, 1318, 1319, 1321, 1322, 1324, 1325, 1327, 1328, 1330, 1331, 1334, 1336, 1337, 1339, 1340, 1342, 1345, 1346, 1348, 1349, 1351, 1352, 1354, 1355, 1357, 1358, 1360, 1361, 1364, 1366, 1367, 1369, 1370, 1372, 1375, 1376, 1378, 1379, 1381, 1382, 1384, 1385, 1387, 1388, 1390, 1391, 1394, 1396, 1397, 1399, 1400, 1402, 1405, 1406, 1408, 1409, 1411, 1412, 1414, 1415, 1417, 1418, 1420, 1421, 1424, 1426, 1427, 1429, 1430, 1432, 1435, 1436, 1438, 1439, 1441, 1442, 1444, 1445, 1447, 1448, 1450, 1451, 1454, 1456, 1457, 1459, 1460, 1462, 1465, 1466, 1468, 1469, 1471, 1472, 1474, 1475, 1477, 1478, 1480, 1481, 1484, 1486, 1487, 1489, 1490, 1492, 1495, 1496, 1498, 1499, 1501, 1502, 1504, 1505, 1507, 1508, 1510, 1511, 1514, 1516, 1517, 1519, 1520, 1522, 1525, 1526, 1528, 1529, 1531, 1532, 1534, 1535, 1537, 1538, 1540, 1541, 1544, 1546, 1547, 1549, 1550, 1552, 1555, 1556, 1558, 1559, 1561, 1562, 1564, 1565, 1567, 1568, 1570, 1571, 1574, 1576, 1577, 1579, 1580, 1582, 1585, 1586, 1588, 1589, 1591, 1592, 1594, 1595, 1597, 1598, 1600, 1601, 1604, 1606, 1607, 1609, 1610, 1612, 1615, 1616, 1618, 1619, 1621, 1622, 1624, 1625, 1627, 1628, 1630, 1631, 1634, 1636, 1637, 1639, 1640, 1642, 1645, 1646, 1648, 1649, 1651, 1652, 1654, 1655, 1657, 1658, 1660, 1661, 1664, 1666]
x=int(input())
for _ in range(x):
    a=int(input())
    print(arr[a-1])
