# -*- coding: utf-8 -*-
"""
Dataset rows for ICD-10 Codes Q00-Q99: Congenital malformations, 
deformations and chromosomal abnormalities.

This file contains the raw data as a list of lists, ready for export to CSV.

Data Structure:
[
    ['Geography', 'Transmission', 'Disease Type', 'Symptoms', 'Label', 'ICD Code']
    ... 100 data rows ...
]

A NOTE ON "TRANSMISSION" AND "DISEASE TYPE":
The requested ICD-10 range (Q00-Q99) concerns congenital, genetic, and 
chromosomal abnormalities. These conditions are NOT infectious.

Therefore, the 'Transmission' and 'Disease Type' features have been adapted 
to be medically accurate for this context:
- 'Transmission': This column uses terms like "Genetic", "Hereditary", 
  "Multifactorial", "Prenatal factors", "Teratogenic", or "Chromosomal" 
  to describe the etiology (origin) of the condition, as they are not 
  "transmitted" in the infectious sense (e.g., "waterborne", "airborne").
- 'Disease Type': This column uses "Structural", "Genetic", "Chromosomal", 
  or "Multifactorial" instead of "bacterial", "viral", etc., as these 
  are the correct medical classifications for these conditions.

Training an AI on this accurate data will yield a useful predictive model.
"""

# Header row for the CSV file
header = [
    'Geography', 
    'Transmission', 
    'Disease Type', 
    'Symptoms', 
    'Label', 
    'ICD Code'
]

