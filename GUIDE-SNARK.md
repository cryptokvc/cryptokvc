# Systèmes SNARK

## Modèle

Un SNARK permet de prouver la connaissance d’un witness satisfaisant un circuit ou un système de contraintes, avec une vérification compacte.

## Circuit et witness

Distinguer les entrées publiques, les valeurs privées, les contraintes et les conversions de représentation. Une contrainte absente peut invalider l’intention métier malgré une preuve cryptographiquement correcte.

## Paramètres et clés

Identifier le rôle du SRS, de la cérémonie éventuelle, de la proving key et de la verification key. Documenter les hypothèses de confiance et les risques liés à une mauvaise génération des paramètres.

## Vérification

Suivre les encodages, le transcript, les contrôles de pairing ou de groupe et la gestion des erreurs. Une preuve valide atteste le circuit prouvé, pas les propriétés non exprimées dans ce circuit.
