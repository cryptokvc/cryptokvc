# Systèmes STARK

## Trace et contraintes

Un calcul est représenté par une trace dont les colonnes et transitions doivent respecter des contraintes algébriques. L’analyse doit identifier le témoin, les bornes et les conditions initiales.

## AIR et engagement

L’AIR décrit les relations vérifiables sur la trace. Le prouveur engage ensuite des évaluations ou des couches dérivées ; le vérificateur contrôle que les ouvertures correspondent au même objet engagé.

## FRI et transcript

FRI réduit la vérification d’un polynôme à des contrôles récursifs de faible degré. Le transcript Fiat-Shamir lie les défis aux engagements précédents et doit être suivi dans l’ordre exact.

## Revue

Relier ces étapes aux fonctions du dépôt, aux paramètres et aux erreurs. La taille de preuve et le coût de vérification ne suffisent pas à conclure sur la sécurité globale.
