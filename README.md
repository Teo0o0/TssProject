TssProject
 
## Proiect Testarea Sistemelor Software

Diaconescu Teodora<br>
Voicu Stefan<br>

Îmbunătățirea testării unitare cu ajutorul inteligenței artificiale

# Partea 1
<br>Scopul I: dezvoltarea unui tool de asistență pentru estimarea complexității și lizibilitatea unui cod sursă. <br><br>
Se împarte codul în secvențe, ca mai apoi să se estimeze o măsură a fiecăreia pentru a ajuta dezvoltatorii în a pune accent pe anumite părți din cod în realizarea unor teste.<br>
În procesul de dezvoltare de software, testarea este considerată o etapă critică întrucât prin aceasta se asigură calitatea și fiabilitatea produsului. În cadrul realizării testelor, dezvoltatorii pot fi influențați de diferiți factori în timpul procesului de analiză a codului.<br>
Un prim astfel de factor este lizibilitatea codului sursă. Cu cât o secvență de cod este mai greu de înțeles, probabilitatea de a ignora anumite cazuri în cadrul procesului de realizare a testelor crește. Acest lucru poate avea un impact semnificativ asupra robusteții produsului rezultat.<br>
O altă metrică folosită este complexitatea sarcinii rezolvate de o secvență de cod. Aceasta se referă la dificultatea problemei și nivelul de înțelegere necesar pentru a-l realiza. În cazul sarcinilor de complexitate scăzută, testarea este relativ simplă, cu fie mai directe, fie mai puține cazuri de acoperit. Odată cu creșterea complexității, apar mai multe cazuri de tratat, din ce în ce mai marginale și greu de găsit. <br>
Folosim un dataset de pe Kaggle adnotat pentru antrenarea modelelor expuse mai jos. <br>
Pentru măsurarea lizibilității codului există librării deja definite, de exemplu pylint pentru Python. Pentru a valorifica acest aspect al codului, folosim un model de tipul Arbori de regresie (Random Forest Regressor).<br>
Pentru problema de complexitate a taskului, folosim o rețea neurală preantrenată, CodeBERT. Trecem problema de la una de clasificare în una de regresie. Label-urile deja date se încadrează în trei clase: ușor, mediu, greu. Le valorificăm drept 0.0, 1.0, 2.0 și considerăm domeniul continuu 0-2 pentru estimarea complexității sarcinii.<br>
Fișierul source.py parcurge un folder și trece toate fișierele de tip .py drept argument pentru main.py. Funcția acestuia este de a sparge codul în funcții și de a genera un fișier în care atribuie fiecărei funcții un scor de lizibilitate și unul de cyclomatic_complexity.<br>

