# not working properly
import re
str='''Skip to main contentSkip to footer

Contact UsShare
 
Like what you see?
Let's talk arrow

Infosys - Asia Pacific

Select Country/region
Armenia
Yerevan
22 Hanrapetutyan Street Suite 5,
Yerevan, 0010, Armenia

Australia
Brisbane - Portland
Level 4, 40 Creek St,
Brisbane QLD 4000,
Australia
Phone +61 3 9860 2000​

Canberra
Level 3, Workspace 3.01,
33 Allara street,
Canberra, ACT 2601
Phone +61 3 9860 2000

Melbourne (Head Office)
Two Melbourne Quarter
Level 4, 697 Collins Street
Docklands, 3008 VIC

Postal: PO Box 528
Collins Street
West Melbourne VIC 8007
Phone +61 3 9860 2000
Fax +61 3 9860 2999

Perth - Portland
The Forrest Centre,
Level 29, 221 St Georges Tce,
Perth WA 6000.
Phone +61 3 9860 2000
Sydney
Level 3, 100 Arthur Street,
North Sydney 2060
NSW, Australia
Tel: +61 2 8912 1500
Fax: +61 2 8912 1555

China
Beijing
Unit 1238, Level 12,​
China Resources Building,​
8 Jianguomenbei Avenue,​
Dongcheng District​
Beijing 100005​

Dalian
10/F, Ascendas Software Park
Phase 2, No. 7,Hui Xian Yuan
Dalian Hi-tech Industrial Zone
Dalian 116 023​
Phone +86 411 39981001
Hangzhou
12F, fangtianxia building,
No. 82Yueda lane,
Binjiang District
Hangzhou 310052
Phone +86 571 87930031
Fax +86 571 87930001

Shanghai
No. 506, Ziyue Road,
Minhang District,
Shanghai, 200241
Phone +86 21 58843000
Fax +86 21 58843001

Shenzhen
Unit 1301-1309, Building 11,
Tianan Cloud Park,
No. 2018 Xuegang Road,
Longgang District,
Shenzhen 518129
Phone +86 21 58843174

17/F,
No. 1 Yuexing 4th Road,
Nanshan District,
Shenzhen 518063

Hong Kong
Hong Kong
Suite 01-03, Level 43,
Champion Tower,
Three Garden Road,
Central, Hong Kong
Phone +852 215 892 70
+852 215 892 71

India
Bengaluru
Plot no. 44/97 A, 3rd cross,
Electronic City,
Hosur Road,
Bengaluru - 560 100
Phone +91 80 2852 0261
Fax +91 80 2852 0362

Offshore Development Center, Plot No. 26A
Electronics City, Plot No. 26AHosur Road
Bengaluru​ 560 100
Phone +91 80 2852 0261
Fax +91 80 2852 0362

IIPM STP UNIT OFFSHORE Development Centre,
SY No. 41(P), 40(P),
Konappana Agrahara Village,
Begur Hobli,
Bengaluru South,
Electronic City P-II,
Bengaluru - 560 100
Phone +91 80 4615 2999

EQUINOX OFFSHORE Development Centre,​
Plot no.47, 1st Main Road,​
Electronics City, Phase1,​
Bengaluru - 560 100​
Phone ​+91 80 3952 1166

​M&C BUILDING OFFSHORE Development Centre,
Sy No. Part- 157, Plot No. 53, Electronics City,
Hosur Road,
Bengaluru - 560 100
Phone +91 80 3331 7777
Fax +​91 80 3331 7333

Manipal Center,
#403, 4th Floor,
North Block, Front Wing,
Dickenson Road, Manipal Centre,
Bengaluru - 560 042
Phone +91 80 2559 5426

Focus Towers
Plot No. 22, 1st Main, 1st Phase,
Electronic City,
Bengaluru - 560 100
Phone +91 80 4635 0027

Centralized Processing Center
'Prestige Alpha'
No.48/1,48/2, Beratenagrahara,
Begur Hobli, Hosur Road,
Bengaluru - 560 100
Phone +91 80 4345 6789

EdgeVerve Systems,
GOLD HILL OFFSHORE Development Centre
Gold Hill Supreme So, 1st Floor, Electronics City Phase 2, Near TCS,
Bengaluru - 560 100
Phone +91 80 4653 8001​

MILESTONE SEZ UNIT OFFSHORE Development Centre,
Bhartiya Centre of Information Technology (BCIT), Bhartiya,
Block 1, Thanisandra Main Road, Chokkanahalli,
Bengaluru - 560 064
Phone +91 80 4615 4800

SEZ UNIT I, OFFSHORE Development Centre,
Sy No.64, 65, 157, 158 & 161,
Electronic City, Doddathogur Village, Begur Hobli,
Bengaluru - 560 100
Phone +91 80 6856 0014

JP IT PARK OFFSHORE Development Centre,
Konappan Agrahara Village,
Begur Hobli, Electronic City,
Bengaluru - 560 100
Phone +91 4921 0550

Bhubaneswar
STPI
Plot No-E/4
Info City
Bhubaneswar - 751 024
Odisha, India
Phone +91 674-6656100
+91 674-6656150
+91 674-6652200
+91 674-6722700
+91 674-6722800
Fax +91 674 232 0186

Plot No – PB 1, NE 1, NP 1
Info Valley, IDCO IT / ITES SEZ
Vill. –Gaudakashipur & Arisal
Bhubaneswar - 752054
Dist. – Khurda
Odisha
Phone +91 674-6656100
+91 674-6656150
+91 674-6652200
+91 674-6722700
+91 674-6722800

Chandigarh
Plot No. 1
Rajiv Gandhi Technology Park
Kishangarh
Chandigarh 160 101
Phone +91 172 503 8000
Fax +91 172 504 6860

Chennai
138, Old Mahabalipuram Road,
Sholinganallur, Chennai,
Tamil Nadu – 600119.
Phone +91 44 2450 9530/9540

Plot No.TP1/1, Central Avenue
Techno Park (SEZ)
Mahindra World City
Chengalpet
Kancheepuram District – 603 004
Phone +91 44 4741 1111
Fax +91 44 4741 5151​

AKDR Tower, No 3/381 3rd Floor,
Rajiv Gandhi Salai (OMR),
Mettukuppam, Chennai-600097
Phone +91 44 2450 9530/9540

Pacifica Tech Park Survey No: 76 No-23
Rajiv Gandhi Salai (OMR),
Navalur Chennai -600130
Phone +91 44 2450 9530/9540

Gurgaon
Uniworld Tower B
Village Tikri
Sector 48
Gurugram - 122 018
Phone +91 124 447 9527
Hubballi
Gokul Hobli, Hubballi Taluk,
Near Hubballi Airport,
Dharwad District,
Karnataka – 580030, lndia.

Hyderabad
Survey No. 210,
Manikonda Village,
Lingampally,
Rangareddy (Dist.),
Hyderabad 500 032
Phone +91 40 6642 0000
Fax +91 40 2300 5223

Survey No. 41 (Pt),50 (pt),
Pocharam Village,
Singapore Township PO,
Ghatkesar Mandal,
Malkajgiri - Medchal District,
Hyderabad, 500088, India
Phone +91 40 40600000
Fax +91 40 66341356

Indore
Near Super Corridor
Scheme No. 151 and 169B
Village - Bada Bangarda and Tigaria badshah
Tehsil - Hetod
Indore
Madhya Pradesh - 453 112
Phone +91 731 474 7200
Jaipur
Plot No. IT-A-001-A-1
Mahindra World City SEZ
Village Kalwara
Tehsil Sanganer
Dist. Jaipur – 302 037
Rajasthan
Phone +91 141 3965 000
Fax +91 141 3965 100

Mangaluru
Kuloor Ferry Road, Kottara
Mangaluru​ 575 006
Phone +91 824 245 1485
+91 824 431 2222

Kamblapadavu
Kurnad Post, Pajeeru Village
Bantwal Taluk - 574 153
Dakshina Kannada (Dist.)
Phone +91 824 442 2800
+91 824 223 4701 to 720
+91 824 431 2222

Mohali
Plot No.I-3, Sector 83-A, IT City,
SAS Nagar, Mohali,
Punjab - 160062
Phone +91 172 430 6000
Fax +91 172 504 6860

Level 9 & 10, Landmark Plaza Building (F3 Tower),
Plot No. A-40A, Phase-VIII B,
Sahibzada Ajit Singh Nagar,
Industrial Area Sector 75, Mohali,
Punjab - 160059
Phone +91 172 338 4000
Fax +91 172 504 6860

Mumbai
85, 'C',
Mittal Towers, 8th Floor
Nariman Point
Mumbai - 400 021
Phone +91 22 4017 1017

11Th Floor, South Tower,
Godrej One Pirojshanagar
Easter Express Highway Vikhroli - East,
Mumbai, Maharashtra – 400079
Phone +91 93073 05047

Mysuru
No. 350, Hebbal Electronics City
Hootagalli
Mysuru 570 027
Phone +91 821 240 4101
Fax +91 821 240 4200

Nagpur
SEZ Co-Developer,
Plot No. 07, Sector-17,
Special Economic Zone, MIHAN,
Nagpur 441 108
Phone +91 712 669 8200
IL Nagpur SEZ Unit 2
Building A1, 5th Floor,
SP Infocity, Sector-1,
MIHAN SEZ,
Nagpur Maharashtra - 441 108
Phone +91 712 669 8200

Pune
Plot No.1, Rajiv Gandhi Infotech Park,
Hinjawadi, Phase-I,
Pune, Maharashtra-411057.
Phone +91 20 2293 2800
Fax +91 20 2293 2832

Plot No.24/2, Rajiv Gandhi Infotech Park,
Hinjawadi, Taluka-Mulshi,
Pune, Maharashtra-411057
Phone +91 20 3982 7000
Fax +91 20 3982 8000

Plot No.24/3, Village-Maan,
Rajiv Gandhi Infotech Park,
Phase-II, Taluka-Mulshi,
Pune, Maharashtra-411057
Phone +91 20 3982 7000
Fax +91 20 3982 8000

Ascendas SEZ Unit
Building - Juniper
International Tech Park,
Rajiv Gandhi Infotech Park, MIDC, Phase-III,
Hinjawadi, Pune- 411 057
Phone +91 20 3982 7000
Fax +91 20 3982 8000

Unit No. 702, Level 7, Wing B,
Tower XII, Cybercity,
Magarpatta City, Hadapsar,
Pune – 411 013
Phone +91 20 3982 7000
Fax +91 20 3982 8000

EdgeVerve Systems
Ground and 1st Floor,
Dassault Systems Dassault Systems Solutions Lab Pvt. Ltd (Formerly Panchshil Tech Park Pvt. Ltd), Tower-B, Plot No. 15A,
Rajiv Gandhi Infotech Park, Phase-I,
Hinjawadi, Taluka-Mulshi,
Pune, Maharashtra-411057
Phone +91 20 6793 6600
Fax +91 20 6675 0827

Thiruvananthapuram
Plot No. 1, Technopark
Campus II, Attipra Village
Thiruvananthapuram 695 583
Phone +91 471 398 2222
Fax +91 471 241 6177

Japan
Nagoya
Regus Hirokoji Garden Avenue Centre
Hirokoji Garden Avenue 4-24-16
Meieki Nakamura-ku
Nagoya city, Aichi Japan
450-0002
Phone +81 3 5545 3251
Fax +81 3 5545 3252​

Osaka
Level 18, Hilton Plaza West,
2-2-2 Umeda, Kita-ku, Osaka City,
Osaka, Japan 530-0001
Phone +81 6 6133 4636
Fax +81 3 5545 3252

Tokyo
Izumi Garden Wing
1-6-3, Roppongi,
Minato-ku, Tokyo 106 0032
Phone +81 3 5545 3251
Fax +81 3 5545 3252

Malaysia
Malaysia
Level 13A -1
Mercu UEM
Jalan Stesen Sentral 5,
Kuala Lumpur Sentral,
Kuala Lumpur 50470
Phone +60 03 2772 1200
New Zealand
Auckland
Infosys House
Level 7, 79 Queen Street,
Auckland 1010
Phone +64 9 3019906​
PO Box 91397,
Victoria Street,
Auckland 1142​

Wellington
Level 15, 171 Featherston Street
Wellington, 6011
New Zealand
Phone +64 9 3019906
Philippines
Manila
6th Floor, Cyber One Building,
11 Eastwood Avenue,
Eastwood Cyberpark,
Bagumbayan, Quezon City
Manila

Singapore
Singapore
CBP office
#05 -01/03.
1,Changi Business Park Crescent,
Plaza 8, Tower A
Singapore 486025
Phone +65 6671 2200
Fax +65 6671 2205

Suntec Office
Level 43 Unit 02,
Suntec Tower 2,
9 Temasek Blvd
Singapore 038989
Phone +65 6572 8400
Fax +65 6572 8405

1 Gateway Dr,
#07-01 Westgate Tower,
Singapore 608531
Phone +65 6801 0388

South Korea
Seoul
401 Campus 02,
4F, Haesung 1st Bldg
Teheran-Ro 504,
Gangnam-Gu
Seoul 06178

Taiwan
Taipei
Centre No. 1372,
Shin Kong Manhattan Building,
14F, Section 5, No. 8,
Xin Yi Road 110, Taipei

Company
Navigate your next
About Us
Careers
Corporate Responsibility
Investors
Newsroom
Alumni
Subsidiaries
EdgeVerve Systems
Infosys BPM
Infosys Consulting
Infosys Public Services
Programs
Infosys Foundation
Infosys Foundation USA
Infosys Science Foundation
Infosys Leadership Institute
Support
Terms of Use
Privacy Statement
Cookie Policy
Safe Harbour Provision
Trademarks
Site Map
Modern Slavery Statement
Payment Guide for Suppliers
Connect with us
Twitter Facebook LinkedIn YouTube
Copyright © 2022 Infosys Limited
+91 93 073 05047
Select Country/region
Arrow up'''
phone_nos=re.findall(r"^(\+91)[0-9\s]+",str)
for phone_no in phone_nos:
    print(phone_no)