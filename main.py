import pandas as pd
import functions as fn 
import json

# Carica il file JSON
with open("controls.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Crea il DataFrame
df = pd.DataFrame(data)


#carica controlli in una lista di dict chiamata `controlli`
controlli = df.to_dict(orient='records')

descrizioni = [c["descrizione"] for c in controlli]
# unisci le descrizioni in un'unica stringa
descrizioni = " ".join(descrizioni)

pool_result = fn.estrai_keywords_bert(descrizioni, top_n=30)

print("Pool iniziale di keyword:")
print(list(set(pool_result)))

