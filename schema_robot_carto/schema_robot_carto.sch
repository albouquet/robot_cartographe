EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Sensor_Distance:VL53L1CXV0FY1 U?
U 1 1 656C982B
P 2500 2150
F 0 "U?" H 2830 2196 50  0000 L CNN
F 1 "VL53L1CXV0FY1" H 2830 2105 50  0000 L CNN
F 2 "Sensor_Distance:ST_VL53L1x" H 3175 1600 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 2600 2150 50  0001 C CNN
	1    2500 2150
	0    1    1    0   
$EndComp
$Comp
L Sensor_Distance:VL53L1CXV0FY1 U?
U 1 1 656CA5E6
P 4250 2150
F 0 "U?" H 4580 2196 50  0000 L CNN
F 1 "VL53L1CXV0FY1" H 4580 2105 50  0000 L CNN
F 2 "Sensor_Distance:ST_VL53L1x" H 4925 1600 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 4350 2150 50  0001 C CNN
	1    4250 2150
	0    1    1    0   
$EndComp
$Comp
L Sensor_Distance:VL53L1CXV0FY1 U?
U 1 1 656CB63F
P 6050 2150
F 0 "U?" H 6380 2196 50  0000 L CNN
F 1 "VL53L1CXV0FY1" H 6380 2105 50  0000 L CNN
F 2 "Sensor_Distance:ST_VL53L1x" H 6725 1600 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 6150 2150 50  0001 C CNN
	1    6050 2150
	0    1    1    0   
$EndComp
$Comp
L Sensor_Distance:VL53L1CXV0FY1 U?
U 1 1 656CB645
P 7750 2150
F 0 "U?" H 8080 2196 50  0000 L CNN
F 1 "VL53L1CXV0FY1" H 8080 2105 50  0000 L CNN
F 2 "Sensor_Distance:ST_VL53L1x" H 8425 1600 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/vl53l1x.pdf" H 7850 2150 50  0001 C CNN
	1    7750 2150
	0    1    1    0   
$EndComp
Wire Bus Line
	7750 1750 7750 1350
Wire Bus Line
	2500 1350 2500 1750
Wire Bus Line
	2500 1350 4250 1350
Wire Bus Line
	4250 1350 4250 1750
Connection ~ 4250 1350
Wire Bus Line
	4250 1350 6050 1350
Wire Bus Line
	6050 1350 6050 1750
Connection ~ 6050 1350
Wire Bus Line
	6050 1350 7750 1350
Wire Bus Line
	2500 1350 1250 1350
Wire Bus Line
	1250 1350 1250 5050
Wire Bus Line
	1250 5050 2550 5050
Wire Bus Line
	2550 5050 2550 5250
Connection ~ 2500 1350
Wire Bus Line
	2650 5250 2650 4850
Wire Bus Line
	2650 4850 1450 4850
Wire Bus Line
	1450 4850 1450 1550
Wire Bus Line
	1450 1550 2400 1550
Wire Bus Line
	2400 1550 2400 1750
Wire Bus Line
	2400 1550 4150 1550
Wire Bus Line
	4150 1550 4150 1750
Connection ~ 2400 1550
Wire Bus Line
	4150 1550 5950 1550
Wire Bus Line
	5950 1550 5950 1750
Connection ~ 4150 1550
Wire Bus Line
	5950 1550 7650 1550
Wire Bus Line
	7650 1550 7650 1750
Connection ~ 5950 1550
$Comp
L power:Earth #PWR?
U 1 1 656E2B96
P 1750 2200
F 0 "#PWR?" H 1750 1950 50  0001 C CNN
F 1 "Earth" H 1750 2050 50  0001 C CNN
F 2 "" H 1750 2200 50  0001 C CNN
F 3 "~" H 1750 2200 50  0001 C CNN
	1    1750 2200
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR?
U 1 1 656E3287
P 3500 2150
F 0 "#PWR?" H 3500 1900 50  0001 C CNN
F 1 "Earth" H 3500 2000 50  0001 C CNN
F 2 "" H 3500 2150 50  0001 C CNN
F 3 "~" H 3500 2150 50  0001 C CNN
	1    3500 2150
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR?
U 1 1 656E384D
P 5300 2150
F 0 "#PWR?" H 5300 1900 50  0001 C CNN
F 1 "Earth" H 5300 2000 50  0001 C CNN
F 2 "" H 5300 2150 50  0001 C CNN
F 3 "~" H 5300 2150 50  0001 C CNN
	1    5300 2150
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR?
U 1 1 656E3F27
P 7050 2150
F 0 "#PWR?" H 7050 1900 50  0001 C CNN
F 1 "Earth" H 7050 2000 50  0001 C CNN
F 2 "" H 7050 2150 50  0001 C CNN
F 3 "~" H 7050 2150 50  0001 C CNN
	1    7050 2150
	1    0    0    -1  
