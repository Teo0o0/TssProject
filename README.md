 ## Proiect Testarea Sistemelor Software

Diaconescu Teodora<br>
Voicu Stefan<br>

Îmbunătățirea testării unitare cu ajutorul inteligenței artificiale


# Obiectiv: dezvoltarea unui tool de asistență pentru estimarea complexității și lizibilitatea unui cod sursă.
În procesul de dezvoltare de software, testarea este considerată o etapă critică întrucât prin aceasta se asigură calitatea și fiabilitatea produsului. În cadrul realizării testelor, dezvoltatorii pot fi influențați de diferiți factori în timpul procesului de analiză a codului.<br><br>
Un prim astfel de factor este lizibilitatea codului sursă. Cu cât o secvență de cod este mai greu de înțeles, probabilitatea de a ignora anumite cazuri în cadrul procesului de realizare a testelor crește. Acest lucru poate avea un impact semnificativ asupra robusteții produsului rezultat.<br>
O altă metrică folosită este complexitatea sarcinii rezolvate de o secvență de cod. Aceasta se referă la dificultatea problemei și nivelul de înțelegere necesar pentru a-l realiza. În cazul sarcinilor de complexitate scăzută, testarea este relativ simplă, cu fie mai directe, fie mai puține cazuri de acoperit. Odată cu creșterea complexității, apar mai multe cazuri de tratat, din ce în ce mai marginale și greu de găsit. <br><br>
Folosim un dataset de pe Kaggle adnotat pentru antrenarea modelelor expuse mai jos. <br>
Pentru a valorifica lizibilitatea codului, folosim un model de tipul Arbori de regresie (Random Forest Regressor).<br>
Pentru problema de complexitate a taskului, folosim o rețea neurală preantrenată, CodeBERT. Trecem problema de la una de clasificare în una de regresie. Label-urile deja date se încadrează în trei clase: ușor, mediu, greu. Le valorificăm drept 0.0, 1.0, 2.0 și considerăm domeniul continuu 0-2 pentru estimarea complexității sarcinii.<br><br>
În cazul limbajului Python, fișierul source.py parcurge folderul curent, generând câte un raport pentru fiecare fișier de tip .py găsit. <br>
În cazul limbajului Java, fișierul java_worker/get_files.py parcurge folderul Tss_Test, ce conține două fișiere de tip .java, generate de ChatGPT, și scrie rapoarte pentru fiecare.<br>
Rapoartele conțin primele două metrici discutate pentru fiecare funcție găsită în parte.<br>



