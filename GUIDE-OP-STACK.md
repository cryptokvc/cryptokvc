# Architecture OP Stack

## Séparation des couches

Distinguer règlement L1, séquenceur, dérivation, exécution et publication des données. Chaque couche possède ses propres hypothèses et son propre horizon de confirmation.

## Dérivation

Suivre la transformation des entrées L1 en dépôts, messages et blocs L2. Les numéros de bloc, timestamps, séquences et replays doivent rester cohérents lors d’une reprise.

## Préconfirmations et finalité

Une préconfirmation est un signal opérationnel distinct de l’inclusion L1 et de la finalité. La documentation doit indiquer précisément quel événement est observé avant de parler de confirmation.

## Modes d’échec

Couvrir retard de publication, reorg, données indisponibles, divergence de dérivation et reprise du séquenceur. Une architecture robuste rend ces états détectables et explicites.