$EndComp
Wire Wire Line
	1750 2200 1900 2200
Wire Wire Line
	1900 2200 1900 2150
Wire Wire Line
	3500 2150 3650 2150
Wire Wire Line
	5300 2150 5450 2150
Wire Wire Line
	7050 2150 7150 2150
$Comp
L power:+3V8 #PWR?
U 1 1 656FC650
P 5450 3200
F 0 "#PWR?" H 5450 3050 50  0001 C CNN
F 1 "+3V8" H 5465 3373 50  0000 C CNN
F 2 "" H 5450 3200 50  0001 C CNN
F 3 "" H 5450 3200 50  0001 C CNN
	1    5450 3200
	1    0    0    -1  
$EndComp
$Comp
L Connector:Raspberry_Pi_2_3 RASPBERRY_PI_ZERO
U 1 1 656D6484
P 3150 6050
F 0 "RASPBERRY_PI_ZERO" V 3196 7394 50  0000 L CNN
F 1 "Raspberry_Pi_2_3" V 3105 7394 50  0000 L CNN
F 2 "" H 3150 6050 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 3150 6050 50  0001 C CNN
	1    3150 6050
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2200 1750 1600 1750
Wire Wire Line
	1600 1750 1600 3300
Wire Wire Line
	1600 3300 2850 3300
Wire Wire Line
	2850 3300 2850 5250
Wire Wire Line
	3950 1750 3350 1750
Wire Wire Line
	3350 1750 3350 3350
Wire Wire Line
	3350 3350 2950 3350
Wire Wire Line
	2950 3350 2950 5250
Wire Wire Line
	5750 1750 5150 1750
Wire Wire Line
	5150 1750 5150 2700
Wire Wire Line
	5150 2700 3500 2700
Wire Wire Line
	3500 2700 3500 3550
Wire Wire Line
	3500 3550 3050 3550
Wire Wire Line
	3050 3550 3050 5250
Wire Wire Line
	7450 1750 6800 1750
Wire Wire Line
	6800 1750 6800 2900
Wire Wire Line
	6800 2900 3700 2900
Wire Wire Line
	3700 2900 3700 3850
Wire Wire Line
	3700 3850 3250 3850
Wire Wire Line
	3250 3850 3250 5250
$Comp
L power:+3V8 #PWR?
U 1 1 6570DD64
P 3100 1950
F 0 "#PWR?" H 3100 1800 50  0001 C CNN
F 1 "+3V8" H 3115 2123 50  0000 C CNN
F 2 "" H 3100 1950 50  0001 C CNN
F 3 "" H 3100 1950 50  0001 C CNN
	1    3100 1950
	1    0    0    -1  
$EndComp
Wire Wire Line
	3100 2150 3100 1950
$Comp
L power:+3V8 #PWR?
U 1 1 6570ECB6
P 4850 1950
F 0 "#PWR?" H 4850 1800 50  0001 C CNN
F 1 "+3V8" H 4865 2123 50  0000 C CNN
F 2 "" H 4850 1950 50  0001 C CNN
F 3 "" H 4850 1950 50  0001 C CNN
	1    4850 1950
	1    0    0    -1  
$EndComp
Wire Wire Line
	4850 2150 4850 1950
$Comp
L power:+3V8 #PWR?
U 1 1 6570FB3A
P 6650 1950
F 0 "#PWR?" H 6650 1800 50  0001 C CNN
F 1 "+3V8" H 6665 2123 50  0000 C CNN
F 2 "" H 6650 1950 50  0001 C CNN
F 3 "" H 6650 1950 50  0001 C CNN
	1    6650 1950
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 2150 6650 1950
$Comp
L power:+3V8 #PWR?
U 1 1 65710C08
P 8350 1950
F 0 "#PWR?" H 8350 1800 50  0001 C CNN
F 1 "+3V8" H 8365 2123 50  0000 C CNN
F 2 "" H 8350 1950 50  0001 C CNN
F 3 "" H 8350 1950 50  0001 C CNN
	1    8350 1950
	1    0    0    -1  
$EndComp
Wire Wire Line
	8350 2150 8350 1950
Wire Wire Line
	3950 5250 4100 5250
$Comp
L Driver_Motor:L298HN U?
U 1 1 659DE89E
P 5850 4400
F 0 "U?" V 5804 5144 50  0000 L CNN
F 1 "L298HN" V 5895 5144 50  0000 L CNN
F 2 "Package_TO_SOT_THT:TO-220-15_P2.54x2.54mm_StaggerOdd_Lead4.58mm_Vertical" H 5900 3750 50  0001 L CNN
F 3 "http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00000240.pdf" H 6000 4650 50  0001 C CNN
	1    5850 4400
	0    1    1    0   