# List of 100 data rows
disease_rows = [
    ['Worldwide', ['Multifactorial', 'Folic acid deficiency', 'Genetic factors'], 'Structural', ['Absence of brain', 'Absence of cranium (skull)', 'Exposed neural tissue', 'Facial abnormalities', 'Brainstem presence', 'Non-viable at birth'], 'Anencephaly and similar malformations', 'Q00'],
    ['Worldwide', ['Neural tube defect', 'Genetic factors', 'Prenatal factors'], 'Structural', ['Sac-like protrusion of brain/meninges', 'Protrusion through skull opening', 'Hydrocephalus', 'Vision problems', 'Seizures', 'Developmental delay'], 'Encephalocele', 'Q01'],
    ['Worldwide', ['Genetic factors', 'Prenatal infection (e.g., Zika)', 'Teratogen exposure'], 'Structural', ['Small head circumference', 'Developmental delay', 'Intellectual disability', 'Seizures', 'Facial distortions', 'Poor motor function'], 'Microcephaly', 'Q02'],
    ['Worldwide', ['Genetic factors', 'Prenatal infection', 'Aqueductal stenosis'], 'Structural', ['Rapidly increasing head size', 'Bulging fontanelle', 'Seizures', 'Poor feeding', 'Vomiting', 'Developmental delay'], 'Congenital hydrocephalus', 'Q03'],
    ['Worldwide', ['Genetic factors', 'Prenatal factors', 'Spontaneous mutation'], 'Structural', ['Varies widely', 'Seizures', 'Developmental delay', 'Motor impairment', 'Intellectual disability', 'Abnormal head shape'], 'Other congenital malformations of brain', 'Q04'],
    ['Worldwide', ['Neural tube defect', 'Folic acid deficiency', 'Genetic factors'], 'Structural', ['Opening in vertebral column', 'Protrusion of spinal cord (meningocele)', 'Nerve damage', 'Leg paralysis', 'Bowel/bladder problems', 'Hydrocephalus'], 'Spina bifida', 'Q05'],
    ['Worldwide', ['Genetic factors', 'Vascular disruption', 'Developmental anomaly'], 'Structural', ['Varies widely', 'Seizures', 'Hemiparesis', 'Developmental delay', 'Absence of spinal cord part', 'Sensory loss'], 'Other congenital malformations of spinal cord', 'Q06'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Varies widely', 'Headache', 'Hydrocephalus', 'Syringomyelia', 'Cranial nerve palsies', 'Balance problems'], 'Other congenital malformations of nervous system', 'Q07'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Varies widely', 'Blindness', 'Cataracts', 'Glaucoma', 'Microphthalmia', 'Strabismus'], 'Congenital malformations of eye (general)', 'Q10'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Prenatal infection (e.g., Rubella)'], 'Structural', ['Cloudy lens at birth', 'Vision impairment', 'White pupil (leukocoria)', 'Nystagmus (involuntary eye movement)', 'Strabismus', 'Microphthalmia'], 'Congenital cataract', 'Q11'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Small eyeball (microphthalmia)', 'Absent eyeball (anophthalmia)', 'Large eyeball (macrophthalmia)', 'Vision impairment', 'Orbital cysts', 'Associated facial anomalies'], 'Anophthalmos, microphthalmos and macrophthalmos', 'Q12'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Corneal opacity', 'Glaucoma', 'Iris abnormalities (aniridia)', 'Scleral abnormalities', 'Varies by specific condition', 'Vision impairment'], 'Congenital malformations of anterior segment of eye', 'Q13'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Retinal detachment', 'Chorioretinal coloboma', 'Optic nerve hypoplasia', 'Vitreous abnormalities', 'Poor vision', 'Nystagmus'], 'Congenital malformations of posterior segment of eye', 'Q14'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Associated syndromes'], 'Structural', ['Drooping eyelid (ptosis)', 'Inability to open eye', 'Ectropion (eyelid outward)', 'Entropion (eyelid inward)', 'Coloboma of eyelid', 'Abnormal eyelash growth'], 'Congenital malformations of eyelid, lacrimal apparatus and orbit', 'Q15'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Prenatal factors'], 'Structural', ['Small or absent outer ear (microtia/anotia)', 'Blocked ear canal (atresia)', 'Hearing loss', 'Preauricular skin tags', 'Abnormal ear position', 'Associated facial anomalies'], 'Congenital malformations of ear causing impairment of hearing', 'Q16'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Protruding ears', 'Malformed ear cartilage', 'Low-set ears', 'Preauricular sinus', 'Accessory auricle', 'Does not typically impair hearing'], 'Other congenital malformations of ear', 'Q17'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Associated syndromes'], 'Structural', ['Facial asymmetry', 'Malformed facial bones', 'Hearing loss', 'Ear abnormalities', 'Mandibular hypoplasia', 'Varies widely'], 'Other congenital malformations of face and neck', 'Q18'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Maternal health (e.g., diabetes)'], 'Structural', ['Cyanosis (blue skin)', 'Shortness of breath', 'Poor feeding (infants)', 'Heart murmur', 'Fatigue', 'Edema (swelling)'], 'Congenital malformations of cardiac chambers and connections', 'Q20'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Maternal health'], 'Structural', ['Heart murmur', 'Shortness of breath on exertion', 'Fatigue', 'Palpitations', 'Right heart enlargement', 'Pulmonary hypertension'], 'Congenital malformations of cardiac septa (ASD, VSD)', 'Q21'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Maternal health'], 'Structural', ['Heart murmur', 'Valve stenosis (narrowing)', 'Valve regurgitation (leaky)', 'Shortness of breath', 'Chest pain', 'Fatigue'], 'Congenital malformations of pulmonary and tricuspid valves', 'Q22'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Associated syndromes (e.g., Marfan)'], 'Structural', ['Heart murmur', 'Valve stenosis (narrowing)', 'Valve regurgitation (leaky)', 'Shortness of breath', 'Fatigue', 'Left ventricular hypertrophy'], 'Congenital malformations of aortic and mitral valves', 'Q23'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Maternal health'], 'Structural', ['Cyanosis', 'Shortness of breath', 'Poor feeding', 'Clubbing of fingers/toes', 'Heart murmur', 'Varies by specific defect (e.g., Tetralogy of Fallot)'], 'Other congenital malformations of heart', 'Q24'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Maternal health'], 'Structural', ['Hypertension in arms', 'Low blood pressure in legs', 'Leg cramps', 'Weak femoral pulse', 'Heart murmur', 'Shortness of breath'], 'Congenital malformations of great arteries (e.g., Coarctation of aorta)', 'Q25'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Maternal health'], 'Structural', ['Varies widely', 'Often asymptomatic', 'Pulmonary hypertension', 'Edema', 'Shortness of breath', 'Heart murmur'], 'Congenital malformations of great veins', 'Q26'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Maternal health'], 'Structural', ['Varies widely', 'Arteriovenous malformation (AVM)', 'Telangiectasia', 'Hemangioma', 'Port-wine stain', 'Risk of bleeding'], 'Other congenital malformations of peripheral vascular system', 'Q27'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Maternal health'], 'Structural', ['Varies widely', 'Lymphedema (swelling)', 'Cyanosis', 'Heart failure', 'Respiratory distress', 'Varies by specific defect'], 'Other congenital malformations of circulatory system', 'Q28'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Prenatal factors'], 'Structural', ['Blocked nasal passage (choanal atresia)', 'Deviated septum (congenital)', 'Nasal hypoplasia', 'Breathing difficulty', 'Feeding difficulty', 'Single nostril'], 'Congenital malformations of nose', 'Q30'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Prenatal factors'], 'Structural', ['Laryngeal web', 'Laryngomalacia (floppy larynx)', 'Stridor (noisy breathing)', 'Hoarse cry', 'Respiratory distress', 'Feeding difficulties'], 'Congenital malformations of larynx', 'Q31'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Prenatal factors'], 'Structural', ['Tracheal stenosis', 'Tracheomalacia (floppy trachea)', 'Tracheoesophageal fistula', 'Stridor', 'Barking cough', 'Recurrent pneumonia'], 'Congenital malformations of trachea and bronchus', 'Q32'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Prenatal factors'], 'Structural', ['Congenital pulmonary airway malformation (CPAM)', 'Pulmonary sequestration', 'Agenesis of lung', 'Respiratory distress', 'Recurrent infections', 'Cyanosis'], 'Congenital malformations of lung', 'Q33'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Prenatal factors'], 'Structural', ['Varies widely', 'Pleural effusion', 'Mediastinal cyst', 'Thymic abnormalities', 'Respiratory distress', 'Chest pain'], 'Other congenital malformations of respiratory system', 'Q34'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Teratogen exposure (e.g., smoking)'], 'Structural', ['Opening in roof of mouth', 'Feeding difficulties', 'Speech difficulties', 'Recurrent ear infections', 'Nasal regurgitation of food', 'Dental problems'], 'Cleft palate', 'Q35'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Teratogen exposure (e.g., smoking)'], 'Structural', ['Opening in upper lip', 'May involve one or both sides', 'Nasal deformity', 'Feeding difficulties', 'Speech difficulties', 'Dental problems'], 'Cleft lip', 'Q36'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Teratogen exposure'], 'Structural', ['Opening in lip and roof of mouth', 'Feeding difficulties', 'Speech difficulties', 'Recurrent ear infections', 'Nasal deformity', 'Dental problems'], 'Cleft palate with cleft lip', 'Q37'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Associated syndromes'], 'Structural', ['Short tongue (ankyloglossia)', 'Large tongue (macroglossia)', 'Cleft tongue', 'Speech difficulties', 'Feeding difficulties', 'Breathing difficulties (if large)'], 'Other congenital malformations of tongue, mouth and pharynx', 'Q38'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Vascular disruption'], 'Structural', ['Esophageal atresia (blocked esophagus)', 'Tracheoesophageal fistula', 'Vomiting', 'Choking', 'Inability to feed', 'Excessive drooling'], 'Congenital malformations of esophagus', 'Q39'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Vascular disruption'], 'Structural', ['Pyloric stenosis', 'Gastric duplication cyst', 'Microgastria', 'Projectile vomiting (pyloric stenosis)', 'Abdominal pain', 'Failure to thrive'], 'Other congenital malformations of stomach', 'Q40'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Vascular disruption'], 'Structural', ['Duodenal atresia (blockage)', 'Intestinal malrotation', 'Meckel diverticulum', 'Abdominal distension', 'Vomiting (often bile-stained)', 'Inability to pass meconium'], 'Congenital absence, atresia and stenosis of small intestine', 'Q41'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Vascular disruption'], 'Structural', ['Anal atresia (imperforate anus)', 'Colonic atresia', 'Hirschsprung disease', 'Inability to pass meconium', 'Abdominal distension', 'Vomiting'], 'Congenital absence, atresia and stenosis of large intestine', 'Q42'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Varies widely', 'Omphalocele (organs outside body)', 'Gastroschisis (organs outside body)', 'Malrotation', 'Intestinal duplication', 'Abdominal wall defect'], 'Other congenital malformations of intestine', 'Q43'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Biliary atresia (blocked bile ducts)', 'Choledochal cyst', 'Agenesis of gallbladder', 'Jaundice', 'Pale stools', 'Dark urine'], 'Congenital malformations of gallbladder, bile ducts and liver', 'Q44'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Pancreatic divisum', 'Annular pancreas', 'Pancreatic agenesis', 'Abdominal pain', 'Pancreatitis', 'Digestive problems'], 'Other congenital malformations of digestive system', 'Q45'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Hormonal factors'], 'Structural', ['Ambiguous genitalia', 'Ovarian dysgenesis', 'Vaginal agenesis', 'Amenorrhea (no period)', 'Infertility', 'Hormonal imbalance'], 'Congenital malformations of ovaries, fallopian tubes and broad ligaments', 'Q50'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Hormonal factors'], 'Structural', ['Uterine agenesis (MRKH syndrome)', 'Bicornuate uterus', 'Septate uterus', 'Recurrent miscarriages', 'Infertility', 'Amenorrhea'], 'Congenital malformations of uterus and cervix', 'Q51'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Hormonal factors'], 'Structural', ['Vaginal atresia', 'Transverse vaginal septum', 'Imperforate hymen', 'Amenorrhea', 'Pelvic pain', 'Difficulty with intercourse'], 'Other congenital malformations of female genitalia', 'Q52'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Hormonal factors'], 'Structural', ['Undescended testis (cryptorchidism)', 'Testicular agenesis', 'Testicular hypoplasia', 'Infertility risk', 'Increased cancer risk', 'Often asymptomatic'], 'Undescended testicle', 'Q53'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Hormonal factors'], 'Structural', ['Hypospadias (urethral opening on underside)', 'Epispadias (urethral opening on top)', 'Chordee (penile curvature)', 'Difficulty urinating', 'Infertility', 'Surgical correction often needed'], 'Hypospadias', 'Q54'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Hormonal factors'], 'Structural', ['Micropenis', 'Penile agenesis', 'Penile duplication', 'Varies widely', 'Hormonal imbalance', 'Psychosocial distress'], 'Other congenital malformations of male genital organs', 'Q55'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Hormonal factors'], 'Structural', ['Ambiguous genitalia', 'Ovotesticular disorder (true hermaphroditism)', 'Gonadal dysgenesis', 'Hormonal imbalance', 'Infertility', 'Complex psychosocial issues'], 'Indeterminate sex and pseudohermaphroditism', 'Q56'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Maternal health (e.g., diabetes)'], 'Structural', ['Bilateral agenesis (Potter syndrome, fatal)', 'Unilateral agenesis (often asymptomatic)', 'Oligohydramnios (low amniotic fluid)', 'Pulmonary hypoplasia', 'Facial anomalies', 'Hypertension (later in life)'], 'Renal agenesis and other reduction defects of kidney', 'Q60'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Polycystic kidney disease (ARPKD/ADPKD)', 'Renal cysts', 'Enlarged kidneys', 'Hypertension', 'Kidney failure', 'Urinary tract infections'], 'Cystic kidney disease', 'Q61'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Prenatal factors'], 'Structural', ['Vesicoureteral reflux (VUR)', 'Ureteral obstruction', 'Hydronephrosis (swollen kidney)', 'Recurrent urinary tract infections', 'Kidney damage', 'Flank pain'], 'Congenital obstructive defects of renal pelvis and malformations of ureter', 'Q62'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Horseshoe kidney', 'Ectopic kidney', 'Renal hypoplasia', 'Often asymptomatic', 'Increased risk of stones', 'Increased risk of infection'], 'Other congenital malformations of kidney', 'Q63'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Unknown etiology'], 'Structural', ['Bladder exstrophy (bladder outside body)', 'Urethral atresia', 'Posterior urethral valves (males)', 'Urinary incontinence', 'Recurrent infections', 'Difficulty urinating'], 'Other congenital malformations of urinary system', 'Q64'],
    ['Worldwide', ['Multifactorial', 'Breech presentation', 'Genetic factors (lax joints)'], 'Structural', ['Hip joint instability', 'Asymmetrical leg creases', 'Limited range of motion', 'Limping (when walking)', 'Uneven leg lengths', 'Audible "clunk" on exam (Ortolani test)'], 'Congenital deformities of hip', 'Q65'],
    ['Worldwide', ['Multifactorial', 'Intrauterine positioning', 'Genetic factors'], 'Structural', ['Clubfoot (talipes equinovarus)', 'Foot turned inward and downward', 'Metatarsus adductus', 'Rocker-bottom foot', 'Difficulty walking', 'Requires casting or surgery'], 'Congenital deformities of feet', 'Q66'],
    ['Worldwide', ['Multifactorial', 'Intrauterine positioning', 'Genetic factors'], 'Structural', ['Varies widely', 'Genu varum (bowlegs)', 'Genu valgum (knock-knees)', 'Tibial torsion', 'Femoral torsion', 'Gait abnormalities'], 'Congenital musculoskeletal deformities of knee', 'Q67'],
    ['Worldwide', ['Multifactorial', 'Intrauterine positioning', 'Amniotic band syndrome'], 'Structural', ['Varies widely', 'Congenital scoliosis', 'Torticollis (wry neck)', 'Facial asymmetry', 'Skull deformities (plagiocephaly)', 'Chest wall deformities'], 'Other congenital musculoskeletal deformities', 'Q68'],
    ['Worldwide', ['Genetic factors', 'Amniotic band syndrome', 'Developmental anomaly'], 'Structural', ['Extra finger or toe', 'Can be skin tag or fully formed digit', 'Often hereditary', 'May be associated with syndromes', 'Generally functional impact is low', 'Surgical removal common'], 'Polydactyly', 'Q69'],
    ['Worldwide', ['Genetic factors', 'Spontaneous mutation', 'Part of a syndrome (e.g., Apert)'], 'Structural', ['Webbed fingers', 'Webbed toes', 'Bony or soft tissue fusion', 'Reduced hand/foot function', 'Can be simple or complex', 'Requires surgical separation'], 'Syndactyly', 'Q70'],
    ['Worldwide', ['Genetic factors', 'Amniotic band syndrome', 'Vascular disruption'], 'Structural', ['Missing limb (amelia)', 'Partially formed limb (meromelia)', 'Phocomelia (hands/feet attached to trunk)', 'Limb hypoplasia', 'Prosthetics may be needed', 'Varies widely in severity'], 'Reduction defects of upper limb', 'Q71'],
    ['Worldwide', ['Genetic factors', 'Amniotic band syndrome', 'Vascular disruption'], 'Structural', ['Missing limb (amelia)', 'Partially formed limb (meromelia)', 'Phocomelia (hands/feet attached to trunk)', 'Limb hypoplasia', 'Prosthetics may be needed', 'Varies widely in severity'], 'Reduction defects of lower limb', 'Q72'],
    ['Worldwide', ['Genetic factors', 'Amniotic band syndrome', 'Vascular disruption'], 'Structural', ['Missing hand/foot', 'Missing finger/toe', 'Split hand/foot (ectrodactyly)', 'Varies widely', 'Functional impairment', 'Surgical/prosthetic options'], 'Reduction defects of unspecified limb', 'Q73'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Associated syndromes'], 'Structural', ['Radial club hand', 'Madelung deformity', 'Shoulder/scapula anomalies', 'Limb length discrepancy', 'Joint contractures', 'Functional impairment'], 'Other congenital malformations of upper limb(s)', 'Q74'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Associated syndromes'], 'Structural', ['Congenital shortening of femur', 'Tibial/fibular hemimelia', 'Limb length discrepancy', 'Gait abnormalities', 'Joint instability', 'Surgical intervention common'], 'Other congenital malformations of lower limb(s)', 'Q75'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Amniotic band syndrome'], 'Structural', ['Varies widely', 'Scoliosis (congenital)', 'Klippel-Feil syndrome (fused vertebrae)', 'Hemivertebrae', 'Back pain', 'Reduced mobility'], 'Congenital malformations of spine', 'Q76'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Associated syndromes'], 'Structural', ['Pectus excavatum (sunken chest)', 'Pectus carinatum (pigeon chest)', 'Absent ribs', 'Fused ribs', 'Respiratory difficulties (if severe)', 'Cosmetic concerns'], 'Congenital malformations of bony thorax', 'Q77'],
    ['Worldwide', ['Genetic factors', 'Spontaneous mutation', 'Hereditary'], 'Genetic (Skeletal)', ['Short stature (dwarfism)', 'Disproportionate limbs', 'Macrocephaly (large head)', 'Joint laxity or stiffness', 'Skeletal abnormalities', 'Varies by type (e.g., Achondroplasia)'], 'Osteochondrodysplasia with defects of growth of long bones and spine', 'Q78'],
    ['Worldwide', ['Genetic factors', 'Developmental anomaly', 'Associated syndromes'], 'Structural', ['Craniosynostosis (premature skull fusion)', 'Abnormal head shape', 'Facial asymmetry', 'Protruding eyes', 'Increased intracranial pressure', 'Developmental delay (if severe)'], 'Congenital malformations of skull and face bones', 'Q79'],
    ['Worldwide', ['Genetic factors', 'Hereditary', 'Spontaneous mutation'], 'Genetic (Skin)', ['Dry, scaly skin', 'Thickened skin', 'Skin "fish-like" scales', 'Overheating (impaired sweating)', 'Risk of skin infection', 'Reduced joint movement'], 'Congenital ichthyosis', 'Q80'],
    ['Worldwide', ['Genetic factors', 'Hereditary', 'Spontaneous mutation'], 'Genetic (Skin)', ['Skin blistering', 'Fragile skin', 'Blisters form from minor friction', 'Risk of infection', 'Scarring', 'Internal blistering (severe forms)'], 'Epidermolysis bullosa', 'Q81'],
    ['Worldwide', ['Genetic factors', 'Hereditary', 'Spontaneous mutation'], 'Genetic (Skin)', ['Varies widely', 'Abnormal hair growth (hypertrichosis)', 'Missing hair (atrichia)', 'Pigmentation disorders (albinism)', 'Vascular anomalies (port-wine stain)', 'Skin laxity (cutis laxa)'], 'Other congenital malformations of skin', 'Q82'],
    ['Worldwide', ['Genetic factors', 'Hereditary', 'Unknown etiology'], 'Genetic (Skin)', ['Absent breasts (amastia)', 'Extra nipples (polythelia)', 'Underdeveloped breasts (hypoplasia)', 'Gynaecomastia (males, congenital)', 'Often asymptomatic', 'Cosmetic concerns'], 'Congenital malformations of breast', 'Q83'],
    ['Worldwide', ['Genetic factors', 'Hereditary', 'Spontaneous mutation'], 'Genetic (Skin)', ['Ectodermal dysplasia', 'Abnormal nails', 'Abnormal hair', 'Abnormal teeth', 'Absent sweat glands', 'Heat intolerance'], 'Other congenital malformations of integument', 'Q84'],
    ['Worldwide', ['Genetic factors', 'Hereditary (Autosomal dominant)', 'Spontaneous mutation'], 'Genetic (Neurocutaneous)', ['Cafe-au-lait spots (NF1)', 'Neurofibromas (benign tumors)', 'Lisch nodules (eye)', 'Learning disabilities', 'Ash-leaf spots (Tuberous Sclerosis)', 'Seizures (Tuberous Sclerosis)'], 'Phakomatoses, not elsewhere classified (e.g., NF, TS)', 'Q85'],
    ['Worldwide', ['Genetic factors', 'Hereditary', 'Associated syndromes'], 'Multifactorial', ['Varies widely', 'Marfan syndrome (connective tissue)', 'Ehlers-Danlos syndrome (joint hypermobility)', 'Tall stature', 'Joint laxity', 'Aortic dissection risk (Marfan)'], 'Congenital malformation syndromes due to known exogenous causes', 'Q86'],
    ['Worldwide', ['Multifactorial', 'Genetic factors', 'Prenatal factors'], 'Multifactorial', ['Varies widely', 'Prader-Willi syndrome', 'Angelman syndrome', 'Sotos syndrome (overgrowth)', 'Beckwith-Wiedemann syndrome', 'Specific facial features'], 'Other specified congenital malformation syndromes', 'Q87'],
    ['Worldwide', ['Unknown etiology', 'Genetic factors', 'Developmental anomaly'], 'Structural', ['Varies widely', 'Congenital anomaly not fitting other categories', 'Rare disorders', 'Unique combinations of features', 'Consult specialist for diagnosis', 'Varies'], 'Other specified congenital malformations, not elsewhere classified', 'Q89'],
    ['Worldwide', ['Chromosomal nondisjunction', 'Maternal age factor', 'Translocation'], 'Chromosomal (Trisomy 21)', ['Intellectual disability', 'Flat facial profile', 'Upward slanting eyes', 'Single palmar crease', 'Congenital heart defects', 'Hypotonia (low muscle tone)'], 'Down syndrome', 'Q90'],
    ['Worldwide', ['Chromosomal nondisjunction', 'Maternal age factor', 'Translocation'], 'Chromosomal (Trisomy 18/13)', ['Severe intellectual disability', 'Congenital heart defects', 'Rocker-bottom feet (T18)', 'Clenched hands (T18)', 'Cleft lip/palate (T13)', 'Polydactyly (T13)'], 'Edwards syndrome (Q91.0-3) and Patau syndrome (Q91.4-7)', 'Q91'],
    ['Worldwide', ['Chromosomal nondisjunction', 'Translocation', 'Meiotic error'], 'Chromosomal', ['Varies by chromosome', 'Developmental delay', 'Intellectual disability', 'Congenital anomalies', 'Dysmorphic features', 'Growth restriction'], 'Other trisomies and partial trisomies, not elsewhere classified', 'Q92'],
    ['Worldwide', ['Chromosomal deletion', 'Spontaneous mutation', 'Inherited translocation'], 'Chromosomal', ['High-pitched cat-like cry (Cri-du-chat)', 'Intellectual disability', 'Low birth weight', 'Hypotonia', 'Microcephaly', 'Dysmorphic facial features'], 'Monosomies and deletions from the autosomes, not elsewhere classified', 'Q93'],
    ['Worldwide', ['Chromosomal translocation', 'Chromosomal inversion', 'Hereditary'], 'Chromosomal', ['Often asymptomatic (carrier)', 'Risk of infertility', 'Recurrent miscarriages', 'Risk of child with unbalanced translocation', 'No net loss/gain of genetic material', 'Varies'], 'Balanced rearrangements and structural markers, not elsewhere classified', 'Q95'],
    ['Worldwide', ['Chromosomal nondisjunction (X)', 'Monosomy X', 'Mosaicism'], 'Chromosomal (XO)', ['Short stature', 'Ovarian failure (infertility)', 'Webbed neck', 'Broad chest', 'Congenital heart defects', 'Amenorrhea'], 'Turner syndrome', 'Q96'],
    ['Worldwide', ['Chromosomal nondisjunction (X)', 'Meiotic error', 'Maternal age factor'], 'Chromosomal (e.g., XXX)', ['Often asymptomatic', 'Tall stature', 'Learning disabilities', 'Delayed speech', 'Motor skill delays', 'Premature ovarian failure (rare)'], 'Other sex chromosome abnormalities, female phenotype, not elsewhere classified', 'Q97'],
    ['Worldwide', ['Chromosomal nondisjunction (X/Y)', 'Meiotic error', 'Maternal/paternal age factor'], 'Chromosomal (e.g., XXY)', ['Tall stature', 'Small testes (hypogonadism)', 'Infertility', 'Gynecomastia (breast development)', 'Learning disabilities', 'Reduced facial/body hair'], 'Other sex chromosome abnormalities, male phenotype, not elsewhere classified', 'Q98'],
    ['Worldwide', ['Chromosomal nondisjunction', 'Mosaicism', 'Structural abnormality'], 'Chromosomal', ['Varies widely', 'Ambiguous genitalia', 'Infertility', 'Developmental delay', 'Hormonal imbalances', 'Associated anomalies'], 'Other sex chromosome abnormalities, both female and male phenotype', 'Q99']
]


# Example of how you would use this data to write a CSV file:
#
# import csv
#
# # Combine header and data
# all_data_to_write = [header] + disease_rows
#
# try:
#     with open('icd_q_dataset.csv', 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
#         writer.writerows(all_data_to_write)
#     print("Successfully wrote icd_q_dataset.csv with 100 data rows.")
#     print(f"Total rows written: {len(all_data_to_write)}")
# except IOError as e:
#     print(f"Error writing CSV file: {e}")
