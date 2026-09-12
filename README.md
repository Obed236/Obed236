# Privaty Car — démo

Cette branche contient la V1 corrigée de Privaty Car, adaptée à la charte graphique officielle.

## Charte intégrée

- palette officielle : noir `#000000`, blanc `#FFFFFF`, doré `#D1AE72` ;
- logotype officiel Privaty Car ;
- Poppins Light pour l'interface ;
- présentation sobre et premium cohérente avec l'univers chauffeur privé.

## Fonctionnel

- réservation de course ;
- paiement Stripe configurable par variables d'environnement ;
- espace administrateur ;
- gestion séparée du statut de course : En attente / Accepter / Refuser ;
- statut de paiement conservé séparément.

## Démarrage de cette branche

Le projet est stocké sous forme de payload compressé afin de conserver l'ensemble de la V1 dans cette branche.

```bash
python bootstrap.py
pip install -r Privaty_Car_V1/requirements.txt
gunicorn wsgi:app
```

`bootstrap.py` reconstruit automatiquement le projet dans `Privaty_Car_V1/` à partir des fichiers `privaty_payload_0.b64` à `privaty_payload_2.b64`.

La charge utile est une archive TAR.XZ encodée en base64, en trois parties, compatible avec la commande de construction Render existante. La charte du 12 septembre inclut les polices locales et les photos fournies.
