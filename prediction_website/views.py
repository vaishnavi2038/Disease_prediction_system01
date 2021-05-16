from django.shortcuts import render
import pickle
import numpy as np
from django.core.mail import send_mail   

# disease prediction model loading file
#model=pickle.load(open("disease_predict_system.pkl","rb")) #relative path

model=pickle.load(open("./models/disease_predict_system.pkl","rb"))
model1=pickle.load(open("./models/covid_prediction_system.pkl","rb"))

#model=pickle.load(open("C:/Users/bahar/Documents/Github/Disease-Prediction-System-/prediction_website/models/disease_predict_system.pkl","rb"))
#model1=pickle.load(open("C:/Users/bahar/Documents/GitHub/Disease-Prediction-System-/prediction_website/models/covid_prediction_system.pkl","rb"))

def home(request):
    return render(request, 'index.html')

def getPredictions(request):
    if request.method=='POST':
        temp=[]
        a=request.POST.get('symptom_one')
        b=request.POST.get('symptom_two')
        c=request.POST.get('symptom_three')
        d=request.POST.get('symptom_four')
        e=request.POST.get('symptom_five')
        f=request.POST.get('symptom_six')
        temp=[a,b,c,d,e,f]

        list3=[(0, 'itching'), (1, 'skin_rash'), (2, 'nodal_skin_eruptions'), (3, 'continuous_sneezing'), (4, 'shivering'), (5, 'chills'), (6, 'joint_pain'), (7, 'stomach_pain'), (8, 'acidity'), (9, 'ulcers_on_tongue'), (10, 'muscle_wasting'), (11, 'vomiting'), (12, 'burning_micturition'), (13, 'spotting_urination'), (14, 'fatigue'), (15, 'weight_gain'), (16, 'anxiety'), (17, 'cold_hands_and_feets'), (18, 'mood_swings'), (19, 'weight_loss'), (20, 'restlessness'), (21, 'lethargy'), (22, 'patches_in_throat'), (23, 'irregular_sugar_level'), (24, 'cough'), (25, 'high_fever'), (26, 'sunken_eyes'), (27, 'breathlessness'), (28, 'sweating'), (29, 'dehydration'), (30, 'indigestion'), (31, 'headache'), (32, 'yellowish_skin'), (33, 'dark_urine'), (34, 'nausea'), (35, 'loss_of_appetite'), (36, 'pain_behind_the_eyes'), (37, 'back_pain'), (38, 'constipation'), (39, 'abdominal_pain'), (40, 'diarrhoea'), (41, 'mild_fever'), (42, 'yellow_urine'), (43, 'yellowing_of_eyes'), (44, 'acute_liver_failure'), (45, 'fluid_overload'), (46, 'swelling_of_stomach'), (47, 'swelled_lymph_nodes'), (48, 'malaise'), (49, 'blurred_and_distorted_vision'), (50, 'phlegm'), (51, 'throat_irritation'), (52, 'redness_of_eyes'), (53, 'sinus_pressure'), (54, 'runny_nose'), (55, 'congestion'), (56, 'chest_pain'), (57, 'weakness_in_limbs'), (58, 'fast_heart_rate'), (59, 'pain_during_bowel_movements'), (60, 'pain_in_anal_region'), (61, 'bloody_stool'), (62, 'irritation_in_anus'), (63, 'neck_pain'), (64, 'dizziness'), (65, 'cramps'), (66, 'bruising'), (67, 'obesity'), (68, 'swollen_legs'), (69, 'swollen_blood_vessels'), (70, 'puffy_face_and_eyes'), (71, 'enlarged_thyroid'), (72, 'brittle_nails'), (73, 'swollen_extremeties'), (74, 'excessive_hunger'), (75, 'extra_marital_contacts'), (76, 'drying_and_tingling_lips'), (77, 'slurred_speech'), (78, 'knee_pain'), (79, 'hip_joint_pain'), (80, 'muscle_weakness'), (81, 'stiff_neck'), (82, 'swelling_joints'), (83, 'movement_stiffness'), (84, 'spinning_movements'), (85, 'loss_of_balance'), (86, 'unsteadiness'), (87, 'weakness_of_one_body_side'), (88, 'loss_of_smell'), (89, 'bladder_discomfort'), (90, 'foul_smell_ofurine'), (91, 'continuous_feel_of_urine'), (92, 'passage_of_gases'), (93, 'internal_itching'), (94, 'toxic_look_(typhos)'), (95, 'depression'), (96, 'irritability'), (97, 'muscle_pain'), (98, 'altered_sensorium'), (99, 'red_spots_over_body'), (100, 'belly_pain'), (101, 'abnormal_menstruation'), (102, 'dischromic_patches'), (103, 'watering_from_eyes'), (104, 'increased_appetite'), (105, 'polyuria'), (106, 'family_history'), (107, 'mucoid_sputum'), (108, 'rusty_sputum'), (109, 'lack_of_concentration'), (110, 'visual_disturbances'), (111, 'receiving_blood_transfusion'), (112, 'receiving_unsterile_injections'), (113, 'coma'), (114, 'stomach_bleeding'), (115, 'distention_of_abdomen'), (116, 'history_of_alcohol_consumption'), (117, 'fluid_overload'), (118, 'blood_in_sputum'), (119, 'prominent_veins_on_calf'), (120, 'palpitations'), (121, 'painful_walking'), (122, 'pus_filled_pimples'), (123, 'blackheads'), (124, 'scurring'), (125, 'skin_peeling'), (126, 'silver_like_dusting'), (127, 'small_dents_in_nails'), (128, 'inflammatory_nails'), (129, 'blister'), (130, 'red_sore_around_nose'), (131, 'yellow_crust_ooze'), (132, 'prognosis')] 
        #list3=[(0, 'itching'), (1, 'skin rash'), (2, 'nodal skin eruptions'), (3, 'continuous sneezing'), (4, 'shivering'), (5, 'chills'), (6, 'joint pain'), (7, 'stomach pain'), (8, 'acidity'), (9, 'ulcers on tongue'), (10, 'muscle wasting'), (11, 'vomiting'), (12, 'burning micturition'), (13, 'spotting urination'), (14, 'fatigue'), (15, 'weight gain'), (16, 'anxiety'), (17, 'cold hands and feets'), (18, 'mood swings'), (19, 'weight loss'), (20, 'restlessness'), (21, 'lethargy'), (22, 'patches in throat'), (23, 'irregular sugar level'), (24, 'cough'), (25, 'high fever'), (26, 'sunken eyes'), (27, 'breathlessness'), (28, 'sweating'), (29, 'dehydration'), (30, 'indigestion'), (31, 'headache'), (32, 'yellowish skin'), (33, 'dark urine'), (34, 'nausea'), (35, 'loss of appetite'), (36, 'pain behind the eyes'), (37, 'back pain'), (38, 'constipation'), (39, 'abdominal pain'), (40, 'diarrhoea'), (41, 'mild fever'), (42, 'yellow urine'), (43, 'yellowing of eyes'), (44, 'acute liver failure'), (45, 'fluid overload'), (46, 'swelling of stomach'), (47, 'swelled lymph nodes'), (48, 'malaise'), (49, 'blurred and distorted vision'), (50, 'phlegm'), (51, 'throat irritation'), (52, 'redness of eyes'), (53, 'sinus pressure'), (54, 'runny nose'), (55, 'congestion'), (56, 'chest pain'), (57, 'weakness in limbs'), (58, 'fast heart rate'), (59, 'pain during bowel movements'), (60, 'pain in anal region'), (61, 'bloody stool'), (62, 'irritation in anus'), (63, 'neck pain'), (64, 'dizziness'), (65, 'cramps'), (66, 'bruising'), (67, 'obesity'), (68, 'swollen legs'), (69, 'swollen blood vessels'), (70, 'puffy face and eyes'), (71, 'enlarged thyroid'), (72, 'brittle nails'), (73, 'swollen extremeties'), (74, 'excessive hunger'), (75, 'extra marital contacts'), (76, 'drying and tingling lips'), (77, 'slurred speech'), (78, 'knee pain'), (79, 'hip joint pain'), (80, 'muscle weakness'), (81, 'stiff neck'), (82, 'swelling joints'), (83, 'movement stiffness'), (84, 'spinning movements'), (85, 'loss of balance'), (86, 'unsteadiness'), (87, 'weakness of one body side'), (88, 'loss of smell'), (89, 'bladder discomfort'), (90, 'foul smell ofurine'), (91, 'continuous feel of urine'), (92, 'passage of gases'), (93, 'internal qaitching'), (94, 'toxic look (typhos)'), (95, 'depression'), (96, 'irritability'), (97, 'muscle pain'), (98, 'altered sensorium'), (99, 'red spots over body'), (100, 'belly pain'), (101, 'abnormal menstruation'), (102, 'dischromic patches'), (103, 'watering from eyes'), (104, 'increased appetite'), (105, 'polyuria'), (106, 'family history'), (107, 'mucoid sputum'), (108, 'rusty sputum'), (109, 'lack of concentration'), (110, 'visual disturbances'), (111, 'receiving blood transfusion'), (112, 'receiving unsterile injections'), (113, 'coma'), (114, 'stomach bleeding'), (115, 'distention of abdomen'), (116, 'history of alcohol consumption'), (117, 'fluid overload'), (118, 'blood in sputum'), (119, 'prominent veins on calf'), (120, 'palpitations'), (121, 'painful walking'), (122, 'pus filled pimples'), (123, 'blackheads'), (124, 'scurring'), (125, 'skin peeling'), (126, 'silver like dusting'), (127, 'small dents in nails'), (128, 'inflammatory nails'), (129, 'blister'), (130, 'red sore around nose'), (131, 'yellow crust ooze'), (132, 'prognosis')]    
        list2=[(0, 1), (1, 3), (2, 4), (3, 4), (4, 5), (5, 3), (6, 3), (7, 5), (8, 3), (9, 4), (10, 3), (11, 5), (12, 6), (13, 6), (14, 4), (15, 3), (16, 4), (17, 5), (18, 3), (19, 3), (20, 5), (21, 2), (22, 6), (23, 5), (24, 4), (25, 7), (26, 3), (27, 4), (28, 3), (29, 4), (30, 5), (31, 3), (32, 3), (33, 4), (34, 5), (35, 4), (36, 4), (37, 3), (38, 4), (39, 4), (40, 6), (41, 5), (42, 4), (43, 4), (44, 6), (45, 6), (46, 7), (47, 6), (48, 6), (49, 5), (50, 5), (51, 4), (52, 5), (53, 4), (54, 5), (55, 5), (56, 7), (57, 7), (58, 5), (59, 5), (60, 6), (61, 5), (62, 6), (63, 5), (64, 4), (65, 4), (66, 4), (67, 4), (68, 5), (69, 5), (70, 5), (71, 6), (72, 5), (73, 5), (74, 4), (75, 5), (76, 4), (77, 4), (78, 3), (79, 2), (80, 2), (81, 4), (82, 5), (83, 5), (84, 6), (85, 4), (86, 4), (87, 4), (88, 3), (89, 4), (90, 5), (91, 6), (92, 5), (93, 4), (94, 5), (95, 3), (96, 2), (97, 2), (98, 2), (99, 3), (100, 4), (101, 6), (102, 6), (103, 4), (104, 5), (105, 4), (106, 5), (107, 4), (108, 4), (109, 3), (110, 3), (111, 5), (112, 2), (113, 7), (114, 6), (115, 4), (116, 5), (117, 4), (118, 5), (119, 6), (120, 4), (121, 2), (122, 2), (123, 2), (124, 2), (125, 3), (126, 2), (127, 2), (128, 2), (129, 4), (130, 2), (131, 3), (132, 5)]
        
        # lists for description and precaution 
        list4=[(0, 'Drug Reaction'), (1, 'Malaria'), (2, 'Allergy'), (3, 'Hypothyroidism'), (4, 'Psoriasis'), (5, 'GERD'), (6, 'Chronic cholestasis'), (7, 'hepatitis A'), (8, 'Osteoarthristis'), (9, '(vertigo) Paroymsal  Positional Vertigo'), (10, 'Hypoglycemia'), (11, 'Acne'), (12, 'Diabetes'), (13, 'Impetigo'), (14, 'Hypertension'), (15, 'Peptic ulcer diseae'), (16, 'Dimorphic hemorrhoids(piles)'), (17, 'Common Cold'), (18, 'Chicken pox'), (19, 'Cervical spondylosis'), (20, 'Hyperthyroidism'), (21, 'Urinary tract infection'), (22, 'Varicose veins'), (23, 'AIDS'), (24, 'Paralysis (brain hemorrhage)'), (25, 'Typhoid'), (26, 'Hepatitis B'), (27, 'Fungal infection'), (28, 'Hepatitis C'), (29, 'Migraine'), (30, 'Bronchial Asthma'), (31, 'Alcoholic hepatitis'), (32, 'Jaundice'), (33, 'Hepatitis E'), (34, 'Dengue'), (35, 'Hepatitis D'), (36, 'Heart attack'), (37, 'Pneumonia'), (38, 'Arthritis'), (39, 'Gastroenteritis'), (40, 'Tuberculosis')]
        list5=[(0, 'An adverse drug reaction (ADR) is an injury caused by taking medication. ADRs may occur following a single dose or prolonged administration of a drug or result from the combination of two or more drugs.'), (1, 'An infectious disease caused by protozoan parasites from the Plasmodium family that can be transmitted by the bite of the Anopheles mosquito or by a contaminated needle or transfusion. Falciparum malaria is the most deadly type.'), (2, "An allergy is an immune system response to a foreign substance that's not typically harmful to your body.They can include certain foods, pollen, or pet dander. Your immune system's job is to keep you healthy by fighting harmful pathogens."), (3, 'Hypothyroidism, also called underactive thyroid or low thyroid, is a disorder of the endocrine system in which the thyroid gland does not produce enough thyroid hormone.'), (4, "Psoriasis is a common skin disorder that forms thick, red, bumpy patches covered with silvery scales. They can pop up anywhere, but most appear on the scalp, elbows, knees, and lower back. Psoriasis can't be passed from person to person. It does sometimes happen in members of the same family."), (5, 'Gastroesophageal reflux disease, or GERD, is a digestive disorder that affects the lower esophageal sphincter (LES), the ring of muscle between the esophagus and stomach. Many people, including pregnant women, suffer from heartburn or acid indigestion caused by GERD.'), (6, 'Chronic cholestatic diseases, whether occurring in infancy, childhood or adulthood, are characterized by defective bile acid transport from the liver to the intestine, which is caused by primary damage to the biliary epithelium in most cases'), (7, "Hepatitis A is a highly contagious liver infection caused by the hepatitis A virus. The virus is one of several types of hepatitis viruses that cause inflammation and affect your liver's ability to function."), (8, 'Osteoarthritis is the most common form of arthritis, affecting millions of people worldwide. It occurs when the protective cartilage that cushions the ends of your bones wears down over time.'), (9, "Benign paroxysmal positional vertigo (BPPV) is one of the most common causes of vertigo — the sudden sensation that you're spinning or that the inside of your head is spinning. Benign paroxysmal positional vertigo causes brief episodes of mild to intense dizziness."), (10, " Hypoglycemia is a condition in which your blood sugar (glucose) level is lower than normal. Glucose is your body's main energy source. Hypoglycemia is often related to diabetes treatment. But other drugs and a variety of conditions — many rare — can cause low blood sugar in people who don't have diabetes."), (11, 'Acne vulgaris is the formation of comedones, papules, pustules, nodules, and/or cysts as a result of obstruction and inflammation of pilosebaceous units (hair follicles and their accompanying sebaceous gland). Acne develops on the face and upper trunk. It most often affects adolescents.'), (12, 'Diabetes is a disease that occurs when your blood glucose, also called blood sugar, is too high. Blood glucose is your main source of energy and comes from the food you eat. Insulin, a hormone made by the pancreas, helps glucose from food get into your cells to be used for energy.'), (13, "Impetigo (im-puh-TIE-go) is a common and highly contagious skin infection that mainly affects infants and children. Impetigo usually appears as red sores on the face, especially around a child's nose and mouth, and on hands and feet. The sores burst and develop honey-colored crusts."), (14, 'Hypertension (HTN or HT), also known as high blood pressure (HBP), is a long-term medical condition in which the blood pressure in the arteries is persistently elevated. High blood pressure typically does not cause symptoms.'), (15, 'Peptic ulcer disease (PUD) is a break in the inner lining of the stomach, the first part of the small intestine, or sometimes the lower esophagus. An ulcer in the stomach is called a gastric ulcer, while one in the first part of the intestines is a duodenal ulcer.'), (16, 'Hemorrhoids, also spelled haemorrhoids, are vascular structures in the anal canal. In their ... Other names, Haemorrhoids, piles, hemorrhoidal disease .'), (17, "The common cold is a viral infection of your nose and throat (upper respiratory tract). It's usually harmless, although it might not feel that way. Many types of viruses can cause a common cold."), (18, 'Chickenpox is a highly contagious disease caused by the varicella-zoster virus (VZV). It can cause an itchy, blister-like rash. The rash first appears on the chest, back, and face, and then spreads over the entire body, causing between 250 and 500 itchy blisters.'), (19, 'Cervical spondylosis is a general term for age-related wear and tear affecting the spinal disks in your neck. As the disks dehydrate and shrink, signs of osteoarthritis develop, including bony projections along the edges of bones (bone spurs).'), (20, "Hyperthyroidism (overactive thyroid) occurs when your thyroid gland produces too much of the hormone thyroxine. Hyperthyroidism can accelerate your body's metabolism, causing unintentional weight loss and a rapid or irregular heartbeat."), (21, 'Urinary tract infection: An infection of the kidney, ureter, bladder, or urethra. Abbreviated UTI. Not everyone with a UTI has symptoms, but common symptoms include a frequent urge to urinate and pain or burning when urinating.'), (22, 'A vein that has enlarged and twisted, often appearing as a bulging, blue blood vessel that is clearly visible through the skin. Varicose veins are most common in older adults, particularly women, and occur especially on the legs.'), (23, "Acquired immunodeficiency syndrome (AIDS) is a chronic, potentially life-threatening condition caused by the human immunodeficiency virus (HIV). By damaging your immune system, HIV interferes with your body's ability to fight infection and disease."), (24, 'Intracerebral hemorrhage (ICH) is when blood suddenly bursts into brain tissue, causing damage to your brain. Symptoms usually appear suddenly during ICH. They include headache, weakness, confusion, and paralysis, particularly on one side of your body.'), (25, 'An acute illness characterized by fever caused by infection with the bacterium Salmonella typhi. Typhoid fever has an insidious onset, with fever, headache, constipation, malaise, chills, and muscle pain. Diarrhea is uncommon, and vomiting is not usually severe.'), (26, "Hepatitis B is an infection of your liver. It can cause scarring of the organ, liver failure, and cancer. It can be fatal if it isn't treated. It's spread when people come in contact with the blood, open sores, or body fluids of someone who has the hepatitis B virus."), (27, 'In humans, fungal infections occur when an invading fungus takes over an area of the body and is too much for the immune system to handle. Fungi can live in the air, soil, water, and plants. There are also some fungi that live naturally in the human body. Like many microbes, there are helpful fungi and harmful fungi.'), (28, 'Inflammation of the liver due to the hepatitis C virus (HCV), which is usually spread via blood transfusion (rare), hemodialysis, and needle sticks. The damage hepatitis C does to the liver can lead to cirrhosis and its complications as well as cancer.'), (29, "A migraine can cause severe throbbing pain or a pulsing sensation, usually on one side of the head. It's often accompanied by nausea, vomiting, and extreme sensitivity to light and sound. Migraine attacks can last for hours to days, and the pain can be so severe that it interferes with your daily activities."), (30, 'Bronchial asthma is a medical condition which causes the airway path of the lungs to swell and narrow. Due to this swelling, the air path produces excess mucus making it hard to breathe, which results in coughing, short breath, and wheezing. The disease is chronic and interferes with daily working.'), (31, "Alcoholic hepatitis is a diseased, inflammatory condition of the liver caused by heavy alcohol consumption over an extended period of time. It's also aggravated by binge drinking and ongoing alcohol use. If you develop this condition, you must stop drinking alcohol"), (32, 'Yellow staining of the skin and sclerae (the whites of the eyes) by abnormally high blood levels of the bile pigment bilirubin. The yellowing extends to other tissues and body fluids. Jaundice was once called the "morbus regius" (the regal disease) in the belief that only the touch of a king could cure it'), (33, 'A rare form of liver inflammation caused by infection with the hepatitis E virus (HEV). It is transmitted via food or drink handled by an infected person or through infected water supplies in areas where fecal matter may get into the water. Hepatitis E does not cause chronic liver disease.'), (34, 'an acute infectious disease caused by a flavivirus (species Dengue virus of the genus Flavivirus), transmitted by aedes mosquitoes, and characterized by headache, severe joint pain, and a rash. — called also breakbone fever, dengue fever.'), (35, 'Hepatitis D, also known as the hepatitis delta virus, is an infection that causes the liver to become inflamed. This swelling can impair liver function and cause long-term liver problems, including liver scarring and cancer. The condition is caused by the hepatitis D virus (HDV).'), (36, 'The death of heart muscle due to the loss of blood supply. The loss of blood supply is usually caused by a complete blockage of a coronary artery, one of the arteries that supplies blood to the heart muscle.'), (37, 'Pneumonia is an infection in one or both lungs. Bacteria, viruses, and fungi cause it. The infection causes inflammation in the air sacs in your lungs, which are called alveoli. The alveoli fill with fluid or pus, making it difficult to breathe.'), (38, 'Arthritis is the swelling and tenderness of one or more of your joints. The main symptoms of arthritis are joint pain and stiffness, which typically worsen with age. The most common types of arthritis are osteoarthritis and rheumatoid arthritis.'), (39, 'Gastroenteritis is an inflammation of the digestive tract, particularly the stomach, and large and small intestines. Viral and bacterial gastroenteritis are intestinal infections associated with symptoms of diarrhea , abdominal cramps, nausea , and vomiting .'), (40, 'Tuberculosis (TB) is an infectious disease usually caused by Mycobacterium tuberculosis (MTB) bacteria. Tuberculosis generally affects the lungs, but can also affect other parts of the body. Most infections show no symptoms, in which case it is known as latent tuberculosis.')]
        list6=[(0, 'stop irritation, consult nearest hospital, stop taking drug, follow up'), (1, 'Consult nearest hospital, avoid oily food, avoid non veg food, keep mosquitos out'), (2, 'apply calamine, cover area with bandage, , use ice to compress itching'), (3, 'reduce stress, exercise, eat healthy, get proper sleep'), (4, 'wash hands with warm soapy water, stop bleeding using pressure, consult doctor, salt baths'), (5, 'avoid fatty spicy food, avoid lying down after eating, maintain healthy weight, exercise'), (6, 'cold baths, anti itch medicine, consult doctor, eat healthy'), (7, 'Consult nearest hospital, wash hands through, avoid fatty spicy food, medication'), (8, 'acetaminophen, consult nearest hospital, follow up, salt baths'), (9, 'lie down, avoid sudden change in body, avoid abrupt head movment, relax'), (10, 'lie down on side, check in pulse, drink sugary drinks, consult doctor'), (11, 'bath twice, avoid fatty spicy food, drink plenty of water, avoid too many products'), (12, 'have balanced diet, exercise, consult doctor, follow up'), (13, 'soak affected area in warm water, use antibiotics, remove scabs with wet compressed cloth, consult doctor'), (14, 'meditation, salt baths, reduce stress, get proper sleep'), (15, 'avoid fatty spicy food, consume probiotic food, eliminate milk, limit alcohol'), (16, 'avoid fatty spicy food, consume witch hazel, warm bath with epsom salt, consume alovera juice'), (17, 'drink vitamin c rich drinks, take vapour, avoid cold food, keep fever in check'), (18, 'use neem in bathing , consume neem leaves, take vaccine, avoid public places'), (19, 'use heating pad or cold pack, exercise, take otc pain reliver, consult doctor'), (20, 'eat healthy, massage, use lemon balm, take radioactive iodine treatment'), (21, 'drink plenty of water, increase vitamin c intake, drink cranberry juice, take probiotics'), (22, 'lie down flat and raise the leg high, use oinments, use vein compression, dont stand still for long'), (23, 'avoid open cuts, wear ppe if possible, consult doctor, follow up'), (24, 'massage, eat healthy, exercise, consult doctor'), (25, 'eat high calorie vegitables, antiboitic therapy, consult doctor, medication'), (26, 'consult nearest hospital, vaccination, eat healthy, medication'), (27, 'bath twice, use detol or neem in bathing water, keep infected area dry, use clean cloths'), (28, 'Consult nearest hospital, vaccination, eat healthy, medication'), (29, 'meditation, reduce stress, use poloroid glasses in sun, consult doctor'), (30, 'switch to loose cloothing, take deep breaths, get away from trigger, seek help'), (31, 'stop alcohol consumption, consult doctor, medication, follow up'), (32, 'drink plenty of water, consume milk thistle, eat fruits and high fiberous food, medication'), (33, 'stop alcohol consumption, rest, consult doctor, medication'), (34, 'drink papaya leaf juice, avoid fatty spicy food, keep mosquitos away, keep hydrated'), (35, 'consult doctor, medication, eat healthy, follow up'), (36, 'call ambulance, chew or swallow asprin, keep calm, '), (37, 'consult doctor, medication, rest, follow up'), (38, 'exercise, use hot and cold therapy, try acupuncture, massage'), (39, 'stop eating solid food for while, try taking small sips of water, rest, ease back into eating'), (40, 'cover mouth, consult doctor, medication, rest')]
        
        # function to convert the no 
        def get_ans(list_form):
            ans=[]
            for w in list_form:
                for i in range(0,len(list3)):
            
                    if w==list3[i][1]:
                        ans.append(list3[i][0])               
            return ans
        
        # function to convert into no 
        def get_out(list_form1):
            ans1=[]
            for w in list_form1:
                for i in range(0,len(list2)):
                    if w==list2[i][0]:
                        ans1.append(list2[i][1])
            return ans1
       
        #call the function
        f=get_ans(temp)
        answer=get_out(f)
        
        #adding extra zeroes
        if len(answer)<17:
            n=17-len(answer)
            x=[0]*n
            answer.extend(x)
              
        #predict the model
        disease=model.predict([answer])
        print(disease)
        y=[disease[0]]
        print(y)

        # getting a description and precaution 
        def comp_dis(any_disease):
            dis=[]
            for m in any_disease:
                for i in range(0,len(list4)):
                    if m==list4[i][1]:
                        dis.append(list4[i][0])
                        print(dis)
            return dis

        def desc_prec(any_disease):
            desc=[]
            prec=[]
            for m in any_disease:
                for i in range(0,len(list5)):
                    if m==(list5[i][0] and list6[i][0]):
                        desc.append(list5[i][1])
                        prec.append(list6[i][1])
            return desc,prec

        # calling the functions 
        number=comp_dis(y)
        desc,prec=desc_prec(number)
        print(desc)
        print(prec)
        desc1=str(desc[0])
        prec1=str(prec[0])
        y1=str(y[0])
        context={"disease":y1,"description":desc1,"precaution":prec1}
        print(context)      
    return render(request, 'predict.html', context)

