# US21-Blockchain
Repo para los desarrollos relacionados al proyecto de investigación de blockchain

# Objetivo
Desarrollar software que tome documentos y los valide contra una blockchain donde se haya guardado su hash.

# Metodología
El PoC consta de dos scripts en python, que deben ser ejecutados en una terminal:

- NavegarBloques.py consulta los últimos bloques y muestra su información
```mermaid
flowchart TD

A[Inicio]
B[Obtener último bloque]
C[Seleccionar bloque N]
D[Consultar bloque vía JSON-RPC]
E[Mostrar Hash]
F[Mostrar Parent Hash]
G[Mostrar Gas y Timestamp]
H[Mostrar Transacciones]
I[¿Quedan bloques?]
J[Fin]

A --> B
B --> C
C --> D
D --> E
E --> F
F --> G
G --> H
H --> I

I -->|Sí| C
I -->|No| J
```
- ComprobarHash.py valida que un hash existe en un cierto bloque, permitiendo así comprobar que un documento no fue modificado luego de guardar su hash en la blockchain

```mermaid
flowchart TD

A[Documento a Validar]
B[Metadatos Registrados<br/>Hash Documento + Nº Bloque + Hash Esperado]
C[Consultar Bloque en BFA]
D[Obtener Hash del Bloque<br/>desde la Blockchain BFA]
E[Comparar Hashes]
F[Documento Validado]
G[Validación Fallida]

A --> B
B --> C
C --> D
D --> E

E -->|Coincide| F
E -->|No coincide| G
```



Este software usa la testnet de BFA, validando contra la API pública en el endpoint http://public.test2.bfa.ar:8545, obtenido de la documentación del proyecto BFA.

# Requerimientos
Sólo requieren la librería requests, que puede ser instalada mediante
$ python -m pip install requests
