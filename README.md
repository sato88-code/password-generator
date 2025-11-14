# 🔐 Generatore di Password

Siamo onesti: inventarsi password sicure è una noia mortale, e finiamo sempre per usare "Password123!".
Ho creato questo script in Python per risolvere il problema e generare password robuste (e impossibili da ricordare, ma sicure!).

Come funziona??
È un tool da terminale molto semplice:
1. Gli dici quanto lunga vuoi la password.
2. Gli dici se vuoi aggiungere simboli speciali (`!`, `@`, `#`, ecc.) per renderla ancora più sicura.
3. Lui te la crea all'istante.

Cosa ho imparato facendolo:
Rispetto ai miei primi esperimenti, qui ho lavorato su:
- **Non far crashare tutto:** Ho inserito un controllo (ciclo `while`) che "costringe" l'utente a rispondere correttamente sì o no, così il programma non esplode se sbagli a scrivere.
- **Gestione delle stringhe:** Ho usato la libreria `string` per non dover scrivere a mano tutto l'alfabeto.
- **Codice pulito:** Ho cercato di scrivere la logica una volta sola, evitando ripetizioni inutili.

---
*Codice scritto per esercizio e per sicurezza digitale.* 🕵️‍♂️