$EndComp
$Comp
L Motor:Motor_DC M?
U 1 1 659DFA11
P 5300 5650
F 0 "M?" H 5458 5646 50  0000 L CNN
F 1 "Motor_DC" H 5458 5555 50  0000 L CNN
F 2 "" H 5300 5560 50  0001 C CNN
F 3 "~" H 5300 5560 50  0001 C CNN
	1    5300 5650
	0    -1   -1   0   
$EndComp
$Comp
L Motor:Motor_DC M?
U 1 1 659E00C8
P 6300 5650
F 0 "M?" H 6458 5646 50  0000 L CNN
F 1 "Motor_DC" H 6458 5555 50  0000 L CNN
F 2 "" H 6300 5560 50  0001 C CNN
F 3 "~" H 6300 5560 50  0001 C CNN
	1    6300 5650
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5600 5650 5600 5350
Wire Wire Line
	5600 5350 5750 5350
Wire Wire Line
	5750 5350 5750 5000
Wire Wire Line
	5100 5650 5100 5150
Wire Wire Line
	5100 5150 5650 5150
Wire Wire Line
	5650 5150 5650 5000
Wire Wire Line
	6100 5650 6100 5250
Wire Wire Line
	6100 5250 5950 5250
Wire Wire Line
	5950 5250 5950 5000
Wire Wire Line
	6600 5600 6600 5100
Wire Wire Line
	6600 5100 6050 5100
Wire Wire Line
	6050 5100 6050 5000
Wire Wire Line
	4100 3600 5750 3600
Wire Wire Line
	5750 3600 5750 3800
Wire Wire Line
	4100 3600 4100 5250
Wire Wire Line
	3650 5250 3650 4350
Wire Wire Line
	3650 4350 5050 4350
Wire Wire Line
	5050 4350 5050 3300
Wire Wire Line
	5050 3300 5850 3300
Wire Wire Line
	5850 3300 5850 3800
Wire Wire Line
	3550 5250 3550 4300
Wire Wire Line
	3550 4300 5000 4300
Wire Wire Line
	5000 4300 5000 3250
Wire Wire Line
	5000 3250 5950 3250
Wire Wire Line
	5950 3250 5950 3800
Wire Wire Line
	3450 5250 3450 4250
Wire Wire Line
	3450 4250 4950 4250
Wire Wire Line
	4950 4250 4950 3200
Wire Wire Line
	4950 3200 5450 3200
Wire Wire Line
	6250 3200 6250 3800
Connection ~ 5450 3200
Wire Wire Line
	5450 3200 6250 3200
Wire Wire Line
	3350 5250 3350 4200
Wire Wire Line
	3350 4200 4900 4200
Wire Wire Line
	4900 4200 4900 3150
Wire Wire Line
	4900 3150 6350 3150
Wire Wire Line
	6350 3150 6350 3800
Wire Wire Line
	6150 3550 4050 3550
Wire Wire Line
	4050 3550 4050 5200
Wire Wire Line
	4050 5200 3850 5200
Wire Wire Line
	3850 5200 3850 5250
Wire Wire Line
	6150 3550 6150 3800
Wire Wire Line
	5150 4400 5150 4900
Wire Wire Line
	5150 4900 4450 4900
Wire Wire Line
	4450 4900 4450 5750
$Comp
L power:+8V #PWR?
U 1 1 65A10A30
P 6750 4500
F 0 "#PWR?" H 6750 4350 50  0001 C CNN
F 1 "+8V" V 6765 4628 50  0000 L CNN
F 2 "" H 6750 4500 50  0001 C CNN
F 3 "" H 6750 4500 50  0001 C CNN
	1    6750 4500
	0    1    1    0   
$EndComp
Wire Wire Line
	6550 4500 6750 4500
Wire Wire Line
	6550 4400 7250 4400
Wire Wire Line
	7250 4400 7250 6300
Wire Wire Line
	7250 6300 5000 6300
Wire Wire Line
	5000 6300 5000 7100
Wire Wire Line
	5000 7100 1850 7100
Wire Wire Line
	1850 7100 1850 6250
$Comp
L power:+5V #PWR?
U 1 1 65A17912
P 7250 4400
F 0 "#PWR?" H 7250 4250 50  0001 C CNN
F 1 "+5V" H 7265 4573 50  0000 C CNN
F 2 "" H 7250 4400 50  0001 C CNN
F 3 "" H 7250 4400 50  0001 C CNN
	1    7250 4400
	1    0    0    -1  
$EndComp
Connection ~ 7250 4400
$EndSCHEMATC