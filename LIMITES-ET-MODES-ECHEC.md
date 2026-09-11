# Limites et modes d’échec

## Données

Une donnée peut être absente, périmée, incohérente ou issue d’une source compromise. Chaque parcours doit préciser fraîcheur, provenance et réaction attendue.

## État blockchain

Couvrir reorgs, replays, nonces inattendus, divergence L1/L2 et reprise après interruption. Les traitements importants doivent être idempotents ou détecter explicitement les doublons.

## Cryptographie

Une preuve peut être valide pour un circuit incomplet, un budget FHE peut être épuisé et une hypothèse de SRS peut être mal comprise. Relier chaque garantie à son hypothèse exacte.

## Périmètre

Cette bibliothèque est documentaire. Elle ne remplace ni audit, ni test de production, ni revue des clés, dépendances, permissions et procédures opérationnelles.
