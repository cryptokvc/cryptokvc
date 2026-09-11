# Intégrité des données HyperEVM

## Données et fraîcheur

Pour chaque donnée de marché, d’oracle ou de bloc, conserver la source, le timestamp, le numéro de bloc et la fenêtre de validité. Une valeur correcte mais trop ancienne peut devenir dangereuse.

## Signatures et nonces

Relier l’intention signée à la transaction effectivement envoyée. Documenter la chaîne, le nonce, les paramètres, les erreurs et le comportement en cas de reprise.

## Reconciliation

Comparer l’état attendu et l’état observé, détecter les reorgs et rendre les traitements idempotents. Un replay ne doit pas produire deux effets métier pour une seule entrée.

## Limites

Une interface compatible ne prouve pas l’exactitude de la source. Les dépendances, les clés, les permissions et les canaux de données doivent être revus séparément.