def covidPredict(request):
    if request.method=='POST':
        a = request.POST.get('Breathing Problem')
        b = request.POST.get('Fever')
        c = request.POST.get('Dry Cough')
        d = request.POST.get('Sore Throat')
        e = request.POST.get('Asthma')
        f = request.POST.get('Chronic Lung Disease')
        g = request.POST.get('Hyper Tension')
        h = request.POST.get('Abroad travel')
        i = request.POST.get('Contact with COVID Patient')
        j = request.POST.get('Attended Large Gathering')
        k = request.POST.get('Visited Public Exposed Places')
        l = request.POST.get('Family working in Public Exposed Places')
        covid_input = [a,b,c,d,e,f,g,h,i,j,k,l]
        for i in range(0, len(covid_input)):
            covid_input[i] = int(covid_input[i])
        print(covid_input)

        #predicting the covid output
        covid_pred=model1.predict([covid_input])
        print(covid_pred)
        covid=[]
        for z in covid_pred:
            if z==1:
                covid="you may have covid"         # add a message 
            else:
                covid="your infection risk is low"   # add a message 
        print(covid)

        context={"covid_predicted":covid}
    return render(request, 'covid.html', context)
    
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        #send an email
        send_mail(
            name, #subject
            message, #message
            email, #from mail
            ['prediction.website@gmail.com'] #to mail
            )
        
        return render(request, 'index.html', {})
    else:
        return render(request, 'index.html',)