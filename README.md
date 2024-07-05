Objective: Predict Yield of Various Crops that grow in given soil(by user).

Inputs : Type of Soil,CropName, Climate Conditions(Taken from Weather APIs)

Output : Yield

Current Progress: SVR model R2 value: 0.725(Good Fit),trying additional models and finding more features to include(Training is done on 1 location to test relevance) 

Main Datasets used:
1)NASA Climate condtions consisting of 
(ALLSKY_SFC_PAR_TOT	ALLSKY_SFC_SW_DIFF	ALLSKY_SFC_SW_DNI	ALLSKY_SFC_SW_DWN	CLOUD_AMT	
CLRSKY_SFC_SW_DWN	PRECTOTCORR	PRECTOTCORR_SUM	PS	QV2M	RH2M	T2M_MAX	T2M_MIN	T2M_RANGE	WS50M	WSC)
humidity ,rainfall ,solar parameters for estimating crop growth ,temperature etc.

2)Icrisat on Details of crop yield in form of time-series data

