# Signatures EVM

## Intention

Relier le message signé à l’action réellement exécutée : chaîne, contrat, fonction, paramètres, valeur et destinataire. Une signature valide ne rend pas sûre une intention mal présentée.

## Nonce et replay

Documenter le nonce, l’identifiant de chaîne, l’expiration et les mécanismes anti-rejeu. Les transactions répétées ou déplacées vers un autre contexte doivent être rejetées lorsque le protocole l’exige.

## Encodage

Comparer l’encodage signé avec celui vérifié par le contrat, notamment pour EIP-712 et les types dynamiques. Les divergences d’encodage sont une source classique de validation trompeuse.

## Vérification

Suivre récupération du signataire, permissions, erreurs et changements de clé. La revue doit couvrir le chemin nominal et les réponses aux signatures périmées ou mal formées.
