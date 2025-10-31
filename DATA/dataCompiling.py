from sectionAraw import ICD_A00_A99_DATASET as sectionA
from sectionBraw import disease_data as sectionB
from sectionCraw import disease_data_rows as sectionC
from sectionDraw import disease_data as sectionD
from sectionEraw import disease_data as sectionE
from sectionFraw import disease_data as sectionF
from sectionGraw import disease_data as sectionG
from sectionHraw import disease_data as sectionH
from sectionIraw import disease_data as sectionI
from sectionJraw import disease_data as sectionJ
from sectionKraw import disease_data as sectionK
from sectionLraw import disease_data as sectionL
from sectionMraw import disease_data as sectionM
from sectionNraw import disease_data as sectionN
from sectionOraw import icd_data_rows as sectionO
from sectionPraw import icd_p_code_data as sectionP
from sectionQraw import disease_rows as sectionQ
from sectionRraw import icd_r_code_data as sectionR
from sectionSraw import icd_s_data as sectionS
from sectionTraw import icd_t_data as sectionT
from sectionVraw import icd_v_code_data as sectionV
from sectionWraw import icd_w_data as sectionW
from sectionXraw import icd_x_data as sectionX
from sectionYraw import icd_y_code_data as sectionY

uncommonOrder = [sectionT, sectionO, sectionL, sectionI]
for i in range(len(sectionI)):
    sectionI[i] = {key: sectionI[i][key] for key in ["geography", "transmission", "disease_type", "symptoms", "disease_name", "icd_code"]}
for k in range(len(sectionL)):
    sectionL[k] = {key: sectionL[k][key] for key in ["geography", "transmission", "disease_type", "symptoms", "disease_name", "icd_code"]}
for j in range(len(sectionO)):
    sectionO[j] = {key: sectionO[j][key] for key in ["Geography", "Transmission", "Disease Type", "Symptoms", "Disease Name", "ICD Code"]}

for a in range(len(sectionD)):
    sectionD[a] = sectionD[a].values()
for b in range(len(sectionI)):
    sectionI[b] = sectionI[b].values()
for c in range(len(sectionL)):
    sectionL[c] = sectionL[c].values()
for d in range(len(sectionM)):
    sectionM[d] = sectionM[d].values()
for e in range(len(sectionO)):
    sectionO[e] = sectionO[e].values()
for f in range(len(sectionR)):
    sectionR[f] = sectionR[f].values()
for h in range(len(sectionV)):
    sectionV[h] = sectionV[h].values()
for i in range(len(sectionW)):
    sectionW[i] = sectionW[i].values()
for j in range(len(sectionX)):
    sectionX[j] = sectionX[j].values()
for k in range(len(sectionY)):
    sectionY[k] = sectionY[k].values()

df = pd.DataFrame(columns = columns, data = sectionA + sectionB + sectionC + sectionD + sectionE + sectionF + sectionG + sectionH + sectionI + sectionJ + sectionK + sectionL + sectionM + sectionN + sectionO + sectionP + sectionQ + sectionR + sectionS + sectionT + sectionV + sectionW + sectionX + sectionY)
df.to_csv("NEAtrainset.csv", index = False)
