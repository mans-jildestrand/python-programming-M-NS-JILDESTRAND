# Laboration 3 – Linjär klassificering

## Beskrivning

Detta projekt undersöker hur **linjär klassificering** kan användas för att dela upp datapunkter i två klasser.

Syftet är att implementera en enkel linjär modell i Python, analysera resultatet visuellt och förstå hur olika lutningar och intercept påverkar klassificeringen.

Projektet inkluderar:

* Inläsning av datapunkter från en CSV-fil.
* Klassificering av punkter med olika linjära gränser.
* Visualisering av punkter och linjer i diagram.
* Analys av hur linjens parametrar påverkar indelningen av datapunkter.

---

## Filer

* **Labb3.py** – Huvudprogrammet som läser in data, klassificerar punkter och plottar resultaten.
* **Functions.py** – Funktion för att dela upp punkter ovanför och under en given linje.
* **unlabelled_data.csv** – Dataset som används för klassificeringen.
* **labelled_data.csv** – Fil som genereras med punkter och deras tilldelade klasser.
* **Rapport.ipynb** – Jupyter Notebook-version av laborationen med text, kod och diagram.
* **README.md** – Denna fil.

---

## Installation och körning

1. Se till att Python är installerat.
2. Installera nödvändiga bibliotek (om inte redan installerade):

<pre class="overflow-visible!" data-start="1434" data-end="1474"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install numpy matplotlib
</span></span></code></div></div></pre>

3. Kör programmet:

<pre class="overflow-visible!" data-start="1498" data-end="1525"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python Labb3.py
</span></span></code></div></div></pre>

Programmet kommer då att:

* Läsa in `unlabelled_data.csv`
* Klassificera punkterna med linjära funktioner
* Spara en ny fil `labelled_data.csv` med tilldelade etiketter
* Visa ett diagram med punkter och linjer

4. För att se rapporten i notebook-format, öppna **Rapport.ipynb** i Jupyter Notebook eller Jupyter Lab.
