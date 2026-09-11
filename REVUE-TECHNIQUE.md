# Grille de revue technique

## Questions essentielles

Quel est le périmètre exact ? Quelle donnée entre dans le système ? Qui la signe ou l’atteste ? Quelle transformation est appliquée ? Quelle sortie est autorisée ?

## Vérifications

Relire les chemins nominaux et les erreurs : données absentes, timestamps périmés, nonce inattendu, preuve invalide, reorg, replay, dépassement de budget de bruit ou échec de déchiffrement.

## Preuves

Associer chaque conclusion à une révision, un fichier et, si nécessaire, une fonction précise. Marquer clairement ce qui est observé, déduit ou non vérifié.

## Restitution

Présenter architecture, invariants, frontières de confiance et modes d’échec avant les considérations de performance. Ne jamais présenter une documentation statique comme un audit ou une garantie de production.
