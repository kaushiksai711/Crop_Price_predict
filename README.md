Objective: Predict Yield of Various Crops that grow in given soil(by user).

Inputs : Type of Soil,CropName, Climate Conditions(Taken from Weather APIs)
Experimented Inputs: Crop name, Location ,3-4 climate parameters(removed many climate parameters due to low correlation with yield)

Output : Yield
Progress:Currently Applied on 1 crop 1 location with parameters leading to MAE:0.07 and R2 score :0.61(Dataset used:updated_dist_data_2.0 - Sheet1.csv) (SVR model with params)

Main Datasets used:
1)NASA Climate condtions consisting of 
(ALLSKY_SFC_PAR_TOT	ALLSKY_SFC_SW_DIFF	ALLSKY_SFC_SW_DNI	ALLSKY_SFC_SW_DWN	CLOUD_AMT	
CLRSKY_SFC_SW_DWN	PRECTOTCORR	PRECTOTCORR_SUM	PS	QV2M	RH2M	T2M_MAX	T2M_MIN	T2M_RANGE	WS50M	WSC)
humidity ,rainfall ,solar parameters for estimating crop growth ,temperature etc.

2)Icrisat on Details of crop yield in form of time-series data
